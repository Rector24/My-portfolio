import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Statement;

public class DBConnection {
    private static final String DRIVER = "org.apache.derby.jdbc.EmbeddedDriver";
    private static final String JDBC_URL = "jdbc:derby:employee_management_db;create=true";
    
    private Connection con;
    
    public DBConnection() throws ClassNotFoundException, SQLException {
        Class.forName(DRIVER);
        this.con = DriverManager.getConnection(JDBC_URL);
        System.out.println("Connected to JavaDB database");
        createTables(); // Create tables if they don't exist
    }
    
    private void createTables() throws SQLException {
        // Create Employee table
        String employeeTableSQL = "CREATE TABLE Employee ("
                + "employee_id VARCHAR(20) PRIMARY KEY,"
                + "employee_name VARCHAR(50) NOT NULL,"
                + "employee_surname VARCHAR(50) NOT NULL,"
                + "employee_department VARCHAR(50) NOT NULL,"
                + "employee_role VARCHAR(50) NOT NULL,"
                + "employee_phone VARCHAR(15) NOT NULL,"
                + "employee_email VARCHAR(100) NOT NULL)";
        
        // Create Department table
        String departmentTableSQL = "CREATE TABLE Department ("
                + "department_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY (START WITH 1, INCREMENT BY 1),"
                + "department_name VARCHAR(50) NOT NULL,"
                + "manager_id VARCHAR(20) REFERENCES Employee(employee_id))";
        
        // Create Payroll table
        String payrollTableSQL = "CREATE TABLE Payroll ("
                + "payroll_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY (START WITH 1, INCREMENT BY 1),"
                + "employee_id VARCHAR(20) REFERENCES Employee(employee_id),"
                + "salary DECIMAL(10,2) NOT NULL,"
                + "bonus DECIMAL(10,2) DEFAULT 0,"
                + "tax DECIMAL(10,2) NOT NULL,"
                + "payment_date DATE NOT NULL)";
        
        try (Statement stmt = con.createStatement()) {
            // Try to create tables, ignore if they already exist
            try { stmt.execute(employeeTableSQL); } catch (SQLException e) {}
            try { stmt.execute(departmentTableSQL); } catch (SQLException e) {}
            try { stmt.execute(payrollTableSQL); } catch (SQLException e) {}
        }
    }
    
    public Connection getConnection() {
        return con;
    }
    
    public void closeConnection() {
        if (con != null) {
            try {
                con.close();
                System.out.println("Database connection closed");
            } catch (SQLException ex) {
                System.err.println("Error closing connection: " + ex.getMessage());
            }
        }
    }
    
    // CRUD operations for Employee
    public boolean addEmployee(String id, String name, String surname, String department, 
            String role, String phone, String email) throws SQLException {
        String sql = "INSERT INTO Employee VALUES (?, ?, ?, ?, ?, ?, ?)";
        try (PreparedStatement pstmt = con.prepareStatement(sql)) {
            pstmt.setString(1, id);
            pstmt.setString(2, name);
            pstmt.setString(3, surname);
            pstmt.setString(4, department);
            pstmt.setString(5, role);
            pstmt.setString(6, phone);
            pstmt.setString(7, email);
            return pstmt.executeUpdate() > 0;
        }
    } 
}
