import jakarta.servlet.*;
import jakarta.servlet.http.*;
import jakarta.servlet.annotation.*;
import java.io.IOException;
import java.sql.*;
import java.util.logging.*;

@WebServlet("/RegisterServlet")
public class RegisterServlet extends HttpServlet {
    
    private static final Logger LOGGER = Logger.getLogger(RegisterServlet.class.getName());
    private static final String DB_URL = "jdbc:postgresql://localhost:5432/employee_db";
    private static final String DB_USER = "postgres";
    private static final String DB_PASSWORD = "admin"; // Change to your actual password
    
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        
        // Get all form parameters
        String employeeId = request.getParameter("txtEmployeeID");
        String name = request.getParameter("txtName");
        String surname = request.getParameter("txtSurname");
        String department = request.getParameter("txtDepartment");
        String role = request.getParameter("txtRole");
        String phone = request.getParameter("txtPhoneNumber");
        String email = request.getParameter("txtEmail");
        String password = request.getParameter("txtPassword");
        String confirmPassword = request.getParameter("txtConfirmPassword");
        
        // Validate inputs
        if (isEmpty(employeeId) || isEmpty(name) || isEmpty(surname) || 
            isEmpty(department) || isEmpty(role) || isEmpty(phone) ||
            isEmpty(email) || isEmpty(password) || isEmpty(confirmPassword)) {
            setErrorAndForward(request, response, "All fields are required!");
            return;
        }
        
        if (!password.equals(confirmPassword)) {
            setErrorAndForward(request, response, "Passwords do not match!");
            return;
        }
        
        if (password.length() < 8) {
            setErrorAndForward(request, response, "Password must be at least 8 characters long!");
            return;
        }
        
        try (Connection con = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD)) {
            // Check if employee ID already exists
            if (employeeExists(con, employeeId)) {
                setErrorAndForward(request, response, "Employee ID already exists!");
                return;
            }
            
            // Check if email already exists
            if (emailExists(con, email)) {
                setErrorAndForward(request, response, "Email already registered!");
                return;
            }
            
            // Start transaction
            con.setAutoCommit(false);
            
            try {
                // Insert into Employee table
                String employeeQuery = "INSERT INTO Employee (employee_id, employee_name, employee_surname, "
                    + "employee_department, employee_role, employee_phone, employee_email) "
                    + "VALUES (?, ?, ?, ?, ?, ?, ?)";
                
                try (PreparedStatement stmt = con.prepareStatement(employeeQuery)) {
                    stmt.setString(1, employeeId);
                    stmt.setString(2, name);
                    stmt.setString(3, surname);
                    stmt.setString(4, department);
                    stmt.setString(5, role);
                    stmt.setString(6, phone);
                    stmt.setString(7, email);
                    stmt.executeUpdate();
                }
                
                // Insert into Login table (WARNING: plain text password - use BCrypt in production)
                String loginQuery = "INSERT INTO Loginn (employee_id, employee_password) VALUES (?, ?)";
                try (PreparedStatement stmt = con.prepareStatement(loginQuery)) {
                    stmt.setString(1, employeeId);
                    stmt.setString(2, password);
                    stmt.executeUpdate();
                }
                
                // Commit transaction
                con.commit();
                
                // Registration successful
                request.setAttribute("success", "Registration successful! Please login.");
                request.getRequestDispatcher("login.jsp").forward(request, response);
                
            } catch (SQLException e) {
                // Rollback on error
                try {
                    if (con != null) con.rollback();
                } catch (SQLException ex) {
                    LOGGER.log(Level.SEVERE, "Error during rollback", ex);
                }
                throw e;
            } finally {
                try {
                    con.setAutoCommit(true);
                } catch (SQLException ex) {
                    LOGGER.log(Level.WARNING, "Error resetting auto-commit", ex);
                }
            }
            
        } catch (SQLException ex) {
            LOGGER.log(Level.SEVERE, "Database error details: " + ex.getMessage(), ex);
            setErrorAndForward(request, response, 
                "Registration failed. Error: " + extractUserFriendlyError(ex));
        }
    }
    
    private boolean isEmpty(String str) {
        return str == null || str.trim().isEmpty();
    }
    
    private boolean employeeExists(Connection con, String employeeId) throws SQLException {
        String query = "SELECT 1 FROM Employee WHERE employee_id = ?";
        try (PreparedStatement stmt = con.prepareStatement(query)) {
            stmt.setString(1, employeeId);
            try (ResultSet rs = stmt.executeQuery()) {
                return rs.next();
            }
        }
    }
    
    private boolean emailExists(Connection con, String email) throws SQLException {
        String query = "SELECT 1 FROM Employee WHERE employee_email = ?";
        try (PreparedStatement stmt = con.prepareStatement(query)) {
            stmt.setString(1, email);
            try (ResultSet rs = stmt.executeQuery()) {
                return rs.next();
            }
        }
    }
    
    private String extractUserFriendlyError(SQLException ex) {
        // Handle specific error cases
        if (ex.getMessage().contains("connection refused")) {
            return "Cannot connect to database. Please try again later.";
        } else if (ex.getMessage().contains("violates unique constraint")) {
            return "The employee ID or email is already registered.";
        } else if (ex.getMessage().contains("password authentication failed")) {
            return "Database authentication failed.";
        }
        return "Please check your input and try again.";
    }
    
    private void setErrorAndForward(HttpServletRequest request, HttpServletResponse response, 
            String errorMessage) throws ServletException, IOException {
        request.setAttribute("error", errorMessage);
        request.getRequestDispatcher("register.jsp").forward(request, response);
    }
}