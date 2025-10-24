from flask import Flask, render_template

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.get("/")
def home():
    # If you don't have templates/index.html yet, use: return "Hello Timmy!"
    return render_template("index.html")
