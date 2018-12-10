import sqlite3
conn=sqlite3.connect("celebrities.db")
cursor=conn.cursor()
#update statement
sql="update celebs set photo=replace(photo, 'nphinity', 'software4rfid')"
cursor.execute(sql)
#close connection
conn.commit()
conn.close()
