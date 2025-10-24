# app.py (repo root)
from flask import Flask, render_template

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.get("/")
def home():
    # if templates/index.html isn't there yet, just return a string
    return render_template("index.html")
    # or: return "Hello Timmy!"
