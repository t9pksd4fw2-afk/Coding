CREATE TABLE employees(
	employee_id TEXT PRIMARY KEY,
	name TEXT,
	city TEXT,
	salary REAL
);

INSERT INTO employees ( employee_id,name,city,salary) VALUES
('1453','James Hoog','New York',34000),
('6859','Nail Knite','Paris',100000),
('2231','Pit Alex','London',20000),
('7969','Mc Lyon','Paris',40000),
('3433','Paul Adam','Rome',31000),
('6894','Lauson Hen','San Jose',50000);

SELECT * FROM employees;
SELECT * FROM employees WHERE employee_id == '3433'

