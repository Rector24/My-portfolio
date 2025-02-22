CREATE VIEW PaymentSummary AS
SELECT MemberID, SUM(Amount) AS TotalPayments
FROM Payments
GROUP BY MemberID;
GO