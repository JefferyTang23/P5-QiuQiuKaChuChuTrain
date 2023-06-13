from flask import Flask, render_template, request, redirect, session
from db import *
import os 
import random
import api_handler

app = Flask(__name__)

app.secret_key = os.urandom(32)

eventDays = [3, 8, 15, 20, 26, 34, 39, 45]

#event = []
@app.route("/")
def index():
    if 'username' in session:
        print("user is in session")
        return redirect('/next')
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
        return redirect('/next')
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
        session['username'] = username
        return redirect('/next')
    return redirect('/next')  #goes straight to game instead of needing to login 

@app.route('/home')
def homepage():
    return render_template('game.html')

@app.route('/direct_register')
def direct_register():
    return render_template("register.html", error_msg="Input Username and Password")

@app.route('/direct_login')
def direct_login():
    return render_template("login.html", error_msg="Input Username and Password")

def revent():
    # random = random.randint(0,100)
    # if random < 50:
    #     return getRandc()
    # else:

    event = getRand()
    happinessChange(session["username"], event[2])
    intelligenceChange(session["username"], event[3])
    rizzChange(session["username"], event[4])
    healthChange(session["username"], event[5])

    nameDesc = [event[0], event[1]]
    return nameDesc

# def sevent(day):
#     event = getSevent(day)

#     randomc = random.randint(0,100)

#     if randomc < 50:
#         desc = str(event[1]) + " " + str(event[2])
#         happinessChange(session["username"], event[4])
#         intelligenceChange(session["username"], event[5])
#         rizzChange(session["username"], event[6])
#         healthChange(session["username"], event[7])
#     else:
#         desc = str(event[1]) + " " + str(event[3])
#         happinessChange(session["username"], event[8])
#         intelligenceChange(session["username"], event[9])
#         rizzChange(session["username"], event[10])
#         healthChange(session["username"], event[11])
    
#     nameDesc = [event[0], desc]
#     return nameDesc

@app.route('/next')
def next():
    random_num = random.randint(0,100)
    day = getDay(session["username"])
    dayt = days()
    if (day >= 50):
        return redirect('/endGame')
    # elif(day in eventDays):
    #     event = sevent(day)
    elif(random_num < 100):
        event = revent()
    #else:  
    addDay(session["username"])
    gpa()
    return render_template('game.html', day = dayt, 
                           eventName = event[0], eventDesc = event[1], 
                           intelligence = getIntelligence(session["username"]), rizz = getRizz(session["username"]), 
                           happiness = getHappiness(session["username"]), health = getHealth(session["username"]),
                           gpa = getGpa(session["username"]))

@app.route("/academicC")
def academicC():
    intelligenceChange(session["username"], 5)
    rizzChange(session["username"], -5)
    return redirect('/next')

@app.route("/musicC")
def musicC():
    rizzChange(session["username"], 3)
    happinessChange(session["username"], 4)
    intelligenceChange(session["username"], -3)
    return redirect('/next')

@app.route("/danceC")
def danceC():
    rizzChange(session["username"], 5)
    happinessChange(session["username"], 2)
    intelligenceChange(session["username"], -3)
    return redirect('/next')

@app.route("/sportsT")
def sportsT():
    rizzChange(session["username"], 3)
    happinessChange(session["username"], 1)
    healthChange(session["username"], 5)
    intelligenceChange(session["username"], -3)
    return redirect('/next')
    
@app.route("/sleep")
def sleep():
    rizzChange(session["username"], -2)
    happinessChange(session["username"], 5)
    healthChange(session["username"], 3)
    intelligenceChange(session["username"], -3)
    return redirect('/next')

@app.route("/hangout")
def hangout():
    rizzChange(session["username"], 5)
    happinessChange(session["username"], 5)
    intelligenceChange(session["username"], -3)
    return redirect('/next')

@app.route("/murder")
def murder():
    rizzChange(session["username"], 5)
    happinessChange(session["username"], 10)
    chance = 0
    if (getIntelligence(session["username"]) > 90):
        chance = random.randint(50,100)
    else: 
        chance = random.randint(0,100)
    if chance <= 75:
        return redirect('/jail')
    return redirect('/next')

@app.route("/drugs")
def drugs():
    happinessChange(session["username"], 8)
    healthChange(session["username"], -5)
    chance = 0
    if getIntelligence(session["username"] > 90):
        chance = random.randint(5,100)
    else: 
        chance = random.randint(0,100)
    if chance < 6:
        return redirect('/jail')
    return redirect('/next')
        
@app.route("/study")
def study():
    happinessChange(session["username"], -5)
    healthChange(session["username"], -5)
    intelligenceChange(session["username"], 8)
    return redirect('/next')

@app.route("/jail")
def jail():
    return render_template("end_game_jail.html")

def gpa():
    if(getIntelligence(session["username"]) >= 95):
        change = [-0.1, 0.0, 0.1, 0.2, 0.3, 0.4]
    if(getIntelligence(session["username"]) < 95 and getIntelligence(session["username"]) >= 90):
        change = [-0.2, -0.1, 0.0, 0.1, 0.2, 0.3]
    if(getIntelligence(session["username"]) < 90 and getIntelligence(session["username"]) >= 80):
        change = [-0.3, -0.2, -0.1, 0.0, 0.1, 0.2]
    if(getIntelligence(session["username"]) < 80 and getIntelligence(session["username"]) >= 65):
        change = [-.35, -.2, -.1, 0, .15,]
    else:
        change = [-.4, -.3, -.2, -.1, 0, .1]

    gpachange = random.choice(change)
    gpaChange(session["username"], gpachange)

@app.route("/endGame")
def endGame():
    if(getHappiness(session["username"]) > 60):
        happiness_description = "Your high school years were relatively happy, despite the reputation Stuyvesant students have."
    else:
        happiness_description = "You had a miserable time at Stuyvesant and wished to get out every single. Little do you know, your time in college will only be more sad"
    if(getRizz(session["username"]) > 75):
        rizz_description = "You were very popular. There were five mentions of you on the crush wall. You have no difficulty getting a SO in college. Congrats!"
    elif(getRizz(session["username"]) > 50):
        rizz_description = "You were sort of popular and was mentioned twice on the crushwall! "
    else:
        rizz_description = "You are a complete loner that simped for people you had no chance for. Get better."
    if(getIntelligence(session["username"]) > 60):
        intelligence_description = "Even in Stuyvesant, you were considered above average smart. You will only continue to thrive in college!"
    else:
        intelligence_description = "Maybe Stuyvesant wasn't the school for you. You felt insecure in a place where everyone seemed smarter than you. You tell yourself that Stuyvesant was still a worthwhile experience!"
    return render_template("end_game.html", intelligence = getIntelligence(session["username"]), rizz = getRizz(session["username"]), happiness = getHappiness(session["username"]), healthy = getHealth(session["username"]), 
                    happinessd = happiness_description, rizzd = rizz_description, intelligenced = intelligence_description )

def days():
    day = getDay(session["username"])
    
    dayPrint = "null"
    if(day == 0):
        dayPrint = "Thursday, September 5th, 2019"
    elif(day == 1):
        dayPrint = "Wednesday, September 20th, 2019"
    elif(day == 2):
        dayPrint = "Monday, October 7th, 2019"
    elif(day == 3):
        dayPrint = "Thursday, October 24th, 2019"
    elif(day == 4):
        dayPrint = "Friday, November 8th, 2019"
    elif(day == 5):
        dayPrint = "Tuesday, November 19th, 2019"
    elif(day == 6):
        dayPrint = "Monday, December 9th, 2019"
    elif(day == 7):
        dayPrint = "Thursday, January 2nd, 2020"
    elif(day == 8):
        dayPrint = "Friday, January 24th, 2020"
    elif(day == 9):
        dayPrint = "Tuesday, February 11th, 2020"
    elif(day == 10):
        dayPrint = "Wednesday, February 25th, 2020"
    elif(day == 11):
        dayPrint = "Tuesday, March 13th, 2020"
    if(day == 12):
        dayPrint = "Monday, September 13st, 2021"
    elif(day == 13):
        dayPrint = "Thursday, September 23th, 2021"
    elif(day == 14):
        dayPrint = "Thursday, October 7th, 2021"
    elif(day == 15):
        dayPrint = "Monday, October 25th, 2021"
    elif(day == 16):
        dayPrint = "Tuesday, November 9th, 2021"
    elif(day == 17):
        dayPrint = "Wednesday, November 24th, 2021"
    elif(day == 18):
        dayPrint = "Thursday, December 9th, 2021"
    elif(day == 19):
        dayPrint = "Monday, January 3rd, 2022"
    elif(day == 20):
        dayPrint = "Monday, January 24th, 2022"
    elif(day == 21):
        dayPrint = "Friday, February 11th, 2022"
    elif(day == 22):
        dayPrint = "Thursday, February 24th, 2022"
    elif(day == 23):
        dayPrint = "Friday, March 11th, 2022"
    elif(day == 24):
        dayPrint = "Tuesday, March 22nd, 2022"
    elif(day == 25):
        dayPrint = "Friday, April 1st, 2022"
    elif(day == 26):
        dayPrint = "Wednesday, April 20th, 2022"
    elif(day == 27):
        dayPrint = "Friday, May 6th, 2022"
    elif(day == 28):
        dayPrint = "Thursday, May 20st, 2022"
    elif(day == 29):
        dayPrint = "Wednesday, June 1st, 2022"
    elif(day == 30):
        dayPrint = "Monday, June 27th, 2022"
    if(day == 31):
        dayPrint = "Thursday, September 8th, 2022"
    elif(day == 32):
        dayPrint = "Thursday, September 22nd, 2022"
    elif(day == 33):
        dayPrint = "Thursday, October 6th, 2022"
    elif(day == 34):
        dayPrint = "Monday, October 24th, 2022"
    elif(day == 35):
        dayPrint = "Tuesday, November 8th, 2022"
    elif(day == 36):
        dayPrint = "Wednesday, November 23rd, 2022"
    elif(day == 37):
        dayPrint = "Thursday, December 8th, 2022"
    elif(day == 38):
        dayPrint = "Tuesday, January 3rd, 2023"
    elif(day == 39):
        dayPrint = "Monday, January 23rd, 2023"
    elif(day == 40):
        dayPrint = "Friday, February 10th, 2023"
    elif(day == 41):
        dayPrint = "Thursday, February 23rd, 2023"
    elif(day == 42):
        dayPrint = "Friday, March 10th, 2023"
    elif(day == 43):
        dayPrint = "Tuesday, March 21st, 2023"
    elif(day == 44):
        dayPrint = "Monday, April 3rd, 2023"
    elif(day == 45):
        dayPrint = "Wednesday, April 19th, 2023"
    elif(day == 46):
        dayPrint = "Friday, May 5th, 2023"
    elif(day == 47):
        dayPrint = "Friday, May 19th, 2023"
    elif(day == 48):
        dayPrint = "Thursday, June 1st, 2023"
    elif(day == 49):
        dayPrint = "Monday, June 26th, 2023"
    if(day >= 50):
        print("THIS WORKS YEAHHH")
        return redirect('/endGame')
    print(day)
    return dayPrint
if __name__ == '__main__':
    init()
    app.run(debug=True, host='0.0.0.0')