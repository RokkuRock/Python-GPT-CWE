# file: xss.py
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    msg = request.args.get('msg', '')
    return f"<h1>Your message: {msg}</h1>"  # CWE-79: 任意 HTML 輸出

if __name__ == "__main__":
    app.run(port=5000)
