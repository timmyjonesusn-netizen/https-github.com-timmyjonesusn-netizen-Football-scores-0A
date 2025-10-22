from flask import Flask, render_template

app = Flask(__name__)

# ---------- Helpers ----------
def compute_alert(weather):
    """
    Return ('none'|'yellow'|'red', message)
    yellow: wind >= 25 mph
    red:    wind >= 40 mph OR has 'warning' text
    """
    wind = (weather or {}).get("wind_mph", 0) or 0
    warning = (weather or {}).get("warning")
    if warning or wind >= 40:
        return "red", (warning or "High winds detected")
    if wind >= 25:
        return "yellow", "Breezy conditions"
    return "none", "All clear"

# ---------- Routes ----------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather")
def weather_page():
    # 🔒 Safe fallback data so the page never 500s
    weather = {
        "location": "Ragland, AL",
        "temp_f": 76,
        "hi_f": 81,
        "lo_f": 61,
        "condition": "Clear Skies",
        "wind_mph": 12,
        "warning": None,   # e.g., "Severe Thunderstorm Watch"
    }
    alert_level, alert_msg = compute_alert(weather)
    return render_template(
        "weather.html",
        weather=weather,
        alert_level=alert_level,
        alert_msg=alert_msg,
    )

@app.route("/music")
def music_page():
    # Links from your earlier notes
    playlists = [
        {
            "title": "Creators Pack • 14 tracks",
            "url": "https://suno.com/playlist/457d7e00-938e-4bf0-bd59-f070729200df",
            "note": "Royalty-free vibe beds (no copyright strikes)."
        },
        {
            "title": "Playlist 2",
            "url": "https://suno.com/playlist/2ec04889-1c23-4e2d-9c27-8a2b6475da4b",
            "note": "Chill backgrounds for voiceover."
        },
        {
            "title": "Playlist 3",
            "url": "https://suno.com/playlist/e95ddd12-7e37-43e2-b3e0-fe342085a19f",
            "note": "Upbeat reels & scene cuts."
        },
        {
            "title": "Playlist 4",
            "url": "https://suno.com/playlist/2e2eefa6-6828-40ba-bf5b-02bf338e3243",
            "note": "Ambient & motion graphics."
        },
    ]
    return render_template("music.html", playlists=playlists)

# Optional: simple /health endpoint Render likes
@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
