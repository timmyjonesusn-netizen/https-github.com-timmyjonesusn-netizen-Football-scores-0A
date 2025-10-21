# serv_timmyapp.py
from flask import Flask, render_template

def create_app():
    app = Flask(__name__, static_folder="static", static_url_path="/static")

    @app.route("/")
    def home():
        return render_template("index.html", page_title="Welcome to TimmyApp")

    @app.route("/ideas")
    def ideas():
        return render_template("stub.html", page_title="Ideas")

    @app.route("/bubbles")
    def bubbles():
        return render_template("stub.html", page_title="Timmy Bubbles")

    @app.route("/music")
    def music():
        return render_template("music.html", page_title="TimmyTunes")

    @app.route("/police")
    def police():
        return render_template("stub.html", page_title="Police Corner")

    @app.route("/tickle")i
    def tickle():
        return render_template("stub.html", page_title="Daily Tickle")

    @app.route("/riddles")
    def riddles():
        return render_template("stub.html", page_title="Riddles")

    @app.route("/weather")
    def weather():
        return render_template("stub.html", page_title="Weather")

    return app
