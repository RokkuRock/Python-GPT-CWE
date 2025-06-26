# insecure_perms.py
import os

def write_log():
    entry = input("Log entry: ")
    # CWE-732: open 後未設置安全模式，預設可能全員皆可讀寫
    with open("app.log", "a") as f:
        f.write(entry + "\n")
    print("Logged")

if __name__ == "__main__":
    write_log()
