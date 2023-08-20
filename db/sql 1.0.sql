create database affandb
use affandb

create table customer(
id int not null,
Cname varchar(30),
desgination varchar(30),
salary int,
primary key(id)
),
Alter table customer
Add Email varchar(30)
Alter table customer
drop Column Email 


SELECT * FROM customer
WHERE Cname LIKE '____';
create table Orders(
Oid int,
Oname varchar(20),
primary key(Oid),
foreign key(Oid) references customer(id)
)

drop table Orders


insert  into customer value(1,'affan','software enginner',12000)
insert  into customer value(5,'affan','software enginner',12000,'hello@gmail.com')
insert  into customer value(2,'amir','dev',20000)
insert  into customer value(6,'asif','dev',20000)
insert  into customer value(3,'ali','software enginner',15000)
insert  into customer value(4,'ali','software enginner',15000)
drop table customer
select distinct * from customer
select * from customer
--order
insert  into Orders value(1,'burger'),
insert  into Orders value(2,'piza'),
insert  into Orders value(3,'sandwich')
select * from customer where salary between 10000 and 15000