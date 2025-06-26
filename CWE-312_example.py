# file: cleartext_storage.py
def store_secret():
    secret = input("Enter secret token: ")
    # CWE-312: 明文寫入
    with open('token.txt', 'w') as f:
        f.write(secret)
    print("Secret stored in token.txt")

if __name__ == "__main__":
    store_secret()
