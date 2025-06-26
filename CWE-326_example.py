# weak_crypto.py
import hashlib

def sign():
    data = input("Data: ")
    # CWE-326: 使用 MD5 而非更安全的 SHA-2/3
    sig = hashlib.md5(data.encode()).hexdigest()
    print("MD5 Sig:", sig)

if __name__ == "__main__":
    sign()
