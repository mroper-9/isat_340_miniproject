import sqlite3
conn=sqlite3.connect("celebrities.db")
cursor=conn.cursor()

celebs="create table celebs(celebID text PRIMARY KEY, firstname text, lastname text, age integer, email text, photo text, bio text)"
cursor.execute(celebs)

conn.commit()
conn.close()