# serv_timmyapp.py — TimmyApp: Full Single-File Edition (no f-strings)
import os, json, random
from datetime import datetime
from flask import Flask, make_response, redirect, jsonify
import requests

# -------- Settings --------
APP_NAME = "TimmyApp"
RAGLAND_LAT = 33.744   # approx Ragland, AL
RAGLAND_LON = -86.150

# -------- Data (replace any time; pages pull from these) --------
EVENTS = [
    {"title": "Friday Night Lights",
     "body": "Ragland vs. Pell City at 7:00 PM. Tailgate opens at 5:30."},
    {"title": "Ten Islands Park Cleanup",
     "body": "Community meetup at 9:00 AM. Gloves and bags provided."},
    {"title": "Fort Strother Walk",
     "body": "Guided tour at 3:00 PM. Bring water and comfy shoes."}
]

UFC_STORIES = [
    {"title": "Weigh-in Whispers",
     "body": "Striking coach says late camp tweaks boosted feints and first-punch timing."},
    {"title": "Five-Round Questions",
     "body": "Cardio looks sharp; expect pace pressure and calf-kick entries."},
    {"title": "Ground Game Rumor",
     "body": "New chain from single-leg to inside trip — watch the fence work."}
]

WHODUNNIT = (
    "It started with a whisper rolling across the bleachers. The Purple Devils had led by seven, "
    "but the scoreboard flickered, then froze. Coach glanced up just as the moon slid behind a cloud, "
    "and the band hit a note that wasn't in the sheet music. Someone cut the field lights—only for a breath—"
    "but long enough to send a hush over Ragland. When the glow returned, the football sat at the fifty, "
    "and a single muddy footprint faced the wrong way. The sheriff swore it was nothing but mischief, "
    "though he couldn't explain the fresh chalk mark shaped like a question. Folks filed out slow, "
    "watching the shadows in the pines. By morning, somebody had stenciled a tiny devil on the press box door—"
    "not our devil, but one grinning sideways—like he knew which play we'd call next Friday."
)

JOKES = [
    "I told my app to cache more. It said, ‘I’m already storing feelings.’",
    "Why did the server take a nap? Too many REST calls.",
    "404 at the gym: couldn’t find the abs."
]

WORDS = [
    {"word": "sonder", "meaning": "the realization that each passerby has a life as vivid as your own."},
    {"word": "petrichor", "meaning": "the pleasant smell after the first rain on dry ground."},
    {"word": "hiraeth", "meaning": "a homesickness for a home you can’t return to."}
]

SUNO_PLAYLIST = "https://suno.com/playlist/457d7e00-938e-4bf0-bd59-f070729200df"

# -------- Helpers --------
def css_global():
    return (
        "<style>"
        ":root{--bg1:#1a0731;--bg2:#3b0b5e;--ink:#f7e9ff;--glow:#ff4fd8}"
        "*{box-sizing:border-box}html,body{height:100%;margin:0}"
        "body{font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;"
        "color:var(--ink);background:radial-gradient(120% 120% at 50% 0%,var(--bg2),var(--bg1));"
        "overflow-x:hidden}"
        "@keyframes pulse{0%,100%{box-shadow:0 0 20px 4px rgba(255,79,216,.20)}"
        "50%{box-shadow:0 0 40px 10px rgba(255,79,216,.45)}}"
        "#bubbles{position:fixed;inset:0;z-index:1;pointer-events:none}"
        ".wrap{position:relative;z-index:2;max-width:1000px;margin:0 auto;padding:22px}"
        ".nav{display:flex;gap:10px;flex-wrap:wrap;margin:6px 0 16px}"
        ".btn{display:inline-block;padding:10px 14px;border:1px solid rgba(255,79,216,.6);"
        "border-radius:12px;text-decoration:none;color:var(--ink)}"
        ".pill{display:inline-block;background:rgba(255,79,216,.15);border:1px solid rgba(255,79,216,.35);"
        "padding:6px 10px;border-radius:999px;font-size:14px}"
        ".grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}"
        ".card{background:linear-gradient(180deg,rgba(255,79,216,.07),rgba(255,79,216,.01));"
        "border:1px solid rgba(255,79,216,.25);border-radius:18px;padding:16px;animation:pulse 3s ease-in-out infinite}"
        ".card h3{margin:0 0 8px}"
        ".scroll{max-height:65vh;overflow:auto;padding-right:8px}"
        "h1{margin:8px 0 10px;font-size:42px;line-height:1.05;text-shadow:0 0 16px rgba(255,79,216,.55)}"
        "h2{margin:0 0 8px}"
        "footer{opacity:.8;margin-top:20px;font-size:14px}"
        "</style>"
    )

def bubbles_js():
    return (
        "<script>(function(){"
        "const c=document.getElementById('bubbles');const x=c.getContext('2d');let W,H,B=[];"
        "function R(){W=c.width=innerWidth;H=c.height=innerHeight}addEventListener('resize',R);R();"
        "function S(){const n=30;B=new Array(n).fill(0).map(()=>({x:Math.random()*W,y:H+Math.random()*H,r:5+Math.random()*20,"
        "s:.35+Math.random()*1.65,d:(Math.random()*.7)-.35,a:.15+Math.random()*.35}))}S();"
        "function T(){x.clearRect(0,0,W,H);for(const b of B){b.y-=b.s;b.x+=b.d;if(b.y+b.r<-24){b.y=H+24;b.x=Math.random()*W}"
        "x.beginPath();const g=x.createRadialGradient(b.x,b.y,0,b.x,b.y,b.r);"
        "g.addColorStop(0,'rgba(255,79,216,'+(b.a+.25)+')');g.addColorStop(1,'rgba(255,255,255,0)');x.fillStyle=g;"
        "x.arc(b.x,b.y,b.r,0,Math.PI*2);x.fill()}requestAnimationFrame(T)}T();"
        "})();</script>"
    )

def navbar(active):
    # active is one of: home, events, whodunnit, music, weather, fun, ufc
    def link(href, label, key):
        base = "<a class='btn' href='" + href + "'>" + label + "</a>"
        if key == active:
            return "<span class='btn' style='background:rgba(255,79,216,.2)'>" + label + "</span>"
        return base
    return (
        "<div class='nav'>"
        + link("/home","Home","home")
        + link("/events","Events","events")
        + link("/whodunnit","Whodunnit","whodunnit")
        + link("/music","Music","music")
        + link("/weather","Weather","weather")
        + link("/fun","Joke & Word","fun")
        + link("/ufc","UFC Stories","ufc")
        + "</div>"
    )

def page_shell(active, title, inner_html, pill_text):
    head = (
        "<!doctype html><meta charset='utf-8'/>"
        "<meta name='viewport' content='width=device-width, initial-scale=1'/>"
        "<title>" + title + " — " + APP_NAME + "</title>"
        + css_global() +
        "<canvas id='bubbles'></canvas>"
        "<div class='wrap'>"
        "<h1>" + title + "</h1>"
        "<div class='nav'>"
        "<span class='pill'>" + pill_text + "</span>"
        "</div>"
        + navbar(active) +
        inner_html +
        "<footer>© " + str(datetime.utcnow().year) + " Timmy — Deployed " + datetime.utcnow().isoformat() + "Z</footer>"
        "</div>"
        + bubbles_js()
    )
    return head

def weather_now_text():
    try:
        r = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": RAGLAND_LAT,
                "longitude": RAGLAND_LON,
                "current_weather": True,
                "temperature_unit": "fahrenheit",
                "windspeed_unit": "mph",
                "forecast_days": 1,
            },
            timeout=5
        )
        if r.ok:
            data = r.json()
            cur = data.get("current_weather", {})
            t = cur.get("temperature")
            w = cur.get("windspeed")
            if t is not None and w is not None:
                return str(int(round(t))) + "°F, " + str(int(round(w))) + " mph wind"
    except Exception:
        pass
    return "Weather unavailable"

# -------- App Factory --------
def create_app():
    app = Flask(__name__)

    # ---------- Pages ----------
    @app.route("/")
    def root():
        return redirect("/home", code=302)

    @app.route("/home")
    def home():
        wt = weather_now_text()
        cards = (
            "<div class='grid'>"
            "<div class='card'><h3>Events</h3><p>Local happenings and meetups.</p>"
            "<p><a class='btn' href='/events'>Open Events</a></p></div>"
            "<div class='card'><h3>Whodunnit</h3><div class='scroll'><p>" + WHODUNNIT + "</p></div>"
            "<p><a class='btn' href='/whodunnit'>Read Story</a></p></div>"
            "<div class='card'><h3>Music</h3><p>Suno playlist link.</p>"
            "<p><a class='btn' href='/music'>Open Music</a></p></div>"
            "<div class='card'><h3>Weather</h3><p>" + wt + "</p>"
            "<p><a class='btn' href='/weather'>Weather Details</a></p></div>"
            "<div class='card'><h3>Joke & Word</h3><p>Daily fun.</p>"
            "<p><a class='btn' href='/fun'>Open Fun</a></p></div>"
            "<div class='card'><h3>UFC Stories</h3><p>Lean rumor mill.</p>"
            "<p><a class='btn' href='/ufc'>Open UFC</a></p></div>"
            "</div>"
        )
        html = page_shell("home", "Purple/Pink Glow + Bubbles", cards, "Welcome")
        resp = make_response(html, 200)
        resp.headers["Content-Type"] = "text/html; charset=utf-8"
        return resp

    @app.route("/events")
    def events():
        items = ""
        for e in EVENTS:
            items += "<div class='card'><h3>" + e["title"] + "</h3><p>" + e["body"] + "</p></div>"
        inner = "<div class='grid'>" + items + "</div>"
        html = page_shell("events", "Events", inner, "Display-only boxes — no inputs")
        r = make_response(html, 200); r.headers["Content-Type"] = "text/html; charset=utf-8"; return r

    @app.route("/whodunnit")
    def whodunnit():
        inner = "<div class='card'><div class='scroll'><p>" + WHODUNNIT + "</p></div></div>"
        html = page_shell("whodunnit", "Whodunnit", inner, "Ragland mystery file")
        r = make_response(html, 200); r.headers["Content-Type"] = "text/html; charset=utf-8"; return r

    @app.route("/music")
    def music():
        inner = (
            "<div class='card'><h3>Suno Playlist</h3>"
            "<p><a class='btn' target='_blank' rel='noopener' href='" + SUNO_PLAYLIST + "'>Open Suno Playlist</a></p>"
            "<p>Tip: Suno may require the app installed/logged in on mobile.</p>"
            "</div>"
        )
        html = page_shell("music", "Music", inner, "Let it play, DJ Timmy")
        r = make_response(html, 200); r.headers["Content-Type"] = "text/html; charset=utf-8"; return r

    @app.route("/weather")
    def weather():
        wt = weather_now_text()
        inner = "<div class='card'><h3>Ragland Weather (°F)</h3><p>" + wt + "</p><p><a class='btn' href='/home'>Back Home</a></p></div>"
        html = page_shell("weather", "Weather", inner, "Live pull via Open-Meteo")
        r = make_response(html, 200); r.headers["Content-Type"] = "text/html; charset=utf-8"; return r

    @app.route("/fun")
    def fun():
        j = random.choice(JOKES)
        w = random.choice(WORDS)
        inner = (
            "<div class='grid'>"
            "<div class='card'><h3>Joke of the Day</h3><p>" + j + "</p></div>"
            "<div class='card'><h3>Word of the Day</h3><p><strong>" + w["word"] + "</strong> — " + w["meaning"] + "</p></div>"
            "</div>"
        )
        html = page_shell("fun", "Daily Fun", inner, "Fresh chuckle + vocab boost")
        r = make_response(html, 200); r.headers["Content-Type"] = "text/html; charset=utf-8"; return r

    @app.route("/ufc")
    def ufc():
        items = ""
        for s in UFC_STORIES:
            items += "<div class='card'><h3>" + s["title"] + "</h3><p>" + s["body"] + "</p></div>"
        inner = "<div class='grid'>" + items + "</div>"
        html = page_shell("ufc", "UFC Stories", inner, "Read-only, clean layout")
        r = make_response(html, 200); r.headers["Content-Type"] = "text/html; charset=utf-8"; return r

    # ---------- APIs (for later front-end use) ----------
    @app.route("/api/events")
    def api_events():
        return jsonify({"events": EVENTS})

    @app.route("/api/ufc")
    def api_ufc():
        return jsonify({"stories": UFC_STORIES})

    @app.route("/api/fun")
    def api_fun():
        w = random.choice(WORDS)
        return jsonify({"joke": random.choice(JOKES), "word": w["word"], "meaning": w["meaning"]})

    @app.route("/api/weather")
    def api_weather():
        try:
            r = requests.get(
                "https://api.open-meteo.com/v1/forecast",
                params={
                    "latitude": RAGLAND_LAT,
                    "longitude": RAGLAND_LON,
                    "current_weather": True,
                    "temperature_unit": "fahrenheit",
                    "windspeed_unit": "mph",
                    "forecast_days": 1,
                },
                timeout=5
            )
            if r.ok:
                return jsonify(r.json())
            return jsonify({"error": "weather provider error"}), 502
        except Exception:
            return jsonify({"error": "weather fetch failed"}), 500

    @app.route("/healthz")
    def healthz():
        return "ok", 200

    # Catch-all keeps visitors in the app
    @app.route("/<path:_unused>")
    def fallback(_unused):
        return redirect("/home", code=302)

    return app

# ---- iOS-safe local run (no reloader) ----
if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
