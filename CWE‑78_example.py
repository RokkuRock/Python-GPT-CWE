# file: cmd_injection.py
import os

def list_dir():
    path = input("Directory to list: ")
    os.system(f"ls {path}")  # CWE-78: 任意 shell 指令注入

if __name__ == "__main__":
    list_dir()
