from flask import Flask, render_template, request
from config import Config

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(Config)

    @app.context_processor
    def inject_globals():
        # Share version for cache-busting CSS
        return {"APP_VERSION": app.config.get("APP_VERSION", "1.0.0")}

    @app.route("/")
    def home():
        return render_template("home.html", title="TimmyApp — Home")

    @app.route("/weather")
    def weather():
        # Simple server-side values; tweak via query for quick tests:
        # /weather?wind=27&alert=false
        wind = int(request.args.get("wind", "8"))
        has_alert = request.args.get("alert", "false").lower() in ("1", "true", "yes", "y")
        weather = {"wind_mph": wind, "has_alert": has_alert}
        return render_template("weather.html", title="Weather", weather=weather)

    @app.route("/music")
    def music():
        # Five working music links (Suno playlists)
        playlists = [
            {"title": "Creator Flow Vol. 1", "url": "https://suno.com/playlist/457d7e00-938e-4bf0-bd59-f070729200df"},
            {"title": "Creator Flow Vol. 2", "url": "https://suno.com/playlist/2ec04889-1c23-4e2d-9c27-8a2b6475da4b"},
            {"title": "Royalty-Friendly Pack", "url": "https://suno.com/playlist/06b80fa9-8c72-4e0a-b277-88d00c441316"},
            {"title": "Background Vibes", "url": "https://suno.com/playlist/e95ddd12-7e37-43e2-b3e0-fe342085a19f"},
            {"title": "Creator 14-Pack", "url": "https://suno.com/playlist/2e2eefa6-6828-40ba-bf5b-02bf338e3243"},
        ]
        note = "Redirects to Suno — 14-song playlist especially for creators (royalty-friendly background music)."
        return render_template("music.html", title="Music", playlists=playlists, note=note)

    @app.route("/story")
    def story():
        sample = (
            "They said the river kept secrets. That night it kept time too — one, two, flash. "
            "The wind teased the banners, and Timmy spotted a smear of purple chalk on the press box knob. "
            "“Follow the bassline,” it said — and he did."
        )
        return render_template("story.html", title="Story", text=sample)

    return app
