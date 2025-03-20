CREATE TABLE Subjects (
    UserID INT,
    Subject VARCHAR(50),
    Result INT,
    PRIMARY KEY (UserID, Subject),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);