# sql_injection.py
import sqlite3

def search_users():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users(name, email)")
    conn.executemany("INSERT INTO users VALUES(?,?)", [
        ("alice","a@x.com"),("bob","b@x.com")
    ])
    term = input("Search name: ")
    # CWE-89: 直接拼接 user 輸入
    query = f"SELECT * FROM users WHERE name LIKE '%{term}%'"
    print("Running:", query)
    for row in conn.execute(query):
        print(row)

if __name__ == "__main__":
    search_users()
