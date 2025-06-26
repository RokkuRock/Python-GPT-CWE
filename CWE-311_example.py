# insecure_request.py
import requests

def fetch():
    url = input("Enter HTTPS URL: ")
    r = requests.get(url, verify=False)
    print("Status code:", r.status_code)

if __name__ == "__main__":
    fetch()
