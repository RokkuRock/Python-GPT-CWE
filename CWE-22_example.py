# path_traversal.py
import os

def read_report():
    name = input("Report name (in reports/): ")
    # CWE-22: 未過濾 ../，可跳脫到任意路徑
    path = os.path.join("reports", name)
    with open(path, "r") as f:
        print(f.read())

if __name__ == "__main__":
    read_report()
