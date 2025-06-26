# file: sql_injection.py
import sqlite3

def login():
    conn = sqlite3.connect(':memory:')
    conn.execute("CREATE TABLE users(u, p)")
    conn.execute("INSERT INTO users VALUES('admin','secret')")
    u = input("User: ")
    p = input("Pass: ")
    # CWE-89: 直接拼接輸入
    q = f"SELECT * FROM users WHERE u = '{u}' AND p = '{p}'"
    print("Query:", q)
    cur = conn.execute(q)
    print("Login successful" if cur.fetchone() else "Login failed")

if __name__ == "__main__":
    login()
