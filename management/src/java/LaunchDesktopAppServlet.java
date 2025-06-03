
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/LaunchDesktopAppServlet")
public class LaunchDesktopAppServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        try {
            // Path to your desktop application JAR file
            String jarPath = "path/to/your/EmployeeManagementSystem.jar";
            
            // Launch the desktop application
            Runtime.getRuntime().exec("java -jar " + jarPath);
            
            response.sendRedirect("dashboard.jsp?message=Application+launched");
        } catch (IOException ex) {
            response.sendRedirect("dashboard.jsp?error=Failed+to+launch+application");
        }
    }
}