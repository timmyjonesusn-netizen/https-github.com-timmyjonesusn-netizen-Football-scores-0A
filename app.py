from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("home.html", title="Timmyapp")

    # keep your other endpoints if you have them:
    @app.route("/music")
    def music():
        return "<h1>Music</h1><p>Wire this later.</p>"

    @app.route("/weather")
    def weather():
        return "<h1>Weather</h1><p>Wire this later.</p>"

    @app.route("/pemdas")
    def pemdas():
        return "<h1>PEMDAS</h1>"

    @app.route("/riddle")
    def riddle():
        return "<h1>Riddle</h1>"

    @app.route("/police")
    def police():
        return "<h1>Police</h1>"

    return app

# Render/Gunicorn entry point
app = create_app()
