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
        s00 = event[6]
        s01 = event[7]
        s02 = event[8]
        s03 = event[9]
        s10 = event[10]
        s11 = event[11]
        s12 = event[12]
        s13 = event[13]
    return render_template("game.html", nameofevent = name, description = desc, choice1 = c1, choice2 = c2)
    else:
        event = getRand()
        name = event[0]
        desc = event[1]
        c1 = event[2]
        c2 = event[3]
        a0 = event[4]
        a1 = event[5]
        s0 = event[6]
        s1 = event[7]
        s2 = event[8]
        s3 = event[9]


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')