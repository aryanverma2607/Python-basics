import sqlite3
cursor=sqlite3.connect("Connection.db")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

cursor.execute(
    "INSERT INTO students VALUES(?,?,?,?)",
    (1,"Aryan",20,"CSE")
)
cursor.commit()

cursor.execute("SELECT * FROM students")

data = cursor.fetchone()

print(data)

cursor.close()

