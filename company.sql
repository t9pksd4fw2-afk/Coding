CREATE TABLE IF NOT EXISTS COMPANY(
name TEXT,
product TEXT,
price REAL,
country TEXT);

INSERT INTO COMPANY VALUES
('Alex','Tablet',500,'England'),
('Tim','Phone',1000,'Spain'),
('Bjorn','Laptop',900,'England'),
('Anthony','Tablet',500,'France'),
('Tom','Phone',1000,'India'),
('Theo','Earbuds',100,'Italy'),
('Bill','Tablet',500,'France'),
('Brent','Phone',1000,'Germany');

SELECT * FROM COMPANY;

SELECT name FROM COMPANY WHERE name LIKE 'A%';

SELECT name FROM COMPANY WHERE name LIKE '%or%';

SELECT COUNT(name) AS 'TOTAL PEOPLE' FROM COMPANY;

SELECT AVG(price) AS 'AVG PRICE' FROM COMPANY;

SELECT DISTINCT * FROM COMPANY ORDER BY price DESC LIMIT 3;

SELECT DISTINCT * FROM COMPANY ORDER BY price ASC LIMIT 3;

SELECT MAX(price) AS 'MOST EXPENSIVE' FROM COMPANY;

SELECT MIN(price) AS 'CHEAPEST' FROM COMPANY;

SELECT * FROM COMPANY WHERE product = 'Phone';

