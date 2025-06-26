# sql_injection.py
import sqlite3

def login():
    conn = sqlite3.connect(':memory:')
    conn.execute("CREATE TABLE users(name, pwd)")
    conn.execute("INSERT INTO users VALUES('admin','secret')")
    user = input("Username: ")
    pwd  = input("Password: ")
    # CWE-89: 直接拼接字串查詢
    query = f"SELECT * FROM users WHERE name = '{user}' AND pwd = '{pwd}'"
    print("Query:", query)
    cur = conn.execute(query)
    print("Login successful" if cur.fetchone() else "Login failed")

if __name__ == "__main__":
    login()
