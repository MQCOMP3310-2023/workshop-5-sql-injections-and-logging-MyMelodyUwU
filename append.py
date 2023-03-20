import sqlite3
conn = sqlite3.connect('./sqlite/words.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS words (word TEXT)')

with open('./resources/data.txt') as file:
    words = file.readlines()

for word in words:
    c.execute('INSERT INTO words VALUES (?)', (word.strip(),))

conn.commit()
conn.close()
