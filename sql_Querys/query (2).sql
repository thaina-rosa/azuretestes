SELECT soh.OrderDate,sod.ProductID, sum(sod.OrderQty) as TotalQuantity
from SalesOrderHeader as soh
join SalesOrderDetail as sod 
on soh.SalesOrderID = sod.SalesOrderID
join Product as p 
on sod.ProductID = p.ProductID
group by sod.ProductID, soh.OrderDate;




