# sql_injection.py
import sqlite3

def search_products():
    term = input("Search product: ")
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE products(name, price)")
    conn.executemany("INSERT INTO products VALUES(?,?)", [
        ("apple", 10), ("banana", 5), ("pear", 7)
    ])
    # CWE-89: 直接拼接 user input 到 SQL 字串
    query = f"SELECT * FROM products WHERE name LIKE '%{term}%'"
    print("Running:", query)
    for row in conn.execute(query):
        print(row)

if __name__ == "__main__":
    search_products()
