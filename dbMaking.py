import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('Database\\attendance.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS attendance
             (date TEXT, roll_number TEXT, timestamp TEXT)''')

# Save (commit) the changes and close the connection
conn.commit()
conn.close()