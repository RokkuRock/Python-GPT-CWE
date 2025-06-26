# weak_crypto.py
import hashlib

def sign():
    data = input("Data to sign: ")
    # CWE-326: 使用 MD5 作為訊息摘要，已知不安全
    sig = hashlib.md5(data.encode()).hexdigest()
    print("Signature (MD5):", sig)

if __name__ == "__main__":
    sign()
