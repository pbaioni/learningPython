import sqlite3

conn = None
cursor = None

def connect(dbName):
    try:
        global conn 
        conn = sqlite3.connect(dbName)
        global cursor
        cursor = conn.cursor()
        print 'database', dbName, 'connected'
    except Exception as e:
        print 'Erreur while connecting to database\n', e
        conn.rollback()
        
def disconnect():
    try:
        conn.close()
        print 'database disconnected'
    except Exception as e:
        print 'Erreur while disconnecting from database\n', e
        conn.rollback()

def executeCommand(cmd):
    try:
        cursor.execute(cmd)
        conn.commit()
        print 'command executed:', cmd
        return cursor
    except Exception as e:
        print 'Erreur while executing command', cmd, '\n', e
        conn.rollback()
        
def createUserTable():
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,name TEXT,age INTERGER)""")
        conn.commit()
        print 'Users table created'
    except Exception as e:
        print 'Erreur while creating user table'
        conn.rollback()
        
def dropUserTable():
    try:
        cursor.execute("""DROP TABLE users""")
        conn.commit()
        print 'Users table dropped'
    except Exception as e:
        print 'Erreur while dropping user table'
        conn.rollback()
        
def insertUser(name, age):
    try:
        cursor.execute("""INSERT INTO users(name, age) VALUES(?, ?)""", (name, age))
        conn.commit()
        print 'User inserted:', name, age 
    except Exception as e:
        print 'Erreur while inserting user', name, age, '\n', e
        conn.rollback()