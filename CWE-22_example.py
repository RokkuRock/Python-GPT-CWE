# view_report.py
import os

def show_report():
    fname = input("Report filename (in reports/): ")
    # CWE-22: 未過濾 '../' → python/path-traversal
    path = os.path.join("reports", fname)
    with open(path, 'r') as f:
        print(f.read())

if __name__ == "__main__":
    show_report()
