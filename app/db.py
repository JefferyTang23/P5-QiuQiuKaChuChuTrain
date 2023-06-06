import sqlite3
import random

DB_FILE="P5.db"

db = sqlite3.connect(DB_FILE, check_same_thread=False) 
c = db.cursor() 
c.execute("CREATE TABLE IF NOT EXISTS users(user TEXT UNIQUE, pwd TEXT, gpa REAL )")
c.execute("CREATE TABLE IF NOT EXISTS stats(user TEXT UNIQUE, happiness INTEGER, intelligence INTEGER, rizz INTEGER, health INTEGER)")
c.execute("CREATE TABLE IF NOT EXISTS rand_events(name TEXT, message TEXT, chance REAL, stat0c INTEGER, stat1c INTEGER, stat2c INTEGER, stat3c INTEGER )")
c.execute("CREATE TABLE IF NOT EXISTS randc_events(name TEXT, message TEXT, choice0 TEXT, choice1 TEXT, aftermath0 TEXT, aftermath1 TEXT, chance REAL, c0stat0c INTEGER, c0stat1c INTEGER, c0stat2c INTEGER, c0stat3c INTEGER, c1stat0c INTEGER, c1stat1c INTEGER, c1stat2c INTEGER, c1stat3c INTEGER )")
c.execute("CREATE TABLE IF NOT EXISTS stat_events(name TEXT, message TEXT, choice0 TEXT, choice1 TEXT, happiness INTEGER, intelligence INTEGER, rizz INTEGER, health INTEGER, stat0c INTEGER, stat1c INTEGER, stat2c INTEGER, stat3c INTEGER )")
c.execute("CREATE TABLE IF NOT EXISTS school_events(name TEXT, message TEXT, choice0 TEXT, choice1 TEXT, date TEXT )")
# c.execute("INSERT into users VALUES('?', '?', '?')")
# c.execute("INSERT into stats VALUES('?', '?', '?', '?', '?')")

c.execute("INSERT into rand_events('fall_bridge', 'You slipped on rat poop on the stairs to the bridge!', 20, -5, 0, -5, -2 )")
c.execute("INSERT into rand_events('escalator_died', 'The escalator you needed stopped working, AGAIN!', 20, -5, 0, 0, 2 )")
c.execute("INSERT into rand_events('ice_cream', 'The McDonald's ice cream machine stopped working, AGAIN!', 20, -5, 0, 0, 1 )")
c.execute("INSERT into rand_events('dropped_phone', 'You accidentally dropped your phone onto the subway tracks!', 20, -10, 0, 0, 1 )")
c.execute("INSERT into rand_events('teacher_out', 'Your teacher is out for 2 months!', 20, 10, -4, 0, 0 )")

c.execute("INSERT into randc_events('friend_leg', 'Your best friend breaks their leg falling down the stairs. You have a test, do you bring them to the hospital?', 'Help them', 'Leave them', 'You accompanied them and they appreciate you.', 'You took your test in guilt and couldn't focus.',  20, 1, 0, 3, 0, -5, 0, -5, 0  )") #in python, drop their grade by .05 if 2nd choice is chosen
c.execute("INSERT into randc_events('friend_leg', 'Your best friend breaks their leg falling down the stairs. You have a test, do you bring them to the hospital?', 'Help them', 'Leave them', 'You accompanied them and they appreciate you.', 'You took your test in guilt and couldn't focus.',  20, 1, 0, 3, 0, -5, 0, -5, 0  )")

def authenticate(user, pwd):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM users WHERE user = ? AND pwd = ?", (user, pwd))
    user = c.fetchone()
    db.commit()
    db.close()
    return user is not None

def check_login(user, pwd):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    getting_username = "SELECT user FROM users"
    command = c.execute(getting_username)
    usernames = command.fetchall()
    
    for x in range(len(usernames)):
        user_name = str(usernames[x])
        temp = user_name[2:len(user_name)-3]
        ex = c.execute("SELECT * FROM users")
        fetch = ex.fetchall()
        
        if (user == temp):
            print("Username already taken.")
            db.commit()
            db.close()
            return True
    db.commit()
    db.close()
    return False

def add_login(user, pwd):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT into users VALUES(?,?,?)",(user, pwd, 100))
    c.execute("INSERT into stats VALUES(?,?,?,?,?)",(user, random.randint(0, 100), random.randint(40, 100), random.randint(0, 100), random.randint(50, 100)))
    db.commit()
    db.close()

def intelligenceChange(user, change):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT intelligence FROM stats WHERE user=?", (user,))
    intelligence = c.fetchone()
    
    c.execute("UPDATE stats SET intelligence = ? WHERE user=?", (intelligence + change, user,))
    db.commit()
    db.close()

def rizzChange(user, change):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT rizz FROM stats WHERE user=?", (user,))
    rizz = c.fetchone()
    
    c.execute("UPDATE stats SET rizz = ? WHERE user=?", (rizz + change, user,))
    db.commit()
    db.close()
    
def healthChange(user, change):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT health FROM stats where user=?",(user,))
    health = c.fetchone()

    c.execute("UPDATE stats SET health = ? WHERE user=?", (health + change, user))
    db.commit()
    db.close()

c.execute("SELECT * FROM stats")
print1 = c.fetchall()
print(print1)

def getHealth(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT health FROM stats where user=?",(user,))
    health = c.fetchone()
    db.commit()
    db.close()

    return health

def getIntelligence(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT intelligence FROM stats where user=?",(user,))
    intelligence = c.fetchone()
    db.commit()
    db.close()
    
    return intelligence

def getHappiness(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT Happiness FROM stats where user=?",(user,))
    Happiness = c.fetchone()
    db.commit()
    db.close()
    
    return Happiness

def getRizz(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT Rizz FROM stats where user=?",(user,))
    Rizz = c.fetchone()
    db.commit()
    db.close()
    
    return Rizz