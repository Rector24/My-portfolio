-- Question 1:
SELECT 
    e.BusinessEntityID,
    e.NationalIDNumber,
    p.FirstName,
    p.LastName,
    (SELECT d.Name 
     FROM HumanResources.EmployeeDepartmentHistory edh 
     INNER JOIN HumanResources.Department d ON edh.DepartmentID = d.DepartmentID 
     WHERE edh.BusinessEntityID = e.BusinessEntityID AND edh.EndDate IS NULL) AS DepartmentName,
    e.JobTitle
FROM 
    HumanResources.Employee e
INNER JOIN 
    Person.Person p ON e.BusinessEntityID = p.BusinessEntityID
WHERE 
    e.OrganizationLevel = 1 
ORDER BY 
    e.BusinessEntityID;

-- Question 2:
SELECT v.AccountNumber, v.Name, v.CreditRating
FROM Purchasing.Vendor AS v
WHERE v.BusinessEntityID NOT IN (SELECT DISTINCT pv.BusinessEntityID FROM Purchasing.ProductVendor AS pv)
ORDER BY v.Name;

-- Question 3:
SELECT sm.ShipMethodID, 
       sm.Name, 
       ROUND(SUM(soh.TotalDue), 2) AS SalesOrdersTotal, 
       ROUND(SUM(poh.TotalDue), 2) AS PurchaseOrdersTotal
FROM Purchasing.ShipMethod AS sm
LEFT JOIN Sales.SalesOrderHeader AS soh ON sm.ShipMethodID = soh.ShipMethodID
LEFT JOIN Purchasing.PurchaseOrderHeader AS poh ON sm.ShipMethodID = poh.ShipMethodID
GROUP BY sm.ShipMethodID, sm.Name;

-- Question 4:
SELECT p.ProductNumber, 
       p.Name AS ProductName, 
       ps.Name AS SubCategory, 
       CASE p.Class 
            WHEN 'H' THEN 'High'
            WHEN 'M' THEN 'Medium'
            WHEN 'L' THEN 'Low'
            ELSE 'Other'
       END AS Class
FROM Production.Product AS p
LEFT JOIN Production.ProductSubcategory AS ps ON p.ProductSubcategoryID = ps.ProductSubcategoryID
WHERE p.MakeFlag = 1 
  AND p.SellEndDate IS NULL; 





