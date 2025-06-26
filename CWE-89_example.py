# sql_injection.py
import sqlite3

def vulnerable_search():
    name = input("Search user by name: ")
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users(name, email)")
    conn.executemany("INSERT INTO users VALUES(?,?)", [
        ("alice","a@example.com"), ("bob","b@example.com")
    ])
    # CWE-89: 直接將使用者輸入串接到 SQL 字串
    query = f"SELECT email FROM users WHERE name = '{name}'"
    print("Executing:", query)
    for row in conn.execute(query):
        print(row[0])

if __name__ == "__main__":
    vulnerable_search()
