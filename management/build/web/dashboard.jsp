<%-- 
    Document   : dashboard
    Created on : 30 May 2025, 15:35:12
    Author     : Moreb
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Employee Dashboard</title>
        <style>
            /* Navy and Gold Professional Theme - Matching Register Page */
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                font-size: 18px;
                text-align: center;
                margin-top: 50px;
                background-color: #f8f9fa;
            }
            
            h1 { 
                color: #0a2540; /* Navy blue */
                font-size: 36px;
                margin-bottom: 10px;
            }
            
            h2 { 
                color: #d4af37; /* Gold */
                margin-bottom: 30px;
                font-weight: 400;
            }
            
            .welcome-message {
                color: #6c757d; /* Medium gray */
                margin-bottom: 30px;
                font-size: 1.2em;
            }
            
            form {
                width: 600px;
                margin: 0 auto;
                padding: 40px;
                border-radius: 8px;
                background: white;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
                border: none;
            }
            
            hr {
                border: 0;
                height: 1px;
                background: linear-gradient(to right, transparent, #d4af37, transparent);
                margin: 25px 0;
            }
            
            a, input[type="submit"] {
                text-decoration: none;
                color: white;
                background-color: #0a2540; /* Navy blue */
                padding: 14px 28px;
                border-radius: 6px;
                font-weight: 500;
                transition: all 0.3s;
                display: inline-block;
                margin-top: 20px;
                font-size: 18px;
                border: none;
                cursor: pointer;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            
            a:hover, input[type="submit"]:hover {
                background-color: #d4af37; /* Gold */
                transform: translateY(-2px);
                box-shadow: 0 4px 8px rgba(0,0,0,0.15);
                color: #0a2540;
            }
            
            .user-info {
                background-color: #f8f9fa;
                padding: 20px;
                border-radius: 6px;
                margin: 20px 0;
                text-align: left;
                border-left: 4px solid #d4af37;
            }
            
            .info-label {
                font-weight: 600;
                color: #0a2540;
                display: inline-block;
                width: 150px;
            }
            
            p {
                margin: 15px 0;
            }
        </style>
    </head>
    <body>
        <form>
            <h1>Employee Dashboard</h1>
            <hr>
            
            <div class="welcome-message">
                Welcome to the Employee Management System
            </div>
            
            <h2>Hello, <%= session.getAttribute("employeeName") %> <%= session.getAttribute("employeeSurname") %>!</h2>
            
            <div class="user-info">
                <p><span class="info-label">Employee ID:</span> <%= session.getAttribute("employeeId") %></p>
                <p><span class="info-label">Role:</span> <%= session.getAttribute("employeeRole") %></p>
            </div>
            
            <p><a href="desktop-app-launcher.jsp">Launch Desktop Application</a></p>
            
            <form action="LogoutServlet" method="POST">
                <input type="submit" value="Logout">
            </form>
        </form>
    </body>
</html>