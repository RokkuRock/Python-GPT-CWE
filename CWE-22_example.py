# path_traversal_server.py
from flask import Flask, request, send_file, abort
import os

app = Flask(__name__)

@app.route("/download")
def download():
    fname = request.args.get("file", "")
    path = os.path.join("uploads", fname)
    if not os.path.isfile(path):
        abort(404)
    return send_file(path)

if __name__ == "__main__":
    app.run(port=5001)
