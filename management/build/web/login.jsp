<%-- 
    Document   : login
    Created on : 30 May 2025, 15:32:55
    Author     : Moreb
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Employee Login</title>
        <style>
            /* Consistent Navy and Gold Professional Theme */
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
            
            form {
                width: 500px;
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
            
            .form-group {
                margin-bottom: 20px;
                text-align: left;
            }
            
            .form-label {
                color: #0a2540;
                font-weight: 500;
                display: block;
                margin-bottom: 8px;
            }
            
            input[type="text"],
            input[type="password"] {
                width: 100%;
                padding: 12px;
                margin: 8px 0;
                border: 1px solid #ced4da;
                border-radius: 6px;
                transition: border-color 0.3s;
                font-size: 16px;
            }
            
            input[type="text"]:focus,
            input[type="password"]:focus {
                border-color: #d4af37; /* Gold */
                outline: none;
                box-shadow: 0 0 0 3px rgba(212, 175, 55, 0.2);
            }
            
            input[type="submit"] {
                background-color: #0a2540; /* Navy blue */
                color: white;
                border: none;
                padding: 14px 28px;
                border-radius: 6px;
                cursor: pointer;
                font-size: 18px;
                font-weight: 500;
                transition: all 0.3s;
                width: auto;
                margin: 20px auto;
                display: block;
            }
            
            input[type="submit"]:hover {
                background-color: #d4af37; /* Gold */
                transform: translateY(-2px);
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            
            .error-message {
                color: #dc3545;
                text-align: center;
                margin-bottom: 20px;
                font-weight: 500;
            }
            
            .success-message {
                color: #28a745;
                text-align: center;
                margin-bottom: 20px;
                font-weight: 500;
            }
            
            .register-link {
                color: #0a2540;
                text-decoration: none;
                font-weight: 500;
                transition: color 0.3s;
            }
            
            .register-link:hover {
                color: #d4af37;
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <h1>Employee Login</h1>
        
        <% if (request.getAttribute("error") != null) { %>
            <div class="error-message"><%= request.getAttribute("error") %></div>
        <% } %>
        
        <% if (request.getAttribute("success") != null) { %>
            <div class="success-message"><%= request.getAttribute("success") %></div>
        <% } %>
        
        <form action="LoginServlet" method="POST">
            <div class="form-group">
                <label class="form-label">Employee ID:</label>
                <input type="text" name="txtEmployeeID" required>
            </div>
            
            <div class="form-group">
                <label class="form-label">Password:</label>
                <input type="password" name="txtPassword" required>
            </div>
            
            <input type="submit" value="Login">
            
            <hr>
            
            <p>Don't have an account? <a class="register-link" href="register.jsp">Register here</a></p>
        </form>
    </body>
</html>