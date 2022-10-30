select c.name, c.city, sum(o.amount) as totalSum
from customers c
join orders o on o.customer_id = c.id 
where o.amount between 100 and 3500 
group by c.name, c.city
order by c.city

---------------------------------
insert into customers (id, name, city, grade, salesperson_id)
values(3006, 'Stefan Huk', 'Kyiv', 500, 5007);

select * from customers
where city in ('London', 'Kyiv')
order by id;

---------------------------------
select o.order_num, o.amount, c.name
from orders o 
join customers c on o.customer_id = c.id
where o.amount between 500 and 2000
order by o.amount

---------------------------------

select name, city, grade
from customers
where city in ('London', 'Paris')
order by name

---------------------------------
update customers
set city = 'Paris', grade = '300'
where name = 'Jozy Altidore';

select name, city, grade
from customers
where city in ('London', 'Paris')
order by id;
