CREATE TABLE IF NOT EXISTS BOOK(
book_id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
genre TEXT NOT NULL,
rating REAL NOT NULL,
pages INTEGER NOT NULL,
pub_year INTEGER NOT NULL);

INSERT INTO BOOK VALUES(1,'Dragon Quest', 'Fantasy',9.2,312,2021);
INSERT INTO BOOK VALUES(2,'Code Wizards', 'Fantasy',8.5,200,2020); 
INSERT INTO BOOK VALUES(3,'Ocean Deep', 'Fantasy',7.8,195,2022);
INSERT INTO BOOK VALUES(4,'Star Rangers', 'Fantasy',9.5,340,2019);
INSERT INTO BOOK VALUES(5,'Forest Secrets', 'Fantasy',8.1,228,2023);
INSERT INTO BOOK VALUES(6,'Robot City', 'Fantasy',7.2,260,2021);
INSERT INTO BOOK VALUES(7,'Time Jumpers', 'Fantasy',8.9,175,2022);
INSERT INTO BOOK VALUES(8,'Magic Academy', 'Fantasy',9.0,398,2020);

SELECT * FROM BOOK;

SELECT title, rating FROM BOOK ORDER BY rating ASC;

SELECT title, rating FROM BOOK ORDER BY rating DESC;

SELECT title, genre, rating FROM BOOK ORDER BY genre ASC,rating desc;

SELECT title, rating FROM BOOK ORDER BY rating DESC LIMIT 3;

SELECT title,pub_year FROM BOOK ORDER BY pub_year asc limit 5;

SELECT genre, COUNT(*) AS book_count  FROM BOOK GROUP BY genre;

SELECT genre, SUM(pages) AS total_pages, AVG(rating)
FROM BOOK
GROUP BY genre;

SELECT genre, COUNT(*) AS book_count
FROM BOOK
GROUP BY genre
HAVING COUNT(*) > 2;

SELECT genre, AVG(rating) AS avg_rating
FROM BOOK
GROUP BY genre
HAVING AVG(rating) >= 8.5;

