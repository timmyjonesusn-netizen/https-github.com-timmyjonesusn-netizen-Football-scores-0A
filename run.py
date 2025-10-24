# run.py  (repo root)
from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "TimmyApp is running ✅ from run.py"
