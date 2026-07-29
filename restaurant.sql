CREATE TABLE IF NOT EXISTS RESTAURANT(
name TEXT,
neighbourhood TEXT,
cuisine TEXT,
review REAL,
price TEXT,
health TEXT);

INSERT INTO RESTAURANT(name,neighbourhood,cuisine,review,price,health) VALUES
('Peter','Brooklyn','Steak',4.4,'$$$$','A'),
('Jongro','Midtown','Korean',3.5,'$$','A'),
('Pocha','Midtown','Pizza',4.0,'$$$','B'),
('Lighthouse','Queens','Chinese',3.9,'$','A'),
('Minca','Downtown','American',4.6,'$$$',''),
('Marea','Chinatown','Chinese',3.0,'$$',''),
('Dirty Candy','Uptown','Italian',4.9,'$$$$','B'),
('Di Fara Candy','Brooklyn','Pizza',3.8,'$$','A'),
('Golden Unicorn','Uptown','Italian',2.8,'$$','A');

SELECT DISTINCT neighbourhood
FROM RESTAURANT;

SELECT DISTINCT cuisine
FROM RESTAURANT;

SELECT * 
FROM RESTAURANT
WHERE cuisine = 'Chinese';

SELECT *
FROM RESTAURANT
WHERE review >= 4.0;

SELECT *
FROM RESTAURANT
WHERE cuisine = 'Italian'
AND price IN ('$$','$$$');

SELECT * 
FROM RESTAURANT 
WHERE price == '$$$';

SELECT *
FROM RESTAURANT
WHERE name LIKE '%Candy%';

SELECT * 
FROM RESTAURANT
WHERE neighbourhood IN ('Midtown','Downtown','Chinatown');

SELECT *
FROM RESTAURANT
WHERE health = '' OR health ISNULL;

SELECT *
FROM RESTAURANT
ORDER BY review DESC
LIMIT 4;

