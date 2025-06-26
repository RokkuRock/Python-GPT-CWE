# template_injection.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    # CWE-94: render_template_string 直接以 user 提交的 template，CodeQL 會抓到
    tpl = request.args.get("tpl", "")
    return render_template_string(tpl)

if __name__ == "__main__":
    # 僅監聽本機，無外部依賴
    app.run(port=5000)
