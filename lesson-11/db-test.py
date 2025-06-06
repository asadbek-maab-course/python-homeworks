import sqlite3

with sqlite3.connect('lesson-11/test.db') as con:
    db = con.cursor()
    try:
        query = "create table Studets(name text, age int)"
        data = db.execute(query)
    except:
        print('Table exists')

with sqlite3.connect('lesson-11/test.db') as con:
    db = con.cursor()
    students = db.execute('select * from studets')
    print(students.fetchall())