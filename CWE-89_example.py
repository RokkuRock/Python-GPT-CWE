# sql_injection.py
import sqlite3

def find_user():
    term = input("Search username substring: ")
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users(name)")
    conn.executemany("INSERT INTO users VALUES(?)", [("alice",),("bob",)])
    # CWE-89: 直接使用 f-string 串接，CodeQL 可偵測
    q = f"SELECT name FROM users WHERE name LIKE '%{term}%'"
    for row in conn.execute(q):
        print("Found:", row[0])

if __name__ == "__main__":
    find_user()
