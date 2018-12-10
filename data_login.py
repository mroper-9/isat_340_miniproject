import sqlite3
conn=sqlite3.connect("celebrities.db")
cursor=conn.cursor()

#table data
row="insert into login values(?,?)"
data=(("Matthew","Roper"),("Caleb","Smith"))
cursor.executemany(row,data)
#commit changes and close connection
conn.commit()
conn.close()