import sqlite3
import pandas as pd

conn = sqlite3.connect('cricket.db')
cursor = conn.cursor()

cursor.executescript("""DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Match;
DROP TABLE IF EXISTS Player_Match;
CREATE TABLE Match(
Match_Id INTEGER PRIMARY KEY,
Season_Id INTEGER,
Match_Winner INTEGER,
Win_Margin INTEGER);
CREATE TABLE Team(
Team_Id INTEGER PRIMARY KEY,
Team_Name TEXT);
CREATE TABLE Player_Match(
Match_Id INTEGER,
Player_Id INTEGER);
INSERT INTO Team VALUES
(1, 'Chennai Super Kings'),(2,'Dehli Capitals'),(3,'Deccan Chargers'),(4,'Dehli Daredevils'),(5,'Mumbai Indians'),(6,'Kolkata Knight Riders'),(7,'Rajasthan Royals'),(8,'Kings XI Punjab');
INSERT INTO Match VALUES
(1,7,5,35),(2,6,4,33),(3,6,5,45),(4,4,3,34),(5,7,8,10),(6,3,4,51),(7,2,2,45),(8,4,5,50),(9,6,6,50),(10,3,4,40),(11,6,3,36),(12,4,5,70);
INSERT INTO Player_Match VALUES
(1,101),(1,12),(2,103),(3,101),(4,104),(5,102);""")
conn.commit()
print('Database ready!')

tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type = 'table';""",conn)
print(tables)

matches = pd.read_sql("""SELECT * FROM Match;""",conn)
print(matches)
print('Rows and columns:',matches.shape)

teams = pd.read_sql("""SELECT * FROM Team;""",conn)
print(teams)

team_names = pd.read_sql("""SELECT Team_Id, Team_Name FROM Team;""",conn)
print(team_names)

player_matches = pd.read_sql("""SELECT Match_Id,Player_Id FROM Player_Match;""",conn)
print(player_matches)

rr_wins = pd.read_sql("""SELECT * FROM Match WHERE Match_Winner == 7;""",conn)
print(rr_wins)

mi_recent = pd.read_sql("""SELECT * FROM Match WHERE Match_Winner == 5 AND Season_Id IN (8,9);""",conn)
print(mi_recent)

de_teams = pd.read_sql("""SELECT * FROM Team WHERE Team_Name LIKE 'De%';""",conn)
print(de_teams)

kings_teams = pd.read_sql("""SELECT * FROM Team WHERE Team_Name LIKE '%Kings';""",conn)
print(kings_teams)

win_margins = pd.read_sql("""SELECT MIN(Win_Margin),MAX(Win_Margin) FROM Match;""",conn)
print(win_margins)

seasons = pd.read_sql("""SELECT MIN(Season_Id),MAX(Season_Id) FROM Match;""",conn)
print(seasons)

conn.close()

