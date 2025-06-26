# file_permissions.py
import os

def log_event():
    msg = input("Log message: ")
    # CWE-732: 建立後未設定權限，預設可能過度開放
    path = "event.log"
    with open(path, "a") as f:
        f.write(msg + "\n")
    # CodeQL 可偵測到未限制權限的檔案操作
    print("Logged to", path)

if __name__ == "__main__":
    log_event()
