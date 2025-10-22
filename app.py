# app.py — TimmyApp full load (glow + bubbles + music + mini weather strip + weather page with wind lights + riddles + daily story)
import os, sys, json, traceback, math, hashlib
from datetime import datetime, date
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# ------------------- Config -------------------
APP_NAME = "TimmyApp"
TIMEZONE = "America/New_York"

# Ragland, AL approx (not displayed)
RAGLAND_LAT = 33.744
RAGLAND_LON = -86.153

# Your Suno playlists — 3 confirmed + 2 placeholders you can swap anytime
MUSIC_LINKS = [
    ("Creator Flow Vol. 1", "Royalty-friendly for Reels/Shorts.", "https://suno.com/playlist/2ec04889-1c23-4e2d-9c27-8a2b6475da4b"),
    ("Dream Beats", "Ambient uplift for smooth edits.", "https://suno.com/playlist/e95ddd12-7e37-43e2-b3e0-fe342085a19f"),
    ("Vibe Factory", "Clean hooks, safe to use.", "https://suno.com/playlist/2e2eefa6-6828-40ba-bf5b-02bf338e3243"),
    ("Cinematic Loops", "Coming online today.", "#"),
    ("Hometown Bounce", "Coming online today.", "#"),
]

# ------------------- Daily content helpers (no DB) -------------------
RIDDLES = [
    ("What has many keys but can’t open a single lock?", "A piano."),
    ("I speak without a mouth and hear without ears. What am I?", "An echo."),
    ("What can travel around the world while staying in a corner?", "A stamp."),
    ("What has hands but can’t clap?", "A clock."),
    ("The more of this there is, the less you see. What is it?", "Darkness."),
    ("What has one eye but cannot see?", "A needle."),
    ("What goes up but never comes down?", "Your age."),
    ("What gets wetter the more it dries?", "A towel."),
]

STORIES = [
    # ~150 words with a touch of French each, neon vibe micro-stories
    "The fog slid across Ten Islands like velvet, and the scoreboard blinked once—violet, then still. "
    "“Tu le vois?” Timmy whispered. A shimmer answered from the press box glass, a tiny glyph pulsing like a heartbeat. "
    "C’était la petite étincelle—the little spark—guiding him past the bleachers to the old Fort Strother marker. "
    "There, a scuffed whistle and purple dust traced a path toward the riverlights. The clue wasn’t loud; it glowed. "
    "By sunrise, fingerprints—just a breath of neon—told the rest.",

    "Midnight found Ragland quiet, except the soft hum in the field lights. "
    "Timmy followed a thread of violet footprints to a note: “Cherche la lumière”—seek the light. "
    "He turned and saw it: tiny bubbles of glow drifting above the fifty-yard line. "
    "They weren’t floating up; they were pointing the way. He grinned. "
    "If it’s not glowing, it’s not going. The town would wake to a solved mystery and a brighter scoreboard.",

    "They said the river kept secrets. That night it kept time, too—one, two, flash. "
    "“Bonsoir,” the wind teased, rustling the banners. Timmy spotted a smear of purple chalk on the press box knob. "
    "Pas un hasard—not an accident. He traced it to a small tin whistle and a scribble, "
    "‘Follow the bassline.’ He did, and the path lit like a dance floor to the old marker, where the last clue waited.",

    "The bleachers sighed as the fog curled low. “Regarde,” Timmy said, pointing where the turf shimmered. "
    "A single neon dot pulsed, then a trail of them, like crumbs of light. "
    "Petit à petit—little by little—they made an arrow toward the river. "
    "The whistle, the dust, the glyphs: none louder than a whisper, all bright as homecoming. "
    "Some truths don’t shout; they glow.",

    "Lightning far off, but the field stayed calm. A gentle pink halo touched the scorer’s box. "
    "C’est par ici—this way—someone had scrawled in faint chalk. "
    "Timmy followed until the ground sang underfoot, a soft hum like a bass drop. "
    "At the marker he found the final note: ‘You found the beat.’ "
    "And in the morning, the town found the glow."
]

def _day_index(n):
    # deterministic rotation by current date in ET
    today = datetime.now().astimezone().date()
    return int(hashlib.md5(str(today).encode()).hexdigest(), 16) % max(1, n)

def get_daily_riddle():
    i = _day_index(len(RIDDLES))
    return RIDDLES[i]

def get_daily_story():
    i = _day_index(len(STORIES))
    return STORIES[i]

# ------------------- Weather + Wind Light -------------------
SEVERE_CODES = {95, 96, 99}  # thunderstorm codes (Open-Meteo WMO)
def fetch_weather():
    """
    Returns dict:
    {
      temp, feels_like, wind, code, code_text, hi, lo, time, place, light ('off'|'yellow'|'red'), light_msg
    }
    """
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={RAGLAND_LAT}&longitude={RAGLAND_LON}"
        "&current=temperature_2m,apparent_temperature,wind_speed_10m,weather_code"
        "&daily=temperature_2m_max,temperature_2m_min,wind_speed_10m_max,weather_code"
        f"&temperature_unit=fahrenheit&wind_speed_unit=mph&timezone={TIMEZONE}"
    )
    try:
        r = requests.get(url, timeout=8)
        data = r.json()
        cur = data.get("current", {})
        daily = data.get("daily", {})

        temp = round(cur.get("temperature_2m", 0))
        feels = round(cur.get("apparent_temperature", 0))
        wind = round(cur.get("wind_speed_10m", 0))
        code = int(cur.get("weather_code", 0))
        hi = round((daily.get("temperature_2m_max") or [temp])[0])
        lo = round((daily.get("temperature_2m_min") or [temp])[0])
        daily_wind_max = round((daily.get("wind_speed_10m_max") or [wind])[0])
        tstamp = cur.get("time", "")

        # condition text (simple map)
        COND = {
            0: "Clear", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
            45: "Fog", 48: "Rime fog", 51: "Light drizzle", 53: "Drizzle", 55: "Heavy drizzle",
            61: "Light rain", 63: "Rain", 65: "Heavy rain", 66: "Freezing rain", 67: "Freezing rain",
            71: "Light snow", 73: "Snow", 75: "Heavy snow", 77: "Snow grains",
            80: "Rain showers", 81: "Rain showers", 82: "Heavy showers",
            85: "Snow showers", 86: "Heavy snow showers",
            95: "Thunderstorm", 96: "Thunderstorm w/ hail", 99: "Severe thunderstorm"
        }
        code_text = COND.get(code, "Conditions")

        # Light logic
        light = "off"
        light_msg = "Calm conditions."
        # Red if severe wind OR severe code
        if wind >= 40 or daily_wind_max >= 40 or code in SEVERE_CODES:
            light, light_msg = "red", "🚨 Severe wind alert — use caution."
        elif wind >= 25:
            light, light_msg = "yellow", "⚠️ Moderate wind — secure lightweight gear."

        return {
            "temp": temp, "feels_like": feels, "wind": wind,
            "code": code, "code_text": code_text, "hi": hi, "lo": lo,
            "time": tstamp, "place": "Ragland, AL",
            "light": light, "light_msg": light_msg
        }
    except Exception:
        return {
            "temp": "--", "feels_like": "--", "wind": "--",
            "code": 0, "code_text": "Conditions", "hi": "--", "lo": "--",
            "time": "", "place": "Ragland, AL",
            "light": "off", "light_msg": "Calm conditions."
        }

# ------------------- Routes -------------------
@app.route("/")
def home():
    # mini weather strip on home
    m = fetch_weather()
    (rq, ra) = get_daily_riddle()
    story = get_daily_story()
    return render_template(
        "home.html",
        app_name=APP_NAME,
        music=MUSIC_LINKS,
        m=m,
        riddle_q=rq,
        riddle_a=ra,
        story_teaser=story[:140] + "…" if len(story) > 140 else story
    )

@app.route("/weather")
def weather():
    m = fetch_weather()
    return render_template("weather.html", m=m)

@app.route("/riddles")
def riddles():
    # full list for cycling
    return render_template("riddles.html", items=RIDDLES)

@app.route("/story")
def story():
    s = get_daily_story()
    return render_template("story.html", text=s)

# ------------------- Health & Diagnostics -------------------
@app.route("/health")
def health():
    return "OK", 200

@app.route("/__diag")
def __diag():
    routes = sorted([f"{list(r.methods)} {r.rule}" for r in app.url_map.iter_rules()])
    info = {
        "python": sys.version,
        "module_loaded": str(app.import_name),
        "routes": routes,
        "has_templates": os.path.isdir(os.path.join(os.getcwd(), "templates")),
        "has_static": os.path.isdir(os.path.join(os.getcwd(), "static")),
    }
    return jsonify(info), 200

@app.route("/__js_err", methods=["POST"])
def __js_err():
    try:
        payload = request.get_json(force=True, silent=True) or {}
        print("🟣 JS Error:", json.dumps(payload)[:2000], flush=True)
    except Exception:
        pass
    return "ok", 200

@app.errorhandler(Exception)
def __global_errors(e):
    tb = traceback.format_exc()
    return (
        f"<pre style='white-space:pre-wrap;background:#140b1d;color:#f8f8f2;padding:12px;border:1px solid #333'>"
        f"🔥 Uncaught server error:\n\n{tb}</pre>",
        500,
        {"Content-Type": "text/html"},
    )
