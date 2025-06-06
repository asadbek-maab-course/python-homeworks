import sqlite3
with sqlite3.connect('lesson-11/homework/roster.db') as conn:
    db = conn.cursor()
    try:
        query = "create table Roster(name text, species text, age int)"
        db.execute(query)
    except:
        pass
    query = "insert into Roster (name, species, age) values ('Benjamin Sisko', 'Human', 40), ('Jadzia Dax', 'Trill', 300), ('Kira Neyrs', 'Bajoran', 29)"
    db.execute(query)

    query = "update Roster set name='Ezri Dax' where name='Jadzia Dax'"
    db.execute(query)
    print("Bajoran Characters:")
    for row in db.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'"):
        print(row)
    for row in db.execute("SELECT Name, Age FROM Roster ORDER BY Age DESC"):
        print(row)




