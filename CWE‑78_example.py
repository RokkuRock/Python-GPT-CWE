# cmd_injection.py
import subprocess

def list_directory():
    # 從使用者讀入目錄名稱
    folder = input("Folder to list: ")
    # CWE-78: 使用 shell=True 且直接拼接使用者輸入
    subprocess.run(f"ls {folder}", shell=True)

if __name__ == "__main__":
    list_directory()
