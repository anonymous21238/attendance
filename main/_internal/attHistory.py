import sqlite3
import pandas as pd

roll = int(input("Enter your roll number: "))

# conn = sqlite3.connect('Database\\attendance.db')
conn = sqlite3.connect('attendance.db')
command = f"select date, timestamp from attendance WHERE roll_number = {roll} ORDER BY date DESC"
result = conn.execute(command)
data = result.fetchall()
conn.close()

df = pd.DataFrame(data, columns = ['Date', 'Timestamp'])
print(df)