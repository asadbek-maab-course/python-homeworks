import sqlite3
conn = sqlite3.connect("lesson-11/homework/library.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
""")

cur.executemany("INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)", [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
])

cur.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")

print("\nDystopian Books:")
for row in cur.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'"):
    print(row)

cur.execute("DELETE FROM Books WHERE Year_Published < 1950")

cur.execute("ALTER TABLE Books ADD COLUMN Rating REAL")

ratings = {
    "To Kill a Mockingbird": 4.8,
    "1984": 4.7,
    "The Great Gatsby": 4.5
}
for title, rating in ratings.items():
    cur.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (rating, title))

print("\nBooks sorted by Year Published:")
for row in cur.execute("SELECT Title, Year_Published FROM Books ORDER BY Year_Published ASC"):
    print(row)

conn.commit()
conn.close()
