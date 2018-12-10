import sqlite3
conn=sqlite3.connect("celebrities.db")
cursor=conn.cursor()

members="create table members(memberID text PRIMARY KEY, firstname text, lastname text, age integer, email text, bio text)"
cursor.execute(members)

conn.commit()
conn.close()