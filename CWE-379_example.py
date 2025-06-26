# temp_file.py
import tempfile

def create_temp():
    # CWE-379: tempfile.mktemp 產生可預測路徑，CodeQL 可報警
    path = tempfile.mktemp(prefix="data_")
    with open(path, "w") as f:
        f.write("temporary")
    print("Wrote to", path)

if __name__ == "__main__":
    create_temp()
