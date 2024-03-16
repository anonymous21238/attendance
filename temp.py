import sqlite3

conn = sqlite3.connect('Database\\attendance.db')

command = "select * from attendance"
result = conn.execute(command)
print(result)
for i in result:
    print(i)