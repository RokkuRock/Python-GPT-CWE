# temp_file.py
import tempfile

def create():
    # CWE-379: tempfile.mktemp 會產生可預測路徑
    path = tempfile.mktemp(prefix="sess_")
    with open(path, "w") as f:
        f.write("session")
    print("Created", path)

if __name__ == "__main__":
    create()
