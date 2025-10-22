from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# === SIMPLE, EDITABLE DATA (change any time) ===
DATA = {
    "site_title": "TimmyApp — Purple Core",
    "playlists": [
        # From your messages; add/remove as you like
        {"title": "Suno Playlist 1", "url": "https://suno.com/playlist/2ec04889-1c23-4e2d-9c27-8a2b6475da4b"},
        {"title": "Suno Playlist 2", "url": "https://suno.com/playlist/e95ddd12-7e37-43e2-b3e0-fe342085a19f"},
        {"title": "Suno Playlist 3", "url": "https://suno.com/playlist/2e2eefa6-6828-40ba-bf5b-02bf338e3243"},
        {"title": "Suno Creators 14-Track", "url": "https://suno.com/playlist/457d7e00-938e-4bf0-bd59-f070729200df"},
    ],
    "weather": {
        "location": "Ragland, AL",
        "hi_f": 82,
        "lo_f": 62,
        "wind_mph": 12,
        "warnings": False
    },
    "story": {
        "title": "Short Story of the Day",
        "text": "On a purple night in Ragland, a neon Yeti hummed along to Timmy’s playlist while bubbles drifted by. “C’est la vibe,” he whispered, and the town glowed.",
    },
    "events": [
        {"when": "Tonight 7:00 PM", "what": "Local Jam Session", "where": "Town Green"},
        {"when": "Fri 6:30 PM", "what": "Purple Devils vs Panthers", "where": "Ragland Stadium"},
    ],
    "idea": "Sticker-bombed QR benches: scan to hear a daily 10-sec ‘Good Vibes from Timmy’ + local sponsor shoutout. Simple, fun, viral.",
    "restaurant": {
        "name": "Southern Comfort Kitchen",
        "note": "#1 pick today — catfish, cornbread, and sweet tea done right."
    }
}

@app.route("/")
def home():
    return render_template("index.html", DATA=DATA)

@app.route("/music")
def music():
    return render_template("music.html", DATA=DATA)

@app.route("/weather", methods=["GET", "POST"])
def weather():
    # No API here (avoids deploy pain). You can update the numbers inline or via the form.
    if request.method == "POST":
        try:
            DATA["weather"]["location"] = request.form.get("location", DATA["weather"]["location"])
            DATA["weather"]["hi_f"] = int(request.form.get("hi_f", DATA["weather"]["hi_f"]))
            DATA["weather"]["lo_f"] = int(request.form.get("lo_f", DATA["weather"]["lo_f"]))
            DATA["weather"]["wind_mph"] = int(request.form.get("wind_mph", DATA["weather"]["wind_mph"]))
            DATA["weather"]["warnings"] = bool(request.form.get("warnings"))
        except:
            pass
        return redirect(url_for("weather"))
    return render_template("weather.html", DATA=DATA)

@app.route("/stories")
def stories():
    return render_template("stories.html", DATA=DATA)

@app.route("/idea")
def idea():
    return render_template("idea.html", DATA=DATA)

if __name__ == "__main__":
    # Local run: python app.py
    app.run(host="0.0.0.0", port=5000, debug=True)
