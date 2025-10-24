from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html")  # or just "Hello, Timmy!"

    return app   # <-- THIS LINE IS REQUIRED
