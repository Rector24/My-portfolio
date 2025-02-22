CREATE PROCEDURE RegisterMember 
    @Name VARCHAR(100), 
    @Email VARCHAR(100), 
    @Phone VARCHAR(15), 
    @MembershipType VARCHAR(50)
AS
BEGIN
    INSERT INTO Members (Name, Email, Phone, MembershipType) 
    VALUES (@Name, @Email, @Phone, @MembershipType);

END;
GO