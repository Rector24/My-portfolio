CREATE TABLE Members (
    MemberID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(15),
    MembershipType VARCHAR(50) NOT NULL
);
GO

CREATE TABLE Trainers (
    TrainerID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Specialty VARCHAR(50),
    ContactInfo VARCHAR(100)
);
GO

CREATE TABLE Classes (
    ClassID INT PRIMARY KEY,
    ClassName VARCHAR(50) NOT NULL,
    Schedule DATETIME NOT NULL,
    TrainerID INT,
    MaxCapacity INT,
    FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID)
);
GO

CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY,
    MemberID INT,
    Date DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentMethod VARCHAR(50),
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
);
GO

CREATE TABLE Feedback (
    FeedbackID INT PRIMARY KEY,
    MemberID INT,
    FeedbackText TEXT NOT NULL,
    Rating INT CHECK (Rating >= 1 AND Rating <= 5),
    FeedbackDate DATE NOT NULL,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
);
GO

CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY,
    MemberID INT,
    ClassID INT,
    BookingDate DATE NOT NULL,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID),
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID)
);
GO

CREATE TABLE Equipment (
    EquipmentID INT PRIMARY KEY,
    EquipmentName VARCHAR(100) NOT NULL,
    PurchaseDate DATE,
    Condition VARCHAR(50)
);
GO

CREATE TABLE Inventory (
    ItemID INT PRIMARY KEY,
    ItemName VARCHAR(100) NOT NULL,
    Quantity INT NOT NULL,
    PurchaseDate DATE NOT NULL,
    SupplierName VARCHAR(100)
);
GO