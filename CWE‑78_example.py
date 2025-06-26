# cmd_injection.py
import subprocess

def list_files():
    directory = input("Directory to list: ")
    # CWE-78: shell=True 且未清洗使用者輸入，可注入命令
    subprocess.run(f"ls {directory}", shell=True)

if __name__ == "__main__":
    list_files()
