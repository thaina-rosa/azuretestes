select distinct
SalesOrderID 
from SalesOrderDetail
group by SalesOrderID 
having COUNT(SalesOrderID )=3