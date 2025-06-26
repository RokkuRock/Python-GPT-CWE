# sql_search.py
import sqlite3

def search():
    term = input("Search product name contains: ")
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE products(name)")
    con.executemany("INSERT INTO products VALUES(?)", [("apple",),("banana",),("apricot",)])
    # CWE-89: f-string 直接拼接 user input → python/sql-injection
    q = f"SELECT name FROM products WHERE name LIKE '%{term}%'"
    print("Query:", q)
    for row in con.execute(q):
        print("Found:", row[0])

if __name__ == "__main__":
    search()
