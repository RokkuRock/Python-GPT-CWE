# cmd_injection.py
import os

def delete_tmp():
    days = input("Delete /tmp files older than how many days? ")
    # CWE-78: shell=True 與 os.system 直接拼接使用者輸入
    os.system(f"find /tmp -mtime +{days} -delete")

if __name__ == "__main__":
    delete_tmp()
