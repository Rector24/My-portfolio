INSERT INTO Macy.Users (Username, Password, Role) VALUES ('admin', 'admin123', 'Management');
INSERT INTO Macy.Customers (Name, Phone, Email) VALUES ('John Doe', '1234567890', 'john@example.com');
INSERT INTO Macy.Menu (ItemName, Price) VALUES ('Pepperoni Pizza', 10.99);
INSERT INTO Macy.Orders (CustomerID, OrderDate) VALUES (1, GETDATE());
INSERT INTO Macy.OrderItems (OrderID, ItemID, Quantity) VALUES (1, 1, 2);