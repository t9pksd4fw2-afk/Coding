CREATE TABLE IF NOT EXISTS BOOKS(
bookid TEXT PRIMARY KEY,
title TEXT,
author TEXT,
genre TEXT,
price REAL,
year INTEGER,
stock INTEGER);

INSERT INTO BOOKS VALUES
('3422','Harry Potter','JK Rowling','Fantasy',10.99,2012,10),
('3421','Hamlet','William Shakespeare','Thriller',9.99,1820,20),
('3420','Tale of Two Cities','Charles Dickens','Suspense',15.99,1901,10),
('3423','Christmas Carol','Charles Dickens','Allegory',10.99,1899,10),
('3425','Oliver Twist','Charles Dickens','Victorian',13.99,1910,3),
('3426','Inspector Calls','J.B Priestley','Mystery',5.99,1945,8.99),
('3427','Percy Jackson','Rick Riordan','Mythology',13.99,2011,2);

SELECT * FROM BOOKS;

SELECT * FROM BOOKS WHERE price > 10 and stock >= 10;

SELECT * FROM BOOKS WHERE genre = 'Fantasy' or genre = 'Fiction';

SELECT * FROM BOOKS WHERE title LIKE 'Ha%';

SELECT * FROM BOOKS WHERE title LIKE
'%s';

SELECT * FROM BOOKS WHERE title LIKE
'_a%';

SELECT * FROM BOOKS WHERE year < 2000;

SELECT * FROM BOOKS WHERE stock != 10;

SELECT COUNT(bookid) AS 'TOTAL BOOKS' FROM BOOKS;

SELECT MAX(price) AS 'MOST EXPENSIVE' FROM BOOKS;

SELECT MIN(price) AS 'CHEAPEST' FROM BOOKS;

SELECT COUNT(*),genre FROM BOOKS GROUP BY genre;

SELECT AVG(price),genre FROM BOOKS GROUP BY genre HAVING AVG(price) > 10;

SELECT * FROM BOOKS ORDER BY price DESC;
SELECT * FROM BOOKS ORDER BY price DESC LIMIT 3;