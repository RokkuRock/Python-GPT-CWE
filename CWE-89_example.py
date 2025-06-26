# file: sql_injection.py
import sqlite3

def login():
    conn = sqlite3.connect(':memory:')
    conn.execute("CREATE TABLE users(u,p)")
    conn.execute("INSERT INTO users VALUES('admin','secret')")
    u = input("Username: ")
    p = input("Password: ")
    q = f"SELECT * FROM users WHERE u='{u}' AND p='{p}'"  # CWE-89
    print("SQL:", q)
    cur = conn.execute(q)
    if cur.fetchone():
        print("Login successful")
    else:
        print("Login failed")
    conn.close()

if __name__ == "__main__":
    login()
