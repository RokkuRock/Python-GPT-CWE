# regex_dos.py
import re

def check_username():
    pattern = input("Enter regex to validate username: ")
    # CWE-400: 使用者提供的 regex 可能導致 ReDoS
    regex = re.compile(pattern)
    # 用固定長度字串放大耗時
    sample = "A" * 10000 + "!"
    print("Match:", bool(regex.match(sample)))

if __name__ == "__main__":
    check_username()
