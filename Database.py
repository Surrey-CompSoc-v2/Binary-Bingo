import sqlite3

# Connect to (or create) a database file
conn = sqlite3.connect("bingo.db")

# Create a cursor to interact with the database
cursor = conn.cursor()

cursor.execute("""
DROP TABLE IF EXISTS events;
               """
               )

# Create a table for bingo events
cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_number INTEGER NOT NULL,
    challenge TEXT,
    used BOLEAN DEFAULT F
);
""")

# Example: inserting a few challenges
challenges = [
    (1, "First person to MOOOOOO gets a sweet!"),
    (2, "First person to hand the treasurer a sock gets a sweet!"),
    (3, "First person to call out the first 3 numbers of the game gets a sweet!"),
    (4, "SWITCH CARDS!"),
    (5, "Surprise! We need 3 volunteers..."),
    (6, "SWITCH CARDS!"),
    (7, "Whoever can hold up the strangest object gets a sweet."),
    (8, "If your number comes up next, you get a sweet!"),
    (9, "Whoever can hold up the largest amount of cash/coins gets a sweet."),
    (10, "Boo Zoe for removing the number 67 from the game :(")
    (11, "Stand up if you have the number 20 on your card.")
]

cursor.executemany("INSERT INTO events (event_number, challenge) VALUES (?, ?);", challenges)

# Save (commit) the changes
conn.commit()

# Retrieve and print all challenges
cursor.execute("SELECT * FROM events;")
for row in cursor.fetchall():
    print(row)

# Always close when done
conn.close()
