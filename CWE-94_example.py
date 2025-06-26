# ssti.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    tpl = request.args.get("tpl", "")
    return render_template_string(tpl)

if __name__ == "__main__":
    app.run(port=5003)
