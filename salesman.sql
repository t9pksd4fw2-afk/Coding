CREATE TABLE IF NOT EXISTS SALE(
salesman_id TEXT PRIMARY KEY,
name TEXT,
city TEXT,
comission TEXT);

INSERT INTO SALE(salesman_id,name,city,comission) VALUES
('5001','James Hong','New York','0.15'),
('5002','Neil Knite','Paris','0.13'),
('5005','Pit Alex','London','0.14'),
('5006','Mc Lyon','Paris','0.12'),
('5007','Paul Adams','Rome','0.11'),
('5003','Lauson Hen','San Jose','0.16');

CREATE TABLE IF NOT EXISTS CUSTOMER(
customer_id TEXT,
cust_name TEXT PRIMARY KEY,
city TEXT,
grade TEXT,
salesman_id TEXT);

INSERT INTO CUSTOMER(customer_id,cust_name,city,grade,salesman_id) VALUES
('1002','Nick Risando','New York','100','5001'),
('1002','Brad Davis','New York','200','5002'),
('1002','Graham Zusi','California','200','5005'),
('1002','Julian Green','London','300','5006'),
('1002','Fabian Johnson','Paris','100','5007'),
('1002','Brad Guran','Berlin','200','5003'),
('1002','Jozy Altidor','Moscow','300','5002'),
('1002','Geoff Cameron','London','','5005');

CREATE TABLE IF NOT EXISTS ORDE(
ord_no TEXT PRIMARY KEY,
purch_amt TEXT,
ord_date TEXT,
customer_id TEXT,
salesman_id TEXT);

INSERT INTO ORDE(ord_no,purch_amt,ord_date,customer_id,salesman_id) VALUES
('700001','150.5','2012-10-05','3005','5002'),
('700009','270.65','2012-09-10','3001','5001'),
('700002','65.26','2012-10-05','3002','5003'),
('700004','110.5','2012-08-17','3004','5007'),
('700007','948.6','2012-09-10','3003','5005'),
('700005','2400.6','2012-07-27','3007','5006');

SELECT CUSTOMER.cust_name, SALE.name, SALE.city
FROM CUSTOMER
JOIN SALE ON CUSTOMER.city = SALE.city;

SELECT CUSTOMER.cust_name, SALE.name, SALE.city
FROM CUSTOMER
JOIN SALE ON CUSTOMER.salesman_id = SALE.salesman_id;

SELECT ORDE.ord_no, CUSTOMER.cust_name, ORDE.customer_id, ORDE.salesman_id
FROM ORDE
JOIN CUSTOMER ON ORDE.customer_id = CUSTOMER.customer_id
JOIN SALE ON ORDE.salesman_id = CUSTOMER.salesman_id
WHERE CUSTOMER.city <> SALE.city;

SELECT ORDE.ord_no, CUSTOMER.cust_name
FROM ORDE
JOIN CUSTOMER ON ORDE.customer_id = CUSTOMER.customer_id;

SELECT CUSTOMER.cust_name AS 'Customer', CUSTOMER.grade AS 'Grade'
FROM ORDE
JOIN SALE ON ORDE.salesman_id = SALE.salesman_id
JOIN CUSTOMER ON ORDE.customer_id = CUSTOMER.customer_id
WHERE CUSTOMER.grade IS NOT NULL;

SELECT CUSTOMER.cust_name AS 'Customer',
CUSTOMER.city AS 'City',
SALE.name AS 'Salesman',
SALE.comission
FROM CUSTOMER
JOIN SALE ON CUSTOMER.salesman_id = SALE.salesman_id
WHERE SALE.comission BETWEEN 0.12 AND 0.14;

SELECT ORDE.ord_no, CUSTOMER.cust_name, SALE.comission AS 'Comission%',
ORDE.purch_amt * SALE.comission AS 'Comission'
FROM ORDE
JOIN SALE ON ORDE.salesman_id = SALE.salesman_id
JOIN CUSTOMER ON ORDE.customer_id = CUSTOMER.customer_id
WHERE CUSTOMER.grade >= 200;

SELECT *
FROM CUSTOMER
JOIN ORDE ON CUSTOMER.customer_id = ORDE.customer_id
WHERE ORDE.ord_date = '2012-10-05';





