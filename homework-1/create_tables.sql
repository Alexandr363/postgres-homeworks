-- SQL-команды для создания таблиц
CREATE DATABASE north;

CREATE TABLE customers   -- клиент
(
    customer_id varchar(30) PRIMARY KEY,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50) NOT NULL
);

CREATE TABLE employees   -- сотрудник
(
    employee_id int2 PRIMARY KEY,
	first_name varchar(30) NOT NULL,
	last_name varchar(30) NOT NULL,
	title varchar(30) NOT NULL,
	birth_date date NOT NULL,
	notes text NOT NULL
);

CREATE TABLE orders    -- заказ
(
    order_id int2 PRIMARY KEY,
	cusmomer_id varchar(10) REFERENCES customers(customer_id),
	employee_id int2 REFERENCES employees(employee_id),
	order_date date NOT NULL,
	ship_sity varchar(20) NOT NULL
);
