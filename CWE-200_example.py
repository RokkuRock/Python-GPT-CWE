# file: info_leak.py
def get_user_data():
    uid = input("User ID: ")
    try:
        with open(f"users/{uid}.txt") as f:
            print(f.read())
    except Exception as e:
        print("Error while accessing file:", e)  # CWE-200

if __name__ == "__main__":
    get_user_data()
