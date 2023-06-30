SELECT p.FirstName, COUNT(soh.SalesOrderID) AS OrderCount
FROM Person as p
JOIN Customer as c ON p.BusinessEntityID = c.CustomerID
JOIN SalesOrderHeader as soh ON c.CustomerID = soh.CustomerID
GROUP BY p.FirstName;
