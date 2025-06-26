# sql_injection.py
import sqlite3

def find_customer():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE customers(id, name)")
    conn.executemany("INSERT INTO customers VALUES(?,?)", [(1,"Alice"),(2,"Bob")])
    term = input("Search name: ")
    # CWE-89: 直接拼接 user input
    query = f"SELECT id FROM customers WHERE name = '{term}'"
    print("Running:", query)
    for r in conn.execute(query):
        print("Found ID:", r[0])

if __name__ == "__main__":
    find_customer()
