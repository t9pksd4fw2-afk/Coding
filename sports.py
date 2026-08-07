import sqlite3
import pandas as pd

conn = sqlite3.connect('sports_team.db')
conn.execute("DROP TABLE IF EXISTS Player;")
conn.execute("""CREATE TABLE Player(Player_Id INTEGER PRIMARY KEY,
Player_Name TEXT NOT NULL UNIQUE,
Team_Name TEXT NOT NULL,
Jersey_Number INTEGER,
Is_Captain TEXT DEFAULT 'No');""")
conn.commit()
print("Table created successfully.")

conn.execute("INSERT INTO Player VALUES (1,'Aarav','Tigers',7,'Yes');")
conn.execute("INSERT INTO Player VALUES (2,'Diya','Tigers',10,'No');")
conn.execute("INSERT INTO Player VALUES (3,'Kabir','Lions',17,'No');")
conn.execute("INSERT INTO Player VALUES (4,'Meera','Eagles',11,'No');")
conn.execute("INSERT INTO Player VALUES (5,'Riya','Tigers',4,'No');")
conn.execute("INSERT INTO Player VALUES (6,'Arjun','Lions',2,'No');")
conn.commit()
print("Rows inserted successfully.")

players = pd.read_sql("SELECT * FROM Player;",conn)
print(players)

print("\n --- Testing PRIMARY KEY ---")
try:
    conn.execute("INSERT INTO Player VALUES (1,'Zoya','Sharks',8,'No');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected", e)
    print("Player_ID 1 already belongs to Aarav - PRIMAY KEY must be unique.")

print("\n --- Testing NOT NULL ---")
try:
    conn.execute("INSERT INTO Player VALUES (7,'Anaya',NULL,6,'No');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("Team_NAME is NOT NULL - every player must have a team name.")

print("\n --- Testing UNIQUE ---")
try:
    conn.execute("INSERT INTO Player VALUES(8,'Aarav','Sharks',12,'No');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("Player_Name is UNIQUE - 'Aarav' is already in the table.")

print("\n --- DEFAULT VALUE CHECK FOR ARJUN ---")
arjun = pd.read_sql("""SELECT Player_Name, Team_Name, Is_Captain FROM Player WHERE Player_Name == 'Arjun';""",conn)
print(arjun)
print("Is_CAPTAIN wasn't given - DEFAULT 'No' was used automatically.")

print("\n --- NULL in the Jersey_Number column ---")
all_players = pd.read_sql("""SELECT Player_Name, Team_Name, Jersey_Number FROM Player;""",conn)
print(all_players)

missing = pd.read_sql("""SELECT Player_Name FROM Player WHERE Jersey_Number IS NULL;""",conn)
print("Players with no jersey number:")
print(missing)

has_data = pd.read_sql("""SELECT Player_Name, Jersey_Number FROM Player WHERE Jersey_Number IS NOT NULL;""",conn)

print("Player with jersey numbers:")
print(has_data)

all = pd.read_sql("""SELECT * FROM Player;""",conn)
print(all)

desc = pd.read_sql("""SELECT * FROM Player ORDER BY Jersey_Number DESC;""",conn)
print(desc)

asc = pd.read_sql("""SELECT * FROM Player ORDER BY Jersey_Number ASC;""",conn)
print(asc)

conn.close()