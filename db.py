import sqlite3

def create_db():
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS positions(id INTEGER PRIMARY KEY AUTOINCREMENT, name text, posts text,description text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text,gender text,dob text,mobile text,doj text,city text,state text,position text,address text)")
    con.commit()

    con.close()

create_db()