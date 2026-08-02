import sqlite3
import pandas as pd
conn = sqlite3.connect('college.db')
cursor = conn.cursor()

cursor.executescript("""DROP TABLE IF EXISTS Department;
DROP TABLE IF EXISTS Faculty;
DROP TABLE IF EXISTS Student;""")

cursor.execute("""CREATE TABLE Department (DeptID INTEGER PRIMARY KEY,
DeptName TEXT,
Building TEXT)""")

cursor.execute("""CREATE TABLE Faculty (FacultyID INTEGER PRIMARY KEY,
FacultyName TEXT,
Subject TEXT,
Salary INTEGER,
DeptID INTEGER)""")

cursor.execute("""CREATE TABLE Student (StudentID INTEGER PRIMARY KEY,
StudentName TEXT,
City TEXT,
Age INTEGER,
Marks INTEGER,
DeptID INTEGER)""")

cursor.executescript("""INSERT INTO Department VALUES
(101,'Computer Science','Block A'),
(102,'French','Block B'),
(103,'Science','Block C');
INSERT INTO Faculty VALUES
(1,'Anita Sharma','Python',70000,101),
(2,'Rahul Verma','Java',65000,101),
(3,'Priya Sharma','Digital Electronics',68000,102),
(4,'Vikram Patel','Thermodynamics',75000,103),
(5,'Neha Gupta','DBMS',75000,101);

INSERT INTO Student VALUES
(201,'Aarav',20,'Dehli',88,101),
(202,'Diya',19,'Mumbai',91,102),
(203,'Kabir',21,'Dehli',75,101),
(204,'Meera',20,'Pune',95,103),
(205,'Rohan',22,'Chennai',68,102),
(206,'Ananya',20,'Dehli',84,101),
(207,'Ishaan',19,'Mumbai',79,103);
""")
conn.commit()

print('\n All Students')
dept = pd.read_sql("""SELECT * FROM Department""",conn)
print(dept)

faculty = pd.read_sql("""SELECT * FROM Faculty""",conn)
print(faculty)

student = pd.read_sql("""SELECT * FROM Student""",conn)
print(student)

