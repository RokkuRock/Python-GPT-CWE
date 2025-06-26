# insecure_perms.py
import os

def dump_debug():
    info = input("Debug info: ")
    # CWE-732: open 後未設置安全權限 → python/insecure-file-permissions
    with open("debug.log", "a") as f:
        f.write(info + "\n")
    # 預設權限可能過度開放
    print("Wrote to debug.log")

if __name__ == "__main__":
    dump_debug()
