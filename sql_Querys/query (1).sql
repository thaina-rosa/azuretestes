select SalesOrderID, OrderDate, TotalDue from SalesOrderHeader
where YEAR(OrderDate) = 2011 and MONTH(OrderDate) = 9 and TotalDue > 1000 
order by TotalDue desc;