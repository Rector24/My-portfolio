/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package management.gui;

import java.sql.Connection;
import java.sql.SQLException;

/**
 *
 * @author Moreb
 */
public class ManagementGui {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        try {
            // Get the connection using the static method
            Connection connection = DBConnection.getConnection();
            
            // Test connection
            if (connection != null && !connection.isClosed()) {
                System.out.println("Database connection established successfully!");
                
                // Here you would typically launch your main GUI frame
                // new MainFrame(connection).setVisible(true);
            }
            
        } catch (SQLException ex) {
            System.err.println("Database connection error: " + ex.getMessage());
            ex.printStackTrace();
        } finally {
            // Consider moving this to a shutdown hook or application exit handler
            DBConnection.closeConnection();
        }
    }
}