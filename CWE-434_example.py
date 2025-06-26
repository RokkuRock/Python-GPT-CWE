# file_upload.py
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    # CWE-434: 未檢查檔案名稱或類型，任意檔案皆可上傳
    path = os.path.join('uploads', f.filename)
    f.save(path)
    return f"Saved {path}"

if __name__ == "__main__":
    os.makedirs('uploads', exist_ok=True)
    app.run(port=5004)
