import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def init_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS userid (
        userid INTEGER NOT NULL UNIQUE
    )
    ''')
    conn.commit()

def getAllUsers():
    cursor.execute("SELECT * FROM userid")
    rows = cursor.fetchall()
    return [row[0] for row in rows]
    

def addUser(user_id: int):
    if user_id != user_id:
        cursor.execute("INSERT INTO userid (userid) VALUES (?)", (user_id,))
        conn.commit()
    else:
        print("error while request")

def getAllUsersAsNumber():
    cursor.execute("SELECT COUNT(*) AS total_rows FROM userid")
    rows = cursor.fetchall()
    return [row[0] for row in rows]

