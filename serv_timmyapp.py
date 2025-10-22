# serv_timmyapp.py
from flask import Flask, render_template, url_for
import os

APP_NAME = "TimmyApp"

def create_app():
    app = Flask(__name__, static_folder="static", static_url_path="/static", template_folder="templates")

    # ---- Routes ----
    @app.route("/")
    def home():
        return render_template("home.html", title="Home")

    @app.route("/ideas")
    def ideas():
        return render_template("ideas.html", title="Ideas")

    @app.route("/bubbles")
    def bubbles():
        # same look as home, just shows the bubbles full-screen
        return render_template("bubbles.html", title="Bubbles")

    @app.route("/music")
    def music():
        # embeds your Suno playlist link
        return render_template("music.html", title="Music")

    @app.route("/police")
    def police():
        return render_template("police.html", title="Police Corner")

    @app.route("/tickle")
    def tickle():
        return render_template("tickle.html", title="Daily Tickle")

    @app.route("/riddles")
    def riddles():
        return render_template("riddles.html", title="Riddles & Whodunnit")

    @app.route("/weather")
    def weather():
        # simple placeholder page (we can wire API after colors are locked)
        return render_template("weather.html", title="Weather")

    return app
