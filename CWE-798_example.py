# hardcoded_credentials.py
def login():
    # CWE-798: 程式內直接寫死帳號與密碼
    USER = "admin"
    PASS = "S3cr3t!"
    user = input("User: ")
    passwd = input("Pass: ")
    if user == USER and passwd == PASS:
        print("Welcome admin")
    else:
        print("Authentication failed")

if __name__ == "__main__":
    login()
