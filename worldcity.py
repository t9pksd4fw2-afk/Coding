import sqlite3 
import pandas as pd

conn = sqlite3.connect('cities.db')
conn.execute("DROP TABLE IF EXISTS City;")
conn.execute("""CREATE TABLE City(
City_Id INTEGER PRIMARY KEY,
City_Name TEXT NOT NULL UNIQUE,
Country TEXT NTO NULL,
Population INTEGER,
Is_Capital TEXT DEFAULT 'No');""")
conn.commit()
print("Table created successfully.")

conn.execute("INSERT INTO  City VALUES (1,'Tokyo','Japan',13960000,'Yes');")
conn.execute("INSERT INTO City VALUES (2,'Paris','France',7500000,'Yes');")
conn.execute("INSERT INTO  City VALUES (3,'London','UK',9000000,'Yes');")
conn.execute("INSERT INTO  City VALUES (4,'Sao Paolo','Brazil',5000000,'No');")
conn.execute("INSERT INTO  City VALUES (5,'Mumbai','India',2000000,'No');")
conn.execute("INSERT INTO City VALUES (6,'Shanghai','China',15960000,'No');")
conn.commit()
print("Rows inserted successfully.")
cities = pd.read_sql("SELECT * FROM City;",conn)
print(cities)

print("\n ---- TESTING PRIMARY KEY ----")
try:
    conn.execute("INSERT INTO City VALUES (1,'Cairo','Egypt',21232323,'Yes');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("City_ID 1 already belongs to TOKYO - PRIMARY KEY must be UNIQUE")
print("\n ---- TESTING NOT NULL ----")
try:
    conn.execute("INSERT INTO CITY VALUES(7,'Berlin',NULL,3645000,'Yes');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("Country is NOT NULL - every row must provide a country value.")
print("\n ---- TESTING UNIQUE ----")
try:
    conn.execute("INSERT INTO City VALUES (8,'Tokyo','Japan',99999,'No');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("City_NAME is UNIQUE - 'Tokyo' is already on the table.")
print("\n ---- DEFAULT value check for Shanghai ----")
shanghai = pd.read_sql("""SELECT City_Name, Country, Is_Capital FROM City WHERE City_NAME == 'Sydney'; """,conn)
print(shanghai)
print("Is_Capital wasn't given - DEFAULT 'No' was used automatically.")

print("\n ---- NULL in the Population column ----")
all_cities = pd.read_sql("""SELECT City_Name, Country , Population FROM City;""",conn)
print(all_cities)
missing = pd.read_sql("""SELECT City_Name FROM City WHERE Population ISNULL;""",conn)
print("Cities with no population data")
print(missing)

has_data = pd.read_sql("""SELECT City_Name, Population FROM City WHERE Population IS NOT NULL; """,conn)
print("Cities with population data:")
print(has_data)

show_all = pd.read_sql("""SELECT * FROM City;""",conn)
print(show_all)

population = pd.read_sql("""SELECT City_Name, Population FROM City WHERE Population > 10000000 ;""",conn)
print(population)

nocap = pd.read_sql("""SELECT Is_Capital FROM CITY WHERE Is_Capital = 'No' ;""",conn)

show_all = pd.read_sql("""SELECT * FROM City ORDER BY Population DESC;""",conn)
print(show_all)

count = pd.read_sql("SELECT COUNT(City_Id) FROM City;",conn)
print(count)
conn.close()