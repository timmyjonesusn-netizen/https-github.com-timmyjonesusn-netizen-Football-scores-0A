# run.py (at repo root)
from flask import Flask

app = Flask(__name__)

@app.get("/")
def ping():
    return "ok"
