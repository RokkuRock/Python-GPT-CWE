# ssti.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    tpl = request.args.get("tpl", "")
    # CWE-94: 未淨化直接渲染使用者提供的 template
    return render_template_string(tpl)

if __name__ == "__main__":
    app.run(port=5003)
