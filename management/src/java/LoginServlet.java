import jakarta.servlet.RequestDispatcher;
import java.io.IOException;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

@WebServlet("/LoginServlet")
public class LoginServlet extends HttpServlet {
    
    private static final Logger LOGGER = Logger.getLogger(LoginServlet.class.getName());
    private static final int MAX_LOGIN_ATTEMPTS = 3;
    private static final String DB_URL = "jdbc:postgresql://localhost:5432/employee_db";
    private static final String DB_USER = "postgres";
    private static final String DB_PASSWORD = "admin"; // Change to your PostgreSQL password
    
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        response.sendRedirect("login.jsp");
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        
        String employeeId = request.getParameter("txtEmployeeID");
        String password = request.getParameter("txtPassword");
        
        // Input validation
        if (isEmpty(employeeId) || isEmpty(password)) {
            setErrorAndForward(request, response, "Employee ID and password are required!");
            return;
        }
        
        try {
            Class.forName("org.postgresql.Driver");
            
            try (Connection con = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD)) {
                // Check if user exists first
                if (!userExists(con, employeeId)) {
                    setErrorAndForward(request, response, "Invalid Employee ID or Password");
                    return;
                }
                
                // Check account status
                if (isAccountLocked(con, employeeId)) {
                    setErrorAndForward(request, response, "Your account is locked. Please contact administrator.");
                    return;
                }
                
                // Authenticate user
                if (authenticateUser(con, employeeId, password)) {
                    handleSuccessfulLogin(con, request, response, employeeId);
                } else {
                    handleFailedLogin(con, request, response, employeeId);
                }
            }
        } catch (ClassNotFoundException ex) {
            LOGGER.log(Level.SEVERE, "JDBC Driver not found", ex);
            setErrorAndForward(request, response, "System error. Please try again later.");
        } catch (SQLException ex) {
            LOGGER.log(Level.SEVERE, "Database error", ex);
            setErrorAndForward(request, response, "Database error. Please try again later.");
        }
    }
    
    private boolean isEmpty(String str) {
        return str == null || str.trim().isEmpty();
    }
    
    private boolean userExists(Connection con, String employeeId) throws SQLException {
        String query = "SELECT employee_id FROM Employee WHERE employee_id = ?";
        try (PreparedStatement stmt = con.prepareStatement(query)) {
            stmt.setString(1, employeeId);
            return stmt.executeQuery().next();
        }
    }
    
    private boolean isAccountLocked(Connection con, String employeeId) throws SQLException {
        String query = "SELECT account_locked FROM Loginn WHERE employee_id = ?";
        try (PreparedStatement stmt = con.prepareStatement(query)) {
            stmt.setString(1, employeeId);
            ResultSet rs = stmt.executeQuery();
            return rs.next() && rs.getBoolean("account_locked");
        }
    }
    
    private boolean authenticateUser(Connection con, String employeeId, String password) throws SQLException {
        String query = "SELECT e.employee_name, e.employee_surname, e.employee_role "
                + "FROM Employee e "
                + "JOIN Loginn l ON e.employee_id = l.employee_id "
                + "WHERE l.employee_id = ? AND l.employee_password = ?";
        
        try (PreparedStatement stmt = con.prepareStatement(query)) {
            stmt.setString(1, employeeId);
            stmt.setString(2, password);
            
            ResultSet rs = stmt.executeQuery();
            return rs.next(); // Returns true if credentials are valid
        }
    }
    
    private void handleSuccessfulLogin(Connection con, HttpServletRequest request, 
            HttpServletResponse response, String employeeId) throws SQLException, IOException, ServletException {
        // Reset login attempts and update last login
        String updateQuery = "UPDATE Loginn SET login_attempts = 0, last_login = CURRENT_TIMESTAMP WHERE employee_id = ?";
        try (PreparedStatement stmt = con.prepareStatement(updateQuery)) {
            stmt.setString(1, employeeId);
            stmt.executeUpdate();
        }
        
        // Get user details for session
        String userQuery = "SELECT employee_name, employee_surname, employee_role FROM Employee WHERE employee_id = ?";
        try (PreparedStatement stmt = con.prepareStatement(userQuery)) {
            stmt.setString(1, employeeId);
            ResultSet rs = stmt.executeQuery();
            
            if (rs.next()) {
                HttpSession session = request.getSession();
                session.setAttribute("employeeId", employeeId);
                session.setAttribute("employeeName", rs.getString("employee_name"));
                session.setAttribute("employeeSurname", rs.getString("employee_surname"));
                session.setAttribute("employeeRole", rs.getString("employee_role"));
                
                // Redirect based on role
                String redirectPage = "admin".equalsIgnoreCase(rs.getString("employee_role")) 
                        ? "adminDashboard.jsp" : "dashboard.jsp";
                response.sendRedirect(redirectPage);
            }
        }
    }
    
    private void handleFailedLogin(Connection con, HttpServletRequest request, 
            HttpServletResponse response, String employeeId) throws SQLException, ServletException, IOException {
        // Increment login attempts
        String incrementQuery = "UPDATE Loginn SET login_attempts = login_attempts + 1 WHERE employee_id = ?";
        try (PreparedStatement stmt = con.prepareStatement(incrementQuery)) {
            stmt.setString(1, employeeId);
            stmt.executeUpdate();
        }
        
        // Check if account should be locked
        String checkQuery = "SELECT login_attempts FROM Loginn WHERE employee_id = ?";
        try (PreparedStatement stmt = con.prepareStatement(checkQuery)) {
            stmt.setString(1, employeeId);
            ResultSet rs = stmt.executeQuery();
            
            if (rs.next() && rs.getInt("login_attempts") >= MAX_LOGIN_ATTEMPTS) {
                String lockQuery = "UPDATE Loginn SET account_locked = TRUE WHERE employee_id = ?";
                try (PreparedStatement lockStmt = con.prepareStatement(lockQuery)) {
                    lockStmt.setString(1, employeeId);
                    lockStmt.executeUpdate();
                }
                setErrorAndForward(request, response, "Too many failed attempts. Account locked.");
            } else {
                int attemptsLeft = MAX_LOGIN_ATTEMPTS - rs.getInt("login_attempts");
                setErrorAndForward(request, response, 
                    "Invalid Employee ID or Password. " + attemptsLeft + " attempts remaining.");
            }
        }
    }
    
    private void setErrorAndForward(HttpServletRequest request, HttpServletResponse response, 
            String errorMessage) throws ServletException, IOException {
        request.setAttribute("error", errorMessage);
        RequestDispatcher rd = request.getRequestDispatcher("login.jsp");
        rd.forward(request, response);
    }
}