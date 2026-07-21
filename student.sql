CREATE TABLE IF NOT EXISTS STUDENT(
student_id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INTEGER NOT NULL,
gender TEXT NOT NULL,
subjects TEXT NOT NULL,
marks INTEGER NOT NULL,
city TEXT NOT NULL);

INSERT INTO STUDENT(student_id,name,age,gender,subjects,marks,city) VALUES
(343423,'Tom',20,'Male','Maths',85,'London'),
(343422,'Ben',21,'Male','English',75,'Manchester'),
(343421,'Melissa',18,'Female','Maths',89,'London'),
(343425,'Jeff',19,'Male','Physics',78,'London'),
(343426,'Smith',18,'Male','Physics',82,'London'),
(343427,'Vandana',17,'Female','Art',78,'Mumbai'),
(343428,'Ryan',20,'Male','Computer Sci',94,'Melbourne'),
(343429,'Chris',22,'Male','D.T',65,'Rome'),
(343420,'Tim',21,'Male','Chemistry',99,'Paris'),
(343432,'Sydney',23,'Female','Biology',84,'Paris');

SELECT * FROM STUDENT;

SELECT COUNT(*) FROM STUDENT;

SELECT * FROM STUDENT ORDER BY marks DESC;

SELECT * FROM STUDENT WHERE subjects = 'Maths' and marks > 80;

SELECT * FROM STUDENT WHERE city = 'Paris' or city = 'London' or city = 'Mumbai';

SELECT * FROM STUDENT WHERE name LIKE '%a';

SELECT DISTINCT subjects FROM STUDENT;


