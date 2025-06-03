<%-- 
    Document   : register
    Created on : 30 May 2025, 15:34:14
    Author     : Moreb
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Employee Registration</title>
        <style>
            /* Navy and Gold Professional Theme */
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
            
            h3 { 
                color: #6c757d; /* Medium gray */
                margin-bottom: 30px;
                font-weight: 400;
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
            
            table {
                width: 100%;
                margin: 20px 0;
                border-collapse: collapse;
            }
            
            td {
                padding: 12px 0;
                vertical-align: middle;
                text-align: left;
            }
            
            td:first-child {
                width: 40%;
                font-weight: 500;
                color: #0a2540;
            }
            
            input[type="text"],
            input[type="password"],
            input[type="email"] {
                width: 100%;
                padding: 12px;
                margin: 8px 0;
                border: 1px solid #ced4da;
                border-radius: 6px;
                transition: border-color 0.3s;
                font-size: 16px;
                box-sizing: border-box;
            }
            
            input[type="text"]:focus,
            input[type="password"]:focus,
            input[type="email"]:focus {
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
                margin: 20px auto 0;
                display: block;
            }
            
            input[type="submit"]:hover {
                background-color: #d4af37; /* Gold */
                transform: translateY(-2px);
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                color: #0a2540;
            }
            
            .error-message {
                color: #dc3545;
                text-align: center;
                margin-bottom: 20px;
                font-weight: 500;
            }
            
            .login-link {
                margin-top: 20px;
                color: #6c757d;
            }
            
            .login-link a {
                color: #0a2540;
                text-decoration: none;
                font-weight: 500;
                transition: color 0.3s;
            }
            
            .login-link a:hover {
                color: #d4af37;
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <% if (request.getAttribute("error") != null) { %>
            <div class="error-message"><%= request.getAttribute("error") %></div>
        <% } %>
        
        <form action="RegisterServlet" method="POST">
            <h1>Employee Registration</h1>
            <h3>Please complete all fields</h3>
            
            <hr>
            
            <table>
                <tbody>
                    <tr>
                        <td>Employee ID:</td>
                        <td><input type="text" name="txtEmployeeID" required></td>
                    </tr>
                    <tr>
                        <td>Name:</td>
                        <td><input type="text" name="txtName" required></td>
                    </tr>
                    <tr>
                        <td>Surname:</td>
                        <td><input type="text" name="txtSurname" required></td>
                    </tr>
                    <tr>
                        <td>Department:</td>
                        <td><input type="text" name="txtDepartment" required></td>
                    </tr>
                    <tr>
                        <td>Role:</td>
                        <td><input type="text" name="txtRole" required></td>
                    </tr>
                    <tr>
                        <td>Phone Number:</td>
                        <td><input type="text" name="txtPhoneNumber" required></td>
                    </tr>
                    <tr>
                        <td>Email:</td>
                        <td><input type="email" name="txtEmail" required></td>
                    </tr>
                    <tr>
                        <td>Password:</td>
                        <td><input type="password" name="txtPassword" required minlength="8"></td>
                    </tr>
                    <tr>
                        <td>Confirm Password:</td>
                        <td><input type="password" name="txtConfirmPassword" required minlength="8"></td>
                    </tr>
                </tbody>
            </table>
            
            <input type="submit" value="Register">
            
            <div class="login-link">
                Already have an account? <a href="login.jsp">Login here</a>
            </div>
        </form>
    </body>
</html>