# ==========================================
# 🚀 TIMMYAPP: BELLS & WHISTLES ENGINE CORE
# ==========================================

import os
from flask import Flask, render_template

app = Flask(__name__)

# -------- ROUTES -------- #

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ideas")
def ideas():
    return render_template("ideas.html")

@app.route("/bibles")
def bibles():
    return render_template("bibles.html")

@app.route("/music")
def music():
    return render_template("music.html")

@app.route("/police")
def police():
    return render_template("police.html")

@app.route("/tickle")
def tickle():
    return render_template("tickle.html")

@app.route("/weather")
def weather():
    return render_template("weather.html")

@app.route("/riddles")
def riddles():
    return render_template("riddles.html")

# -------- SAFETY / DEFAULT -------- #
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Reggie lost this page chasing a mail truck.</p>", 404


# -------- LAUNCH CONFIG -------- #
if __name__ == "__main__":
    # Render-safe dynamic port
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
