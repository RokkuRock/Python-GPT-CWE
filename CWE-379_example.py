# temp_file.py
import tempfile

def create_temp():
    # CWE-379: 使用 mktemp 會產生可預測路徑
    path = tempfile.mktemp(prefix="session_")
    with open(path, "w") as f:
        f.write("session data")
    print("Wrote to", path)

if __name__ == "__main__":
    create_temp()
