CREATE VIEW Macy.OrderDetails AS
SELECT O.OrderID, C.Name AS CustomerName, M.ItemName, OI.Quantity
FROM Macy.Orders O
JOIN Macy.Customers C ON O.CustomerID = C.CustomerID
JOIN Macy.OrderItems OI ON O.OrderID = OI.OrderID
JOIN Macy.Menu M ON OI.ItemID = M.ItemID;
GO