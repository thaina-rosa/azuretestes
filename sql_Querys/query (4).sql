SELECT p.Name AS ProductName, p.DaysToManufacture, SUM(od.OrderQty) AS TotalQuantity
FROM SalesOrderDetail as od
JOIN SpecialOfferProduct as sop ON od.ProductID = sop.ProductID
JOIN Product as p ON sop.ProductID = p.ProductID
GROUP BY p.Name, p.DaysToManufacture
ORDER BY SUM(od.OrderQty) DESC
  
