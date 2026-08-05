import sqlite3
import pandas as pd

conn = sqlite3.connect('wildlife_park.db')
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS Animal;
DROP TABLE IF EXISTS Keeper;
DROP TABLE IF EXISTS Animal_Keeper;

CREATE TABLE Animal(
Animal_Id INTEGER PRIMARY KEY,
Animal_Name TEXT,
Animal_Type TEXT,
Habitat TEXT,
Age INTEGER,
Food_Kg REAL);

CREATE TABLE Keeper(
Keeper_Id INTEGER PRIMARY KEY,
Keeper_Name TEXT,
Country TEXT);

CREATE TABLE Animal_Keeper(
Animal_Id INTEGER,
Keeper_Id INTEGER);

INSERT INTO Animal VALUES
(1,'Leo','Mammal','Savannah',8,7.5),
(2,'Maya','Mammal','Savannah',5,6.0),
(3,'Tim','Bird','Rainforest',4,1.5),
(4,'Ted','Reptile','Rainforest',3,3.5),
(5,'Ryan','Bird','Wetland',10,2.5),
(6,'Jude','Mammal','Forest',6,3.5),
(7,'Harry','Reptile','Forest',2,4.0),
(8,'Phil','Reptile','Desert',9,2.5),
(9,'Cole','Mammal','Desert',11,1.5),
(10,'Raul','Bird','Savannah',5,6.5),
(11,'Max','Reptile','Forest',6,9.5),
(12,'Bryan','Nird','Savannah',7,3.0);

INSERT INTO Keeper VALUES
(1,'Aarav','India'),
(2,'Bill','USA'),
(3,'Meera','India'),
(4,'Kabir','India'),
(5,'Riya','India');

INSERT INTO Animal_Keeper VALUES
(1,1),(2,1),(3,2),(4,2),(5,3),(6,4),(7,4),(8,3),(9,5),(10,1);


""")
conn.commit()
print('Wildlife database ready.')

animal_type = pd.read_sql("""SELECT DISTINCT(Animal_Type) FROM Animal;""",conn)
print(animal_type)

habitats = pd.read_sql("""SELECT DISTINCT(Habitat) FROM Animal;""",conn)
print(habitats)

oldest_animals = pd.read_sql("""SELECT Animal_Name, Animal_Type, Age FROM Animal ORDER BY Age DESC;""",conn)
print(oldest_animals)

food_order = pd.read_sql("""SELECT Animal_Name,Food_Kg FROM Animal ORDER BY Food_Kg;""",conn)
print(food_order)

keeper_names = pd.read_sql("""SELECT Keeper_Name, Country FROM Keeper ORDER BY Keeper_Name;""",conn)
print(keeper_names)

mammal_count = pd.read_sql("""SELECT COUNT(Animal_Id) FROM ANIMAL WHERE Animal_Type = 'Mammal';""",conn)
print(mammal_count)

bird_food = pd.read_sql("""SELECT SUM(Food_Kg) FROM Animal WHERE Animal_Type == 'Bird';""",conn)
print(bird_food)

average_age = pd.read_sql("""SELECT AVG(Age) FROM Animal;""",conn)
print(average_age)

average_mammal_food = pd.read_sql("""SELECT AVG(Food_Kg) FROM Animal WHERE Animal_Type == 'Mammmal';""",conn)
print(average_mammal_food)

animals_per_habitat = pd.read_sql("""SELECT Habitat,COUNT(Animal_Id) FROM Animal GROUP BY Habitat;""",conn)
print(animals_per_habitat)

average_age_per_habitat = pd.read_sql("""SELECT Habitat, AVG(Age) FROM Animal GROUP BY Habitat ORDER BY AVG(Age) DESC;""",conn)
print(average_age_per_habitat)

conn.close()