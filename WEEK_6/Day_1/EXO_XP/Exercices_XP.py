CREATE TABLE if not exists items (
	id_item serial primary key,
	nom_item varchar (50) NOT NULL,
	prix_item smallint NOT NULL 

	);


CREATE TABLE if not exists customers(
	id_customer serial primary key,
	prenom_customer  varchar (50) NOT NULL,
	nom_customer varchar (50) NOT NULL

	);



insert into items (nom_item,prix_item)
values ('Small Desk',100),('Large Desk',300),('Fan',80);

insert into customers (prenom_customer,nom_customer)
values ('Greg','Jones'),('Sandra','Jones'),('Scott','Scott'),('Trevor','Vert'),('Mélanie','Johnson');

#All the items.

select * from items

#All the items with a price above 80 (80 not included).

select * from items where prix_item > 80

#All the items with a price below 300. (300 included)

select * from items where prix_item <= 300

#All customers whose last name is ‘Smith’ (What will be your outcome?).

select * from customers where nom_customer = 'Smith'

#All customers whose last name is ‘Jones’.

select * from customers where nom_customer = 'Jones'

#All customers whose firstname is not ‘Scott’

select * from customers where nom_customer != 'Scott'