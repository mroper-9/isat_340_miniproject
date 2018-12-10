import sqlite3
conn=sqlite3.connect("celebrities.db")
cursor=conn.cursor()
#sql statement
sql="select * from members"
cursor.execute(sql)
#get the rows
rows=cursor.fetchall()
#print the rows
for row in rows:
    print(row)
#close connection
conn.close()
