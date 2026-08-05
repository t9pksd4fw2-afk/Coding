import sqlite3
import pandas as pd

conn = sqlite3.connect('movie.db')
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS Movie;
DROP TABLE IF EXISTS Actor;
DROP TABLE IF EXISTS Movie_Actor;

CREATE TABLE Movie(
Movie_Id INTEGER PRIMARY KEY,
Title TEXT,
Genre TEXT,
Year INTEGER,
Rating REAL,
Duration INTEGER);

CREATE TABLE Actor(
Actor_Id INTEGER PRIMARY KEY,
Actor_Name TEXT,
Birth_Year INTEGER,
Country TEXT);

CREATE TABLE Movie_Actor(
Movie_Id INTEGER,
Actor_Id INTEGER);

INSERT INTO Movie VALUES
(1,'The Lion King','Animation',1994,8.5,88),
(2,'Toy Story 5','Animation',2026,8.0,90),
(3,'Spiderman','Action',2026,8.9,150),
(4,'Avengers','Action',2012,8.4,120),
(5,'Dune','Action',2024,8.7,120),
(6,'Star Wars','Action',1998,8.5,98),
(7,'Godfather','Action',1999,9.5,180),
(8,'Home Alone','Action',1992,7.8,110),
(9,'Black Panther','Action',2018,8.5,120),
(10,'Avengers Endgame','Action',2019,8.5,200),
(11,'Interstellar','Action',2011,9.5,130),
(12,'Moana','Animation',2017,6.5,90);

INSERT INTO Actor VALUES
(1,'Tom Hanks',1956,'USA'),
(2,'Tom Holland',1996,'UK'),
(3,'Idris Elba',1980,'UK'),
(4,'Ryan Reynolds',1982,'Canada'),
(5,'Will Smith',1968,'USA'),
(6,'Chris Evans',1986,'USA'),
(7,'Jackie Chan',1965,'China'),
(8,'Shah Rukh Khan',1966,'India'),
(9,'Lupita Nyongo',1983,'Kenya'),
(10,'Robert Downey JR',1976,'USA');

INSERT INTO Movie_Actor VALUES
(1,2),(2,1),(5,1),(6,3),(6,8),(7,4),(8,7),(9,5),(11,2),(12,1);
""")
conn.commit()
print('Database ready.')

genere = pd.read_sql("""SELECT DISTINCT(Genre) FROM Movie;""",conn)
print(genere)

country = pd.read_sql("""SELECT DISTINCT(Country) FROM Actor;""",conn)
print(country)

top_movies = pd.read_sql("""SELECT Title,Genre,Rating FROM Movie ORDER BY Rating DESC;""",conn)
print(top_movies)

oldest_first = pd.read_sql("""SELECT Title, Year FROM Movie ORDER BY Year;""",conn)
print(oldest_first)

youngest_actors = pd.read_sql("""SELECT Actor_Name,Birth_Year,Country FROM Actor ORDER BY Birth_Year DESC;""",conn)
print(youngest_actors)

action_count = pd.read_sql("""SELECT COUNT(Movie_Id) FROM Movie WHERE Genre == 'Action';""",conn)
print(action_count)

animation_mins = pd.read_sql("""SELECT SUM(Duration) FROM Movie WHERE Genre == 'Animation';""",conn)
print(animation_mins)

avg_action_dur = pd.read_sql("""SELECT AVG(Duration) FROM Movie WHERE Genre == 'Action';""",conn)
print(avg_action_dur)

avg_rating = pd.read_sql("""SELECT AVG(Rating) FROM Movie;""",conn)
print(avg_rating)

movies_per_genre = pd.read_sql("""SELECT Genre, COUNT(Movie_Id) FROM Movie GROUP BY Genre;""",conn)
print(movies_per_genre)

avg_per_genre = pd.read_sql("""SELECT Genre, AVG(Rating) FROM Movie GROUP BY Genre 
ORDER BY AVG(Rating) DESC;""",conn)
print(avg_per_genre)
conn.close()
