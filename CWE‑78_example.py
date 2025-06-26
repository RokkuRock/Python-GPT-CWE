# file: cmd_injection.py
import subprocess

def list_dir():
    path = input("Directory to list: ")
    # CWE-78: shell=True + 未清洗輸入
    subprocess.call(f"ls {path}", shell=True)

if __name__ == "__main__":
    list_dir()
