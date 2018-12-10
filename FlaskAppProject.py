__author__ = 'Tony Teate'

#imports
import sqlite3
from flask import Flask, render_template
from flask import request, redirect, url_for

#instantiate
app = Flask(__name__)
# route for handling the login page logic
#LOGIN FOR MATT
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    #connect to login table in database
    conn = sqlite3.connect("celebrities.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM login''')
    row1 = c.fetchone()
    row2 = c.fetchone()
    user1 = row1[0]
    pw1 = row1[1]
    user2 = row2[0]
    pw2 = row2[1]
    if request.method == 'POST':
        #accepts usernames and passwords for both members
        if (request.form['username'] != user1 or request.form['password'] != pw1) and (request.form['username'] != user2 or request.form['password'] != pw2):
            error = 'Invalid Credentials. Please try again.'
        elif request.form['username'] == user1:
            return redirect(url_for('info_matt'))
        elif request.form['username'] == user2:
            return redirect(url_for('info_caleb'))
    return render_template('login.htm', error=error)

#INFO MATT
@app.route('/info_matt', methods=['GET','POST'])
def info_matt():
    memberID = None
    firstname = ""
    lastname = ""
    age = None
    email = ""
    bio = ""
    success = False

    #this is called when the page is FIRST LOADED
    if request.method == 'GET':
        #connect to the database and select one record (row of data)
        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM members''')
        row = c.fetchone()
        # print (row)
        #if the row contains data, store it in variables
        if row:
            memberID = row[0]
            firstname = row[1]
            lastname = row[2]
            age = row[3]
            email = row[4]
            bio = row[5]
        #close connection to the database
        conn.close()
        #print(row)
    #this is called when the submit button is clicked
    if request.method == 'POST':
        # get the data from the form and store it in variables
        memberID = request.form['memberID']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age = request.form['age']
        email = request.form['email']
        bio = request.form['bio']
        success= True
        # now store the data from the form into the database
        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM members''')
        row = c.fetchone()
        if row: #if the row exist, update the data in the row
            c.execute('''UPDATE members SET firstname = ?, lastname = ?, age = ?, email = ?, bio = ? WHERE memberID=?''',
                      (firstname, lastname, age, email, bio, memberID))
        else: #if the row does not exist, insert data into the row
            c.execute('''INSERT INTO members VALUES (?, ?, ?, ?, ?, ?)''',
                      (memberID, firstname, lastname, age, email, bio))
        #success set to true so user sees message that their info was updated
        success=True
        conn.commit()
        conn.close()
    return render_template('profile.htm', memberID=memberID, firstname=firstname, lastname=lastname, age=age, email=email, bio=bio, success=success)
#INFO CALEB
@app.route('/info_caleb', methods=['GET','POST'])
def info_caleb():
    memberID = None
    firstname = ""
    lastname = ""
    age = None
    email = ""
    bio = ""
    success = False

    #this is called when the page is FIRST LOADED
    if request.method == 'GET':
        #connect to the database and select one record (row of data)
        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM members''')
        row = c.fetchone()
        row2 = c.fetchone()
        # print (row)
        #if the row contains data, store it in variables
        if row2:
            memberID = row2[0]
            firstname = row2[1]
            lastname = row2[2]
            age = row2[3]
            email = row2[4]
            bio = row2[5]
        #close connection to the database
        conn.close()
        #print(row)
    #this is called when the submit button is clicked
    if request.method == 'POST':
        # get the data from the form and store it in variables
        memberID = request.form['memberID']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age = request.form['age']
        email = request.form['email']
        bio = request.form['bio']
        success= True
        # now store the data from the form into the database
        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM members''')
        row = c.fetchone()
        row2 = c.fetchone()
        if row2: #if the row exist, update the data in the row
            c.execute('''UPDATE members SET firstname = ?, lastname = ?, age = ?, email = ?, bio = ? WHERE memberID=?''',
                      (firstname, lastname, age, email, bio, memberID))
        else: #if the row does not exist, insert data into the row
            c.execute('''INSERT INTO members VALUES (?, ?, ?, ?, ?, ?)''',
                      (memberID, firstname, lastname, age, email, bio))
        #success set to true so user sees message that their info was updated
        success=True
        conn.commit()
        conn.close()
    return render_template('profile_smith.htm', memberID=memberID, firstname=firstname, lastname=lastname, age=age, email=email, bio=bio, success=success)


def get(request):
    pass

#view all celebrities
@app.route('/view_all_celebs')
def view_all():
    celebID = None
    firstname = ''
    lastname = ''
    age = ''
    email = ''
    photo = ''
    bio = ''

    conn = sqlite3.connect('celebrities.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM celebs ORDER BY celebID''')
    rows = c.fetchall()
    conn.close()
    #return
    return render_template('view_all_celebs.htm', rows=rows)

#view one celeb
@app.route('/view_one_celeb')
def view_one():
    conn = sqlite3.connect('celebrities.db')
    c = conn.cursor()
    #change celebID in SQL statement to view a different celebrity
    c.execute('''SELECT * FROM celebs WHERE celebID="1"''')
    #rows for each individual celebrity
    r1 = c.fetchone()
    #selecting the first celebrity (r1)
    celebID = r1[0]
    firstname = r1[1]
    lastname = r1[2]
    age = r1[3]
    email = r1[4]
    photo = r1[5]
    bio = r1[6]

    conn.close()

    return render_template('view_one_celeb.htm', celebID=celebID, firstname=firstname, lastname=lastname, age=age,
                           email=email, photo=photo, bio=bio)


def post(request):
    pass

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == "__main__":
    app.run(debug=False)
