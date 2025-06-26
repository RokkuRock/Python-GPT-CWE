# file_permissions.py
import os

def write_log():
    data = input("Log entry: ")
    # CWE-732: 建立檔案後未設置安全權限
    with open("app.log", "a") as f:
        f.write(data + "\n")
    # 預設權限可能對所有使用者讀寫
    print("Log written to app.log")

if __name__ == "__main__":
    write_log()
