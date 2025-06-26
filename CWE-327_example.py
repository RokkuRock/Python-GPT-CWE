# weak_crypto.py
import hashlib

def sign():
    msg = input("Data: ")
    # CWE-327: MD5 雜湊已知不安全
    sig = hashlib.md5(msg.encode()).hexdigest()
    print("MD5:", sig)

if __name__ == "__main__":
    sign()
