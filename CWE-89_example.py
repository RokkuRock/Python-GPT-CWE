# sql_injection.py
import sqlite3

def vulnerable_login():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE admin(u, p)")
    conn.execute("INSERT INTO admin VALUES('root','toor')")
    user = input("Username: ")
    pwd  = input("Password: ")
    # CWE-89: 直接拼接使用者輸入到 SQL 字串
    query = f"SELECT * FROM admin WHERE u='{user}' AND p='{pwd}'"
    print("Executing:", query)
    cur = conn.execute(query)
    if cur.fetchone():
        print("Access granted")
    else:
        print("Access denied")

if __name__ == "__main__":
    vulnerable_login()
