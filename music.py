import sqlite3
import pandas as pd

conn = sqlite3.connect('music.db')

conn.execute("CREATE TABLE song(song_id INTEGER PRIMARY KEY, song_name TEXT NOT NULL, song_streams INTEGER, song_duration REAL)")


conn.executemany("INSERT INTO song VALUES(?,?,?,?)",[
    (4331,"God's Plan",34000000,2.01),(4332,'Thriller',10000000,3.53),(4333,'Beat It',9000000,5.03),(4334,'Graduation',50000000,4.40),(4335,'Billie Jean',34211330,7.01),
     ])

conn.execute("CREATE TABLE artist(artist_id INTEGER PRIMARY KEY, artist_name TEXT, artist_country TEXT)")

conn.executemany('INSERT INTO artist VALUES(?,?,?)',[(3211,"Michael Jackson","USA"),(3212,"Drake","USA"),(3213,"Kanye West","USA"),])

conn.execute("CREATE TABLE album(album_id INTEGER PRIMARY KEY,album_name TEXT, artist_id INTEGER)")

conn.executemany("INSERT INTO album VALUES(?,?,?)",[(1111,"Thriller",3211),(1112,"Graduation",3213),(1113,"Smooth Criminal",3211),])

song = pd.read_sql("SELECT * FROM song",conn)
print(song)
print()

album = pd.read_sql("SELECT * FROM album",conn)
print(album)
print()

artist = pd.read_sql("SELECT * FROM artist",conn)
print(artist)
print()

