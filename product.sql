CREATE TABLE IF NOT EXISTS PROD(
productid TEXT PRIMARY KEY,
productname TEXT,
category TEXT,
price REAL,
stock INTEGER);

INSERT INTO PROD VALUES
('5001','Phone','Electronic',1000.99,100),
('5002','Tablet','Electronic',550.99,25),
('5003','Laptop','Electronic',999.99,75),
('5004','Airfryer','Cooking',100.99,50),
('5005','Laptop','Electronic',999.99,1),
('5006','Harry Potter','Books',10.99,5);

SELECT * FROM PROD;

SELECT price,productname FROM PROD;

SELECT * FROM PROD WHERE price > 900;

SELECT * FROM PROD where category = 'Electronic' or category = 'Books';

SELECT * FROM PROD where productname LIKE 'L%';

SELECT * FROM PROD where price >= 500 and price <= 2000;

SELECT * FROM PROD ORDER BY price DESC;

SELECT COUNT(*), AVG(price), MAX(price),MIN(price) FROM PROD;

SELECT SUM(stock) FROM PROD;

SELECT AVG(price) FROM PROD GROUP BY category;

SELECT * FROM PROD GROUP BY category HAVING stock >1;

DROP TABLE PROD;


