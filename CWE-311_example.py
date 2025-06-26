# insecure_request.py
import requests

def fetch():
    url = input("Enter HTTPS URL: ")
    # CWE-311: verify=False 會跳過 SSL 憑證檢查
    r = requests.get(url, verify=False)
    print("Status code:", r.status_code)

if __name__ == "__main__":
    fetch()
