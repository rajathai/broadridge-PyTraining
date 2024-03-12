import sqlite3

# Connect to SQLite Database
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

# Create table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
)
"""
)

conn.commit()
conn.close()
