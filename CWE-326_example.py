# weak_crypto.py
import hashlib

def sign_data():
    data = input("Data to sign: ")
    # CWE-326: 使用 MD5 作為雜湊演算法
    h = hashlib.md5(data.encode()).hexdigest()
    print("MD5:", h)

if __name__ == "__main__":
    sign_data()
