import sqlite3


conn = sqlite3.connect('celebrities.db')
c = conn.cursor()
c.execute('''SELECT * FROM celebs ORDER BY celebID''')

r1 = c.fetchone()
r2 = c.fetchone()
r3 = c.fetchone()
r4 = c.fetchone()
r5 = c.fetchone()
r6 = c.fetchone()
r7 = c.fetchone()
r8 = c.fetchone()

celebID = r1[0]
firstname = r1[1]
lastname = r1[2]
age = r1[3]
email = r1[4]
photo = r1[5]
bio = r1[6]

conn.close()

return render_template('view_one_celeb.htm', celebID=celebID, firstname=firstname, lastname=lastname, age=age,
                       email=email, photo=photo,bio=bio)

