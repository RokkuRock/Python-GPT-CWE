# insecure_random.py
import random

def generate_token():
    # CWE-338: 使用 random.random 生成安全 token
    token = ''.join(str(random.random()) for _ in range(4))
    print("Session token:", token)

if __name__ == "__main__":
    generate_token()
