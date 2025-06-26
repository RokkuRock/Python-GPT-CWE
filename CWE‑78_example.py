# cmd_injection.py
import subprocess

def remove_old_logs():
    days = input("Delete logs older than how many days? ")
    # CWE-78: shell=True 且未清洗使用者輸入 → python/command-injection
    subprocess.run(f"find /var/log -mtime +{days} -delete", shell=True)

if __name__ == "__main__":
    remove_old_logs()
