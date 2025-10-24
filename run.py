# run.py  — guaranteed boot
from flask import Flask

app = Flask(__name__)

@app.get("/")
def ping():
    return "TimmyApp: run.py minimal app is UP ✅"
