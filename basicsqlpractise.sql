-- Select product_name, price from products

-- Select product_name, price 
-- from products
-- where price > 50;

-- Select product_name, price 
-- from products
-- where price  between 20 and 40;


-- Select customer_name, city
-- from customers
-- where customer_name like 'A%';


-- Select customer_name, city,country
-- from customers
-- where country='Germany' or country ='France'
-- order by customer_name DESC;

-- Select product_name, price
-- from products
-- where price >= 20 and price <=50
-- order by price desc;

-- Select customer_name, city,country
-- from customers
-- where country = 'UK' and city ='London';

-- Select product_name,price
-- from products
-- where product_name like '%Chocolate%'
-- order by price asc;

-- Select customer_name, city,country
-- from customers
-- where country <> 'Germany' and city IS NOT NULL
-- order by country ASC, Customer_name ASC;


-- select product_name, price, category_id
-- from products
-- where price < 30 or category_id = 1
-- order by price asc
-- limit 10;

-- Display order_id, customer_id, and order_date for orders placed from 2022-01-01 through 2022-03-31, inclusive.
-- Sort the newest orders first and show only the first 15 rows.
select order_id, customer_id, order_date
from orders
where order_date between '2022-01-01' and '2022-03-31'
order by order_date DESC
limit 15;





















