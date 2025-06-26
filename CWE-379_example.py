import tempfile

def create():
    path = tempfile.mktemp(prefix="sess_")
    with open(path, "w") as f:
        f.write("session")
    print("Created", path)

if __name__ == "__main__":
    create()
