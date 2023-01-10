/*create table if not exists students(
		id serial primary key,
 		first_name varchar (50) NOT NULL,
		last_name varchar (50) NOT NULL,
 		birth_date date NOT NULL);*/
		
/*insert into students(first_name,last_name,birth_date)
values('Marc','Benichou','02/11/1998'),
	  ('Yoan','Cohen','03/12/2010'),
	  ('Lea','Benichou','27/07/1987'),
	  ('Amelia','Dux','07/04/1996'),
	  ('David','Grez','14/06/2003'),
	  ('Omer','Simpson','03/10/1980'),
	  ('W Mohamed','TAPSOBA','28/06/2000');*/

-- 3-1

--select first_name, last_name from students where id = 6--

-- 3-2
--select first_name, last_name from students where first_name = 'Marc' AND last_name = 'Benichou'--

-- 3-4

--select first_name, last_name from students where first_name = 'Marc' OR last_name = 'Benichou'--

-- 3-4

--select first_name, last_name from students where first_name like '%a%'--

-- 3-5

--select first_name, last_name from students where first_name like 'a%'--


--select first_name, last_name from students where first_name like 'A%'--

-- 3-6

--select first_name, last_name from students where first_name like '%a'--

-- 3-7

--select first_name, last_name from students where first_name like '%a_'--

-- 3-8

--select first_name, last_name from students where id = 1 OR id = 2--

-- 4

--select * from students where birth_date >= '01/01/2000'--