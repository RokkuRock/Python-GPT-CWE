# temp_file.py
import tempfile

def create_temp():
    # CWE-379: mktemp 生成可預測路徑
    path = tempfile.mktemp(prefix="tmpdata_")
    with open(path, "w") as f:
        f.write("temporary data")
    print("Wrote to", path)

if __name__ == "__main__":
    create_temp()
