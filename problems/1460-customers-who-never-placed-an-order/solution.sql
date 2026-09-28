-- your query
SELECT c.customer_id ,c.name 
from customers as c 
left join orders as o 
on o.customer_id = c.customer_id
where o.customer_id is null
order by c.customer_id asc
