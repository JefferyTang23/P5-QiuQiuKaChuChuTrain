import sqlite3
import random

DB_FILE="P5.db"

db = sqlite3.connect(DB_FILE, check_same_thread=False) 
c = db.cursor() 
c.execute("CREATE TABLE IF NOT EXISTS users(user TEXT UNIQUE, pwd TEXT, gpa REAL )")
c.execute("CREATE TABLE IF NOT EXISTS stats(user TEXT UNIQUE, happiness INTEGER, intelligence INTEGER, rizz INTEGER, health INTEGER)")
# c.execute("INSERT into users VALUES('?', '?', '?')")
# c.execute("INSERT into stats VALUES('?', '?', '?', '?', '?')")


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
