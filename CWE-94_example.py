# code_injection.py
def run_user_code():
    src = input("Enter Python expression: ")
    # CWE-94: 未限制的 exec 執行
    exec(f"print({src})")

if __name__ == "__main__":
    run_user_code()
