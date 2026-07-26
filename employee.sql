CREATE TABLE IF NOT EXISTS EMP(
salesman_id TEXT PRIMARY KEY,
name TEXT,
city TEXT,
salary INTEGER);


INSERT INTO EMP(salesman_id,name,city,salary) VALUES
('5001','James Hong','New York',50000),
('5002','Neil Knite','Paris',20000),
('5005','Pit Alex','London',30000),
('5006','Mc Lyon','Paris',25000),
('5007','Paul Adams','',10000),
('5003','Lauson Hen','San Jose',43000),
('5009','James Hen','San Jose',45000);

SELECT COUNT(salesman_id) FROM EMP;
SELECT COUNT(city) FROM EMP WHERE city = 'Paris';
SELECT salary FROM EMP ORDER BY salary ASC limit 3;
SELECT salary FROM EMP ORDER BY salary DESC limit 3;
SELECT DISTINCT salesman_id FROM EMP;
SELECT name FROM EMP WHERE name LIKE '%a%';
SELECT * FROM EMP WHERE city = 'New York';
SELECT * FROM EMP WHERE city = '';
SELECT AVG(salary) FROM EMP;
SELECT MIN(salary) FROM EMP;
SELECT MAX(salary) FROM EMP;
SELECT SUM(salary) FROM EMP;