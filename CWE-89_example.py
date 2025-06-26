# sql_injection.py
import sqlite3

def add_and_search():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE items(id INTEGER, name TEXT)")
    conn.executemany("INSERT INTO items VALUES(?,?)", [(1,"apple"),(2,"banana")])
    name = input("Search item name: ")
    # CWE-89: 直接拼接使用者輸入到查詢字串
    q = f"SELECT id FROM items WHERE name = '{name}'"
    print("Running:", q)
    for row in conn.execute(q):
        print("Found ID:", row[0])

if __name__ == "__main__":
    add_and_search()
