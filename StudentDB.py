import sqlite3
connection = sqlite3.connect("student_detials.db")
print("Database opened successfully")
cursor = connection.cursor()
#delete
#cursor.execute('''DROP TABLE Student_Info;''')
connection.execute("create table Student_Info (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, gender TEXT NOT NULL, contact TEXT UNIQUE NOT NULL, dob TEXT NOT NULL, address TEXT NOT NULL)")
print("Table created successfully")
connection.close()   
