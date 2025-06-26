# ssrf.py
import requests

def fetch_url():
    url = input("Enter URL to fetch: ")
    # CWE-918: 未限制的外部 URL 請求
    r = requests.get(url)
    print("Status code:", r.status_code)

if __name__ == "__main__":
    fetch_url()
