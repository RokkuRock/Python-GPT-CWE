def store_api_key():
    key = input("Enter API key: ")
    with open("config.txt", "w") as f:
        f.write(f"api_key={key}\n")
    print("Key saved to config.txt")

if __name__ == "__main__":
    store_api_key()
