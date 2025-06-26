# hardcoded_creds.py
def login():
    # CWE-798: 程式內硬編 user/pass
    USER = "admin"
    PASS = "P@ssw0rd"
    u = input("User: ")
    p = input("Pass: ")
    if u == USER and p == PASS:
        print("Welcome")
    else:
        print("Denied")

if __name__ == "__main__":
    login()
