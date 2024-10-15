import sqlite3

conn = sqlite3.connect("not_telegram.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age NUMBER,
    balance INTEGER NOT NULL
    )
''')

for i in range(10):
    cursor.execute('''INSERT OR REPLACE INTO Users (id, username, email, age, balance) VALUES(?, ?, ?, ?, ?)''',
                   (i+1, f"User{i+1}", f"example{i+1}@gmail.com", f"{(i+1)*10}", f"1000"))

for i in range(10):
    if i % 2 == 0:
        cursor.execute('''UPDATE Users SET balance = 500 WHERE id = ?''',(i+1,))

for i in range(10):
    if i % 3 == 0:
        cursor.execute('''DELETE FROM Users WHERE id = ?''',(i+1,))

cursor.execute("""SELECT id, username, email, age, balance FROM Users WHERE age <> 60""")

for r in cursor.fetchall():
    print(f"Имя: {r[1]} | Почта: {r[2]} | Возраст: {r[3]} | Баланс: {r[4]}")

conn.commit()
conn.close()
