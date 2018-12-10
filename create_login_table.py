import sqlite3
conn=sqlite3.connect("celebrities.db")
cursor=conn.cursor()

login="create table login(username text PRIMARY KEY, password text)"
cursor.execute(login)

conn.commit()
conn.close()