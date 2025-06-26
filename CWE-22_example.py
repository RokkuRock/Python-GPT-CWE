# path_traversal.py
def read_data():
    filename = input("Filename under data/: ")
    # CWE-22: 未過濾 '../'，可讀取任意檔案
    with open(f"data/{filename}", 'r') as f:
        print(f.read())

if __name__ == "__main__":
    read_data()
