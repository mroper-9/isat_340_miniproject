import sqlite3
conn=sqlite3.connect("celebrities.db")
cursor=conn.cursor()

#table data
row="insert into members values(?,?,?,?,?,?)"
data=((1,"Matthew","Roper",21,"ropermj@dukes.jmu.edu","I was born and raised in Fairfax County, VA. I am now a senior at JMU majoring in Integrated Science and Technology."),
      (2,"Caleb","Smith",21,"smith7cj@dukes.jmu.edu","I was born and raised in Roanoke, Virginia...."))
cursor.executemany(row,data)
#commit changes and close connection
conn.commit()
conn.close()