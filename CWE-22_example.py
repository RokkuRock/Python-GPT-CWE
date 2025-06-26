# file: path_traversal.py
def read_file():
    fn = input("Filename in safe/ to read: ")
    path = f"safe/{fn}"
    with open(path, 'r') as f:
        print("Content:", f.read())

if __name__ == "__main__":
    read_file()
