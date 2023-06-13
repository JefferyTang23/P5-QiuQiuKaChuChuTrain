import sqlite3
import random

DB_FILE="P5.db"

db = sqlite3.connect(DB_FILE, check_same_thread=False) 
c = db.cursor() 
c.execute("CREATE TABLE IF NOT EXISTS users(user TEXT UNIQUE, pwd TEXT, gpa REAL, day INTEGER )")
c.execute("""CREATE TABLE IF NOT EXISTS stats(user TEXT UNIQUE, 
    happiness INTEGER, intelligence INTEGER, rizz INTEGER, health INTEGER)""")
c.execute("""CREATE TABLE IF NOT EXISTS rand_events(name TEXT, message TEXT, stat0c INTEGER, stat1c INTEGER, stat2c INTEGER, stat3c INTEGER )""")
c.execute("""CREATE TABLE IF NOT EXISTS randc_events(name TEXT, message TEXT, choice0 TEXT, 
    choice1 TEXT, aftermath0 TEXT, aftermath1 TEXT, c0stat0c INTEGER, c0stat1c INTEGER, 
    c0stat2c INTEGER, c0stat3c INTEGER, c1stat0c INTEGER, c1stat1c INTEGER, c1stat2c INTEGER, c1stat3c INTEGER )""")
# c.execute("""CREATE TABLE IF NOT EXISTS school_events(name TEXT, message TEXT, 
#    aftermath0 TEXT, aftermath1 TEXT, c0stat0c INTEGER, c0stat1c INTEGER, c0stat2c INTEGER, 
#    c0stat3c INTEGER, c1stat0c INTEGER, c1stat1c INTEGER, c1stat2c INTEGER, c1stat3c INTEGER, date INTEGER )""")

#c.execute("""CREATE TABLE IF NOT EXISTS stat_events(name TEXT, message TEXT, choice0 TEXT, choice1 TEXT, 
    #happiness INTEGER, intelligence INTEGER, rizz INTEGER, health INTEGER, stat0c INTEGER, stat1c INTEGER, 
    #stat2c INTEGER, stat3c INTEGER )""")
# c.execute("""CREATE TABLE IF NOT EXISTS school_events(name TEXT, message TEXT, choice0 TEXT, choice1 TEXT, 
#    aftermath00 TEXT, aftermath01 TEXT, aftermath1 TEXT, c00stat0c INTEGER, c00stat1c INTEGER, c00stat2c INTEGER, 
#    c00stat3c INTEGER, c01stat0c INTEGER, c01stat1c INTEGER, c01stat2c INTEGER, c01stat3c INTEGER, 
#    c1stat0c INTEGER, c1stat1c INTEGER, c1stat2c INTEGER, c1stat3c INTEGER, date INTEGER )""")
# c.execute("INSERT into users VALUES('?', '?', '?')")
# c.execute("INSERT into stats VALUES('?', '?', '?', '?', '?')")


def init():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("INSERT into rand_events VALUES(?, ?, ?, ?, ?, ? )", 
              ('fall_bridge', 'You slipped on rat poop on the stairs to the bridge!', -5, 0, -5, -2 ))
    c.execute("INSERT into rand_events VALUES(?, ?, ?, ?, ?, ? )", 
              ('escalator_died', 'The escalator you needed stopped working, AGAIN!', -5, 0, 0, 2 ))
    c.execute("INSERT into rand_events VALUES(?, ?, ?, ?, ?, ? )", 
              ('ice_cream', 'The McDonalds ice cream machine stopped working, AGAIN!', -5, 0, 0, 1 ))
    c.execute("INSERT into rand_events VALUES(?, ?, ?, ?, ?, ? )", 
              ('dropped_phone', 'You accidentally dropped your phone onto the subway tracks!', -10, 0, 0, 1 ))
    c.execute("INSERT into rand_events VALUES(?, ?, ?, ?, ?, ? )", 
              ('teacher_out', 'Your teacher is out for 2 months!', 10, -4, 0, 0 ))
    c.execute("INSERT into rand_events VALUES(?, ?, ?, ?, ?, ? )", 
              ('gift', 'You recieved a mystery gift that someone put in your locker', 5, 0, 8, 0 ))
    c.execute("INSERT into rand_events VALUES(?, ?, ?, ?, ?, ? )", 
              ('laptop_broke', 'Your laptop broke, but your mom promised to get you a new one!', 10, 0, 0, 0 ))
    c.execute("INSERT into rand_events VALUES(?, ?, ?, ?, ?, ? )", 
              ('teacher_see', 'You saw your teacher in the hallway and was too awkward to say hi', -3, 0, -2, 0 ))
    c.execute("INSERT into rand_events VALUES(?, ?, ?, ?, ?, ? )", 
              ('crush_hi', 'Your crush said hi to you!', 5, 0, 0, 1 ))
    c.execute("INSERT into rand_events VALUES(?, ?, ?, ?, ?, ? )", 
              ('response_right', 'You answered a question right in front of everyone!', 3, 3, 1, 0 ))
    # c.execute("INSERT into randc_events VALUES(?, ?, ?, ?, ?,  ?, ?, ?, ?, ?, ?, ?, ?, ?  )", 
    #           ('friend_leg', 'Your best friend breaks their leg falling down the stairs. You have a test, do you bring them to the hospital?', 'Help them', 'Leave them', 'You accompanied them and they appreciate you.', 'You took your test in guilt and could not focus.',  20, 1, 0, 3, 0, -5, 0, -5, 0  )) #in python, drop their grade by .05 if 2nd choice is chosen
    # c.execute("INSERT into randc_events VALUES(?, ?, ?, ?, ?,  ?, ?, ?, ?, ?, ?, ?, ?, ?  )",
    #           ('book', 'You are reading your English book on the train but your body would rather sleep.', 'Force yourself to finish the reading', 'Close your eyes', 'You are tired, but you did well on the pop quiz in class!', 'That was a good nap; too bad you failed the pop quiz!',  20, -5, 3, 0, -5, 5, -5, 0, 5  )) #in python, drop their grade by .05 if 2nd choice is chosen
    # c.execute("INSERT into randc_events VALUES(?, ?, ?, ?, ?,  ?, ?, ?, ?, ?, ?, ?, ?, ?  )",
    #           ('lab', 'You accidentally knocked over and broke some lab equipment.', 'Confess to teacher', 'Hide the fact', 'Your classmates respected your decision but your teacher told your parents and you were fined.', 'Some students looked and laughed at you but you somehow got away with it.',  20, -10, 0, 5, 0, 5, 0, -5, 0  ))
    # c.execute("INSERT into randc_events VALUES(?, ?, ?, ?, ?,  ?, ?, ?, ?, ?, ?, ?, ?, ?  )", 
    #           ('homeless', 'A homeless person came up to you and asked you for money', 'Give $1', 'Walk away', 'Your wallet is emptier but you felt you did the right thing.', 'You walked away in guilt.',  20, 5, 0, 0, 0, -5, 0, 0, 0  )) #lose $1 for first choice
    # c.execute("INSERT into randc_events VALUES(?, ?, ?, ?, ?,  ?, ?, ?, ?, ?, ?, ?, ?, ?  )",
    #            ('book', 'You see one of your teacher pushing a book cart in the hallway. A student walks by and accidentally knocked over the books.', 'Help pick books up', 'Walk away', 'Your teacher appreciates you.', 'You walked away in guilt.',  20, 5, 0, 3, 0, -5, 0, -3, 0  ))

    # c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
    #           ('StuySquad_2019', 'It\'s time for Stuy\'s annual dance show!', 
    #            'You helped put on an amazing show and met amazing people!', 'The show didn\'t go as planned but you still met a lot of cool people!', 
    #            30, -1, 20, 10, 20, -1, 12, 10, 3))
    # c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
    #           ('StuySquad_2021', 'It\'s time for Stuy\'s annual dance show!', 
    #            'You helped put on an amazing show and met amazing people!', 'The show didn\'t go as planned but you still met a lot of cool people!', 
    #            30, -1, 20, 10, 20, -1, 12, 10, 15))
    # c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
    #           ('StuySquad_2022', 'It\'s time for Stuy\'s annual dance show!', 
    #            'You helped put on an amazing show and met amazing people!', 'The show didn\'t go as planned but you still met a lot of cool people!',
    #            30, -1, 20, 10, 20, -1, 12, 10, 34))
    # c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
    #           ('SING_2020', 'It\'s time for Stuy\'s annual SING!', 
    #            'You helped put on an amazing show and met amazing people! Your grade was victorious!', 'Your grade couldn\'t win but you still met a lot of cool people!',
    #            30, -1, 20, 10, 20, -1, 12, 10, 8))
    # c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
    #           ('SING_2022', 'It\'s time for Stuy\'s annual SING!',
    #            'You helped put on an amazing show and met amazing people! Your grade was victorious!', 'Your grade couldn\'t win but you still met a lot of cool people!', 
    #            30, -1, 20, 10, 20, -1, 12, 10, 20))
    # c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
    #           ('SING_2023', 'It\'s time for Stuy\'s annual SING!', 
    #            'You helped put on an amazing show and met amazing people! Your grade was victorious!', 'Your grade couldn\'t win but you still met a lot of cool people!', 
    #            30, -1, 20, 10, 20, -1, 12, 10, 39))
    # c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
    #           ('SOS_2022', 'It\'s time for Stuy\'s annual SOS!', 
    #            'You helped put on an amazing show and met amazing people!', 'The show didn\'t go as planned but you still met a lot of cool people!', 
    #            30, -1, 20, 10, 20, -1, 12, 10, 26))
    # c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
    #           ('SOS_2023', 'It\'s time for Stuy\'s annual SOS!', 
    #            'You helped put on an amazing show and met amazing people!', 'The show didn\'t go as planned but you still met a lot of cool people!', 
    #            30, -1, 20, 10, 20, -1, 12, 10, 45))

    # c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
    #           ('StuySquad_2019', 'It\'s time for Stuy\'s annual dance show! Join StuySquad 2019?', 'Join', 'Don\'t take part', 'You helped put on an amazing show and met amazing people!', 'The show didn\'t go as planned but you still met a lot of cool people!', 'You chose not to take part', 30, -1, 20, 10, 20, -1, 12, 10, 0, 0, 0, 0, 3))
    # c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
    #           ('StuySquad_2021', 'It\'s time for Stuy\'s annual dance show! Join StuySquad 2021?', 'Join', 'Don\'t take part', 'You helped put on an amazing show and met amazing people!', 'The show didn\'t go as planned but you still met a lot of cool people!', 'You chose not to take part', 30, -1, 20, 10, 20, -1, 12, 10, 0, 0, 0, 0, 15))
    # c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
    #           ('StuySquad_2022', 'It\'s time for Stuy\'s annual dance show! Join StuySquad 2022?', 'Join', 'Don\'t take part', 'You helped put on an amazing show and met amazing people!', 'The show didn\'t go as planned but you still met a lot of cool people!', 'You chose not to take part', 30, -1, 20, 10, 20, -1, 12, 10, 0, 0, 0, 0, 34))
    # c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
    #           ('SING_2020', 'It\'s time for Stuy\'s annual SING! Join SING 2020?', 'Join', 'Don\'t take part', 'You helped put on an amazing show and met amazing people! Your grade was victorious!', 'Your grade couldn\'t win but you still met a lot of cool people!', 'You chose not to take part', 30, -1, 20, 10, 20, -1, 12, 10, 0, 0, 0, 0, 8))
    # c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
    #           ('SING_2022', 'It\'s time for Stuy\'s annual SING! Join SING 2022?', 'Join', 'Don\'t take part', 'You helped put on an amazing show and met amazing people! Your grade was victorious!', 'Your grade couldn\'t win but you still met a lot of cool people!', 'You chose not to take part', 30, -1, 20, 10, 20, -1, 12, 10, 0, 0, 0, 0, 20))
    # c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
    #           ('SING_2023', 'It\'s time for Stuy\'s annual SING! Join SING 2023', 'Join', 'Don\'t take part', 'You helped put on an amazing show and met amazing people! Your grade was victorious!', 'Your grade couldn\'t win but you still met a lot of cool people!', 'You chose not to take part', 30, -1, 20, 10, 20, -1, 12, 10, 0, 0, 0, 0, 39))
    # c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
    #           ('SOS_2022', 'It\'s time for Stuy\'s annual showcase! Join SOS 2022?', 'Join', 'Don\'t take part', 'You helped put on an amazing show and met amazing people!', 'The show didn\'t go as planned but you still met a lot of cool people!', 'You chose not to take part', 30, -1, 20, 10, 20, -1, 12, 10, 0, 0, 0, 0, 26))
    # c.execute("INSERT into school_events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
    #           ('SOS_2023', 'It\'s time for Stuy\'s annual showcase! Join SOS 2023?', 'Join', 'Don\'t take part', 'You helped put on an amazing show and met amazing people!', 'The show didn\'t go as planned but you still met a lot of cool people!', 'You chose not to take part', 30, -1, 20, 10, 20, -1, 12, 10, 0, 0, 0, 0, 45))

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
    c.execute("INSERT into users VALUES(?,?,?,?)",(user, pwd, 95, 0))
    c.execute("INSERT into stats VALUES(?,?,?,?,?)",(user, random.randint(0, 100), random.randint(40, 100), random.randint(0, 100), random.randint(50, 100)))
    db.commit()
    db.close()

def happinessChange(user, change):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT happiness FROM stats WHERE user=?", (user,))
    happiness = c.fetchone()
    
    newval = int(happiness[0]) + int(change)
    if(newval > 100):
        newval = 100
    if(newval < 0):
        newval = 0

    c.execute("UPDATE stats SET happiness = ? WHERE user=?", (newval, user,))
    db.commit()
    db.close()

def intelligenceChange(user, change):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT intelligence FROM stats WHERE user=?", (user,))
    intelligence = c.fetchone()
    
    newval = intelligence[0] + change
    if(newval > 100):
        newval = 100
    if(newval < 0):
        newval = 0

    c.execute("UPDATE stats SET intelligence = ? WHERE user=?", (newval, user,))
    db.commit()
    db.close()

def rizzChange(user, change):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT rizz FROM stats WHERE user=?", (user,))
    rizz = c.fetchone()
    
    newval = rizz[0] + change
    if(newval > 100):
        newval = 100
    if(newval < 0):
        newval = 0

    c.execute("UPDATE stats SET rizz = ? WHERE user=?", (newval, user,))
    db.commit()
    db.close()
    
def healthChange(user, change):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT health FROM stats where user=?",(user,))
    health = c.fetchone()

    newval = health[0] + change
    if(newval > 100):
        newval = 100
    if(newval < 0):
        newval = 0

    c.execute("UPDATE stats SET health = ? WHERE user=?", (newval, user))
    db.commit()
    db.close()

def gpaChange(user, change):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT gpa FROM users where user=?",(user,))
    gpa = c.fetchone()

    newval = gpa[0] + change
    if(newval > 100):
        newval = 100
    if(newval < 0):
        newval = 0
    newval = round(newval, 2)
    c.execute("UPDATE users SET gpa = ? WHERE user=?", (newval, user))
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

    return health[0]

def getIntelligence(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT intelligence FROM stats where user=?",(user,))
    intelligence = c.fetchone()
    db.commit()
    db.close()
    
    return intelligence[0]

def getHappiness(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT Happiness FROM stats where user=?",(user,))
    Happiness = c.fetchone()
    db.commit()
    db.close()
    
    return Happiness[0]

def getRizz(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT Rizz FROM stats where user=?",(user,))
    Rizz = c.fetchone()
    db.commit()
    db.close()
    
    return Rizz[0]

# def getRandc():
#     db = sqlite3.connect(DB_FILE)
#     c = db.cursor()
#     c.execute("SELECT * FROM randc_events")
#     all_events = c.fetchall()
#     #print(all_events)

#     event = random.choice(all_events)
#     print(event)
#     db.commit()
#     db.close()
#     return event

def getRand():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM rand_events")
    all_events = c.fetchall()
    #print(all_events)

    event = random.choice(all_events)
    # print(event)
    db.commit()
    db.close()
    return event

# def getSevent(day):
#     db = sqlite3.connect(DB_FILE)
#     c = db.cursor()
#     print(day)
#     int(day)
#     c.execute("""SELECT name, message, aftermath0, aftermath1, c0stat0c, c0stat1c, c0stat2c, 
#    c0stat3c, c1stat0c, c1stat1c, c1stat2c, c1stat3c FROM school_events WHERE date=?""", (day,))
#     event = c.fetchall()
#     db.commit()
#     db.close()
    
#     print(event)
#     return event

def getDay(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT day FROM users WHERE user=?", (user,))
    day = c.fetchone()
    db.commit()
    db.close()

    return day[0]

def getGpa(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT gpa FROM users WHERE user=?", (user,))
    gpa = c.fetchone()
    db.commit()
    db.close()

    return gpa[0]

def addDay(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("UPDATE users SET day=? WHERE user=?", (getDay(user) + 1, user,))
    db.commit()
    db.close()
    