import sqlite3
import random

DB_FILE="P5.db"

db = sqlite3.connect(DB_FILE, check_same_thread=False) 
c = db.cursor() 
c.execute("CREATE TABLE IF NOT EXISTS users(user TEXT UNIQUE, pwd TEXT, gpa REAL )")
c.execute("""CREATE TABLE IF NOT EXISTS stats(user TEXT UNIQUE, 
    happiness INTEGER, intelligence INTEGER, rizz INTEGER, health INTEGER)""")
c.execute("""CREATE TABLE IF NOT EXISTS rand_events(name TEXT, message TEXT, 
chance REAL, stat0c INTEGER, stat1c INTEGER, stat2c INTEGER, stat3c INTEGER )""")
c.execute("""CREATE TABLE IF NOT EXISTS randc_events(name TEXT, message TEXT, choice0 TEXT, 
    choice1 TEXT, aftermath0 TEXT, aftermath1 TEXT, chance REAL, c0stat0c INTEGER, c0stat1c INTEGER, 
    c0stat2c INTEGER, c0stat3c INTEGER, c1stat0c INTEGER, c1stat1c INTEGER, c1stat2c INTEGER, c1stat3c INTEGER )""")
c.execute("""CREATE TABLE IF NOT EXISTS stat_events(name TEXT, message TEXT, choice0 TEXT, choice1 TEXT, 
    happiness INTEGER, intelligence INTEGER, rizz INTEGER, health INTEGER, stat0c INTEGER, stat1c INTEGER, 
    stat2c INTEGER, stat3c INTEGER )""")
c.execute("""CREATE TABLE IF NOT EXISTS school_events(name TEXT, message TEXT, choice0 TEXT, choice1 TEXT, 
    aftermath00 TEXT, aftermath01 TEXT, aftermath1 TEXT, c00stat0c INTEGER, c00stat1c INTEGER, c00stat2c INTEGER, 
    c00stat3c INTEGER, c01stat0c INTEGER, c01stat1c INTEGER, c01stat2c INTEGER, c01stat3c INTEGER, 
    c1stat0c INTEGER, c1stat1c INTEGER, c1stat2c INTEGER, c1stat3c INTEGER, date TEXT )""")
# c.execute("INSERT into users VALUES('?', '?', '?')")
# c.execute("INSERT into stats VALUES('?', '?', '?', '?', '?')")

def init():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("INSERT into rand_events VALUES(?, ?, ?, ?, ?, ?, ? )", 
              ('fall_bridge', 'You slipped on rat poop on the stairs to the bridge!', 20, -5, 0, -5, -2 ))
    c.execute("INSERT into rand_events VALUES(?, ?, ?, ?, ?, ?, ? )", 
              ('escalator_died', 'The escalator you needed stopped working, AGAIN!', 20, -5, 0, 0, 2 ))
    c.execute("INSERT into rand_events VALUES(?, ?, ?, ?, ?, ?, ? )", 
              ('ice_cream', 'The McDonalds ice cream machine stopped working, AGAIN!', 20, -5, 0, 0, 1 ))
    c.execute("INSERT into rand_events VALUES(?, ?, ?, ?, ?, ?, ? )", 
              ('dropped_phone', 'You accidentally dropped your phone onto the subway tracks!', 20, -10, 0, 0, 1 ))
    c.execute("INSERT into rand_events VALUES(?, ?, ?, ?, ?, ?, ? )", 
              ('teacher_out', 'Your teacher is out for 2 months!', 20, 10, -4, 0, 0 ))

    c.execute("INSERT into randc_events VALUES(?, ?, ?, ?, ?, ?,  ?, ?, ?, ?, ?, ?, ?, ?, ?  )", 
              ('friend_leg', 'Your best friend breaks their leg falling down the stairs. You have a test, do you bring them to the hospital?', 'Help them', 'Leave them', 'You accompanied them and they appreciate you.', 'You took your test in guilt and could not focus.',  20, 1, 0, 3, 0, -5, 0, -5, 0  )) #in python, drop their grade by .05 if 2nd choice is chosen
    c.execute("INSERT into randc_events VALUES(?, ?, ?, ?, ?, ?,  ?, ?, ?, ?, ?, ?, ?, ?, ?  )",
              ('book', 'You are reading your English book on the train but your body would rather sleep.', 'Force yourself to finish the reading', 'Close your eyes', 'You are tired, but you did well on the pop quiz in class!', 'That was a good nap; too bad you failed the pop quiz!',  20, -5, 3, 0, -5, 5, -5, 0, 5  )) #in python, drop their grade by .05 if 2nd choice is chosen
    c.execute("INSERT into randc_events VALUES(?, ?, ?, ?, ?, ?,  ?, ?, ?, ?, ?, ?, ?, ?, ?  )",
              ('lab', 'You accidentally knocked over and broke some lab equipment.', 'Confess to teacher', 'Hide the fact', 'Your classmates respected your decision but your teacher told your parents and you were fined.', 'Some students looked and laughed at you but you somehow got away with it.',  20, -10, 0, 5, 0, 5, 0, -5, 0  ))
    c.execute("INSERT into randc_events VALUES(?, ?, ?, ?, ?, ?,  ?, ?, ?, ?, ?, ?, ?, ?, ?  )", 
              ('homeless', 'A homeless person came up to you and asked you for money', 'Give $1', 'Walk away', 'Your wallet is emptier but you felt you did the right thing.', 'You walked away in guilt.',  20, 5, 0, 0, 0, -5, 0, 0, 0  )) #lose $1 for first choice
    c.execute("INSERT into randc_events VALUES(?, ?, ?, ?, ?, ?,  ?, ?, ?, ?, ?, ?, ?, ?, ?  )",
               ('book', 'You see one of your teacher pushing a book cart in the hallway. A student walks by and accidentally knocked over the books.', 'Help pick books up', 'Walk away', 'Your teacher appreciates you.', 'You walked away in guilt.',  20, 5, 0, 3, 0, -5, 0, -3, 0  ))

    c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
              ('StuySquad_2019', 'It\'s time for Stuy\'s annual dance show! Join StuySquad 2019?', 'Join', 'Don\'t take part', 'You helped put on an amazing show and met amazing people!', 'The show didn\'t go as planned but you still met a lot of cool people!', 'You chose not to take part', 30, -1, 20, 10, 20, -1, 12, 10, 0, 0, 0, 0, '19Oct0'))
    c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
              ('StuySquad_2021', 'It\'s time for Stuy\'s annual dance show! Join StuySquad 2021?', 'Join', 'Don\'t take part', 'You helped put on an amazing show and met amazing people!', 'The show didn\'t go as planned but you still met a lot of cool people!', 'You chose not to take part', 30, -1, 20, 10, 20, -1, 12, 10, 0, 0, 0, 0, '21Oct0'))
    c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
              ('StuySquad_2022', 'It\'s time for Stuy\'s annual dance show! Join StuySquad 2022?', 'Join', 'Don\'t take part', 'You helped put on an amazing show and met amazing people!', 'The show didn\'t go as planned but you still met a lot of cool people!', 'You chose not to take part', 30, -1, 20, 10, 20, -1, 12, 10, 0, 0, 0, 0, '2Oct0'))
    c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
              ('SING_2020', 'It\'s time for Stuy\'s annual SING! Join SING 2020?', 'Join', 'Don\'t take part', 'You helped put on an amazing show and met amazing people! Your grade was victorious!', 'Your grade couldn\'t win but you still met a lot of cool people!', 'You chose not to take part', 30, -1, 20, 10, 20, -1, 12, 10, 0, 0, 0, 0, '20Feb0'))
    c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
              ('SING_2022', 'It\'s time for Stuy\'s annual SING! Join SING 2022?', 'Join', 'Don\'t take part', 'You helped put on an amazing show and met amazing people! Your grade was victorious!', 'Your grade couldn\'t win but you still met a lot of cool people!', 'You chose not to take part', 30, -1, 20, 10, 20, -1, 12, 10, 0, 0, 0, 0, '22Feb0'))
    c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
              ('SING_2023', 'It\'s time for Stuy\'s annual SING! Join SING 2023', 'Join', 'Don\'t take part', 'You helped put on an amazing show and met amazing people! Your grade was victorious!', 'Your grade couldn\'t win but you still met a lot of cool people!', 'You chose not to take part', 30, -1, 20, 10, 20, -1, 12, 10, 0, 0, 0, 0, '23Feb0'))
    c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
              ('SOS_2022', 'It\'s time for Stuy\'s annual showcase! Join SOS 2022?', 'Join', 'Don\'t take part', 'You helped put on an amazing show and met amazing people!', 'The show didn\'t go as planned but you still met a lot of cool people!', 'You chose not to take part', 30, -1, 20, 10, 20, -1, 12, 10, 0, 0, 0, 0, '22Apr1'))
    c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
              ('SOS_2023', 'It\'s time for Stuy\'s annual showcase! Join SOS 2023?', 'Join', 'Don\'t take part', 'You helped put on an amazing show and met amazing people!', 'The show didn\'t go as planned but you still met a lot of cool people!', 'You chose not to take part', 30, -1, 20, 10, 20, -1, 12, 10, 0, 0, 0, 0, '23Apr1'))

    db.commit()
    db.close()
    
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