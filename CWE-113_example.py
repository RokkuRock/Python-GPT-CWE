# header_injection.py
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/setcookie')
def setcookie():
    user = request.args.get('user', '')
    # CWE-113: 直接將 user input 寫入 header，可能注入 CRLF
    resp = Response("Cookie set")
    resp.headers['Set-Cookie'] = f"user={user}"
    return resp

if __name__ == "__main__":
    app.run(port=5005)
