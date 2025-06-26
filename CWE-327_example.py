# weak_crypto.py
import hashlib

def sign_data():
    data = input("Data to sign: ")
    # CWE-327: 使用 MD5 而非安全雜湊 → python/weak-crypto
    sig = hashlib.md5(data.encode()).hexdigest()
    print("MD5 signature:", sig)

if __name__ == "__main__":
    sign_data()
