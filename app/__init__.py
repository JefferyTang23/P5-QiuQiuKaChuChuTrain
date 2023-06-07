from flask import Flask, render_template, request, redirect, session
from db import *
import os 

app = Flask(__name__)

app.secret_key = os.urandom(32)

@app.route("/")
def index():
    if 'username' in session:
        print("user is in session")
        return render_template('game.html')
    return render_template('login.html', error_msg="Input Username and Password")

@app.route('/login', methods = ["GET", "POST"])
def login():
    username = request.form.get('username') 
    password = request.form.get('password')

    # if username and password are correct
    print(authenticate(username, password))
    if (authenticate(username, password)):
        session['username'] = username # create a session/cookie w/username
        print("session started")
        return render_template('game.html')
    # if password is wrong or username is wrong
    else:
        print("sigh")
        return render_template('login.html', error_msg="Incorrect Credentials") # displays login page 
    

@app.route('/register', methods = ["GET", "POST"])
def register():
    username = request.form.get('username') # username user inputs on form
    password = request.form.get('password') # password user inputs on form

    # if any field is empty
    if ((username == "") or (password == "")):
        return render_template( 'register.html', error_msg="Fill in any blank fields") # displays create_account page w/error_msg
    
    # if username is not unique / the same as another user's username (check in database)
    if (check_login(username, password)):
        return render_template( 'register.html', error_msg="Username already taken") # displays create_account page w/error_msg
    
    # username is unique
    if (request.method == 'POST'):
        add_login(username, password)
        return redirect('/home')
    return render_template('game.html')  #goes straight to game instead of needing to login 

@app.route('/home')
def homepage():
    return render_template('game.html')

@app.route('/direct_register')
def direct_register():
    return render_template("register.html", error_msg="Input Username and Password")

@app.route('/direct_login')
def direct_login():
    return render_template("login.html", error_msg="Input Username and Password")
"""CREATE TABLE IF NOT EXISTS rand_events(name TEXT, message TEXT, 
chance REAL, stat0c INTEGER, stat1c INTEGER, stat2c INTEGER, stat3c INTEGER )""")
("""CREATE TABLE IF NOT EXISTS randc_events(name TEXT, message TEXT, choice0 TEXT, 
    choice1 TEXT, aftermath0 TEXT, aftermath1 TEXT, chance REAL, c0stat0c INTEGER, c0stat1c INTEGER, 
    c0stat2c INTEGER, c0stat3c INTEGER, c1stat0c INTEGER, c1stat1c INTEGER, c1stat2c INTEGER, c1stat3c INTEGER )""")
def event():
    random = randint(0,100)
    if random < 50:
        event = getRandc()
        name = event[0]
        desc = event[1]
        c1 = event[2]
        c2 = event[3]
        a0 = event[4]
        a1 = event[5]
        
    else:
        event = getRand()
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')