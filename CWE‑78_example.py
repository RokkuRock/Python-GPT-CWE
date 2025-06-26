# cmd_injection.py
import subprocess

def delete_logs():
    days = input("Delete logs older than how many days? ")
    # CWE-78: shell=True 且未過濾 days，可能注入如 "0; rm -rf /tmp/*"
    subprocess.run(f"find /var/log -type f -mtime +{days} -delete", shell=True)

if __name__ == "__main__":
    delete_logs()
