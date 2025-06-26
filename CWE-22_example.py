# file: path_traversal.py
def read_file():
    fn = input("Filename under data/: ")
    # CWE-22: 未過濾 ../
    with open(f"data/{fn}", 'r') as f:
        print(f.read())

if __name__ == "__main__":
    read_file()
