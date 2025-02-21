CREATE TABLE Macy.Users (
    UserID INT PRIMARY KEY IDENTITY(1,1),
    Username NVARCHAR(50) NOT NULL,
    Password NVARCHAR(50) NOT NULL,
    Role NVARCHAR(50) NOT NULL -- Management or Staff
);
GO
CREATE TABLE Macy.Customers (
    CustomerID INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(100) NOT NULL,
    Phone NVARCHAR(15),
    Email NVARCHAR(100)
) ON SecondaryFG;
GO
CREATE TABLE Macy.Menu (
    ItemID INT PRIMARY KEY IDENTITY(1,1),
    ItemName NVARCHAR(100) NOT NULL,
    Price DECIMAL(10,2) NOT NULL
) ON SecondaryFG;
GO
CREATE TABLE Macy.Orders (
    OrderID INT PRIMARY KEY IDENTITY(1,1),
    CustomerID INT FOREIGN KEY REFERENCES Macy.Customers(CustomerID),
    OrderDate DATETIME NOT NULL
) ON SecondaryFG;
GO

CREATE TABLE Macy.OrderItems (
    OrderItemID INT PRIMARY KEY IDENTITY(1,1),
    OrderID INT FOREIGN KEY REFERENCES Macy.Orders(OrderID),
    ItemID INT FOREIGN KEY REFERENCES Macy.Menu(ItemID),
    Quantity INT NOT NULL
) ON SecondaryFG;
GO


