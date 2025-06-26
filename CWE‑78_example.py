# cmd_injection.py
import subprocess

def list_dir():
    folder = input("Folder to list: ")
    # CWE-78: shell=True 且未清洗輸入，會被 CodeQL 偵測
    subprocess.Popen(f"ls {folder}", shell=True)

if __name__ == "__main__":
    list_dir()
