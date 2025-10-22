# serv_timmyapp.py — TimmyApp: Full Fresh Build (no f-strings, single-file)
import os, random
from datetime import datetime, date
from flask import Flask, make_response, redirect, jsonify
import requests

APP_NAME = "TimmyApp"
RAGLAND_LAT, RAGLAND_LON = 33.744, -86.150

# --------- DATA ---------
POLICE_NOTES = [
    {"title": "Community Reminder", "body": "School zone patrols active 7–9 AM and 2–4 PM. Please slow down."},
    {"title": "Safety Tip", "body": "Lock vehicles at night. Report suspicious activity via non-emergency line."},
    {"title": "Weekend Notice", "body": "Parade route near Main St. Sat 10 AM — rolling closures for ~45 minutes."}
]

RIDDLES = [
    {"q": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
     "choices": ["An echo", "A kite", "A flute", "Leaves"], "answer": "An echo"},
    {"q": "What can run but never walks, has a mouth but never talks?",
     "choices": ["A river", "A shadow", "Time", "Fire"], "answer": "A river"}
]

PEMDAS_TEXT = (
    "PEMDAS = Parentheses → Exponents → Multiplication/Division → Addition/Subtraction. "
    "Work left-to-right within each tier. Example: 8 + 6 ÷ 3 × (2 + 1)^2 = 8 + 2 × 9 = 8 + 18 = 26."
)

PLAYLISTS = [
    {"name": "Playlist 1", "url": "https://suno.com/playlist/457d7e00-938e-4bf0-bd59-f070729200df"},
    {"name": "Playlist 2", "url": "https://suno.com/playlist/2ec04889-1c23-4e2d-9c27-8a2b6475da4b"},
    {"name": "Playlist 3", "url": "https://suno.com/playlist/e95ddd12-7e37-43e2-b3e0-fe342085a19f"},
    {"name": "Playlist 4", "url": "https://suno.com/playlist/2e2eefa6-6828-40ba-bf5b-02bf338e3243"},
    {"name": "Playlist 5", "url": "https://suno.com/playlist/2e2eefa6-6828-40ba-bf5b-02bf338e3243",
     "note": "🎶 Redirected to Suno — 14-song playlist especially for creators. Free background music, no copyright."}
]

HISTORY_ROTATION = [
    {"title": "Revolutionary War (1775–1783)", "blurb": "Thirteen colonies fought for independence, reshaping a continent."},
    {"title": "War of 1812 (1812–1815)", "blurb": "Naval clashes and frontier battles tested the young United States."},
    {"title": "Creek War (1813–1814)", "blurb": "Andrew Jackson’s forces fought Red Stick Creeks — Horseshoe Bend proved decisive."},
    {"title": "Civil War (1861–1865)", "blurb": "A nation divided — industrial might, railways, and ironclads changed warfare."},
    {"title": "WWII (1939–1945)", "blurb": "Global conflict; radar, codebreaking, and air power defined the era."}
]

TEN_ISLANDS_STORY = (
    "At Ten Islands on the Coosa, the river bends like a drawn bow. In 1813–1814, Andrew Jackson "
    "moved men, wagons, and cannon through mud and pine to close the loop on the Creek War. "
    "Fort Strother rose as a hub — a rough grid of huts and stores — where scouts traded whispers "
    "for rations and blacksmiths beat iron bright as lightning. When orders came, columns splashed "
    "through ford and shoal, the river singing against their boots. The campaign traced a hard crescent "
    "toward Horseshoe Bend, where the fighting cracked like timber and the tide turned. By the time "
    "the smoke cleared, the Coosa carried it downstream — past the islands, past the camps — leaving "
    "only footprints in clay and the stubborn echo of drum and bugle."
)

# --------- STYLE ---------
def css_global():
    return (
        "<style>"
        ":root{--bg1:#1a0731;--bg2:#3b0b5e;--ink:#f7e9ff;--blue:#6bb0ff}"
        "*{box-sizing:border-box}html,body{height:100%;margin:0}"
        "body{font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;"
        "color:var(--ink);background:radial-gradient(120% 120% at 50% 0%,var(--bg2),var(--bg1));overflow-x:hidden}"
        "@keyframes pulse{0%,100%{box-shadow:0 0 20px 4px rgba(255,79,216,.20)}50%{box-shadow:0 0 40px 10px rgba(255,79,216,.45)}}"
        "#bubbles{position:fixed;inset:0;z-index:1;pointer-events:none}"
        ".wrap{position:relative;z-index:2;max-width:1000px;margin:0 auto;padding:22px}"
        ".nav{display:flex;gap:10px;flex-wrap:wrap;margin:6px 0 16px}"
        ".btn{display:inline-block;padding:10px 14px;border:1px solid rgba(255,79,216,.6);border-radius:12px;"
        "text-decoration:none;color:var(--ink)}"
        ".btn.blue{border-color:var(--blue);background:transparent}"
        ".pill{display:inline-block;background:rgba(255,79,216,.15);border:1px solid rgba(255,79,216,.35);"
        "padding:6px 10px;border-radius:999px;font-size:14px}"
        ".grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}"
        ".card{background:linear-gradient(180deg,rgba(255,79,216,.07),rgba(255,79,216,.01));"
        "border:1px solid rgba(255,79,216,.25);border-radius:18px;padding:16px;animation:pulse 3s ease-in-out infinite}"
        ".card h3{margin:0 0 8px}"
        ".scroll{max-height:65vh;overflow:auto;padding-right:8px}"
        ".wordmark{font-family:cursive;font-size:28px;letter-spacing:2px;opacity:.95;margin-bottom:12px;"
        "text-shadow:0 0 12px rgba(255,255,255,.25), 0 0 18px rgba(255,79,216,.35)}"
        "h1{margin:8px 0 2px;font-size:42px;text-shadow:0 0 16px rgba(255,79,216,.55)}"
        "footer{opacity:.8;margin-top:20px;font-size:14px}"
        "</style>"
    )

def bubbles_js():
    # Purple core, with occasional blue and rare white bubbles
    return (
        "<script>(function(){"
        "const c=document.getElementById('bubbles');const x=c.getContext('2d');let W,H,B=[];"
        "function R(){W=c.width=innerWidth;H=c.height=innerHeight}addEventListener('resize',R);R();"
        "function color(){const r=Math.random();if(r<0.05)return'white';if(r<0.25)return'blue';return'pink'}"
        "function S(){const n=34;B=new Array(n).fill(0).map(()=>({x:Math.random()*W,y:H+Math.random()*H,r:5+Math.random()*22,"
        "s:.35+Math.random()*1.7,d:(Math.random()*.7)-.35,a:.15+Math.random()*.35,t:color()}))}S();"
        "function T(){x.clearRect(0,0,W,H);for(const b of B){b.y-=b.s;b.x+=b.d;if(b.y+b.r<-24){b.y=H+24;b.x=Math.random()*W;b.t=color()}"
        "x.beginPath();let core='255,79,216';if(b.t==='blue')core='120,170,255';if(b.t==='white')core='255,255,255';"
        "const g=x.createRadialGradient(b.x,b.y,0,b.x,b.y,b.r);"
        "g.addColorStop(0,'rgba('+core+','+(b.a+.25)+')');g.addColorStop(1,'rgba(255,255,255,0)');x.fillStyle=g;"
        "x.arc(b.x,b.y,b.r,0,Math.PI*2);x.fill()}requestAnimationFrame(T)}T();})();</script>"
    )

def navbar(active):
    def link(href, label, key, extra=""):
        base = "<a class='btn " + extra + "' href='" + href + "'>" + label + "</a>"
        return "<span class='btn " + extra + "' style='background:rgba(255,79,216,.2)'>" + label + "</span>" if key == active else base
    return (
        "<div class='nav'>"
        + link("/home","Home","home")
        + link("/police","Police","police","blue")
        + link("/music","Music","music")
        + link("/weather","Weather","weather")
        + link("/learn","PEMDAS & Riddle","learn")
        + link("/history","Ten Islands History","history")
        + "</div>"
    )

def page_shell(active, title, inner_html, pill_text):
    html = (
        "<!doctype html><meta charset='utf-8'/>"
        "<meta name='viewport' content='width=device-width, initial-scale=1'/>"
        "<title>" + title + " — " + APP_NAME + "</title>"
        + css_global() +
        "<canvas id='bubbles'></canvas>"
        "<div class='wrap'>"
        "<div class='wordmark'>Timmy</div>"
        "<h1>" + title + "</h1>"
        "<div class='nav'><span class='pill'>" + pill_text + "</span></div>"
        + navbar(active) +
        inner_html +
        "<footer>© " + str(datetime.utcnow().year) + " Timmy — Deployed " + datetime.utcnow().isoformat() + "Z</footer>"
        "</div>"
        + bubbles_js()
    )
    r = make_response(html, 200)
    r.headers["Content-Type"] = "text/html; charset=utf-8"
    return r

# --------- HELPERS ---------
def weather_text():
    try:
        r = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": RAGLAND_LAT,
                "longitude": RAGLAND_LON,
                "current_weather": True,
                "temperature_unit": "fahrenheit",
                "windspeed_unit": "mph"
            },
            timeout=5
        )
        if r.ok:
            d = r.json().get("current_weather", {})
            t, w = d.get("temperature"), d.get("windspeed")
            if t is not None and w is not None:
                return str(int(round(t))) + "°F, " + str(int(round(w))) + " mph wind"
    except Exception:
        pass
    return "Weather unavailable"

# --------- APP ---------
def create_app():
    app = Flask(__name__)

    # Simple security headers
    @app.after_request
    def secure(resp):
        resp.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains; preload"
        resp.headers["X-Content-Type-Options"] = "nosniff"
        resp.headers["X-Frame-Options"] = "DENY"
        return resp

    @app.route("/")
    def root():
        return redirect("/home", code=302)

    @app.route("/home")
    def home():
        wt = weather_text()
        cards = (
            "<div class='grid'>"
            "<div class='card'><h3>Police</h3><p>Community notes and safety tips.</p>"
            "<p><a class='btn blue' href='/police'>Open Police</a></p></div>"
            "<div class='card'><h3>Music</h3><p>Five Suno playlists — pick your vibe.</p>"
            "<p><a class='btn' href='/music'>Open Music</a></p></div>"
            "<div class='card'><h3>Weather</h3><p>" + wt + "</p>"
            "<p><a class='btn' href='/weather'>Weather Details</a></p></div>"
            "<div class='card'><h3>PEMDAS & Riddle</h3><p>Quiz your brain and remember the order.</p>"
            "<p><a class='btn' href='/learn'>Open Learn</a></p></div>"
            "<div class='card'><h3>Ten Islands History</h3><p>Andrew Jackson, Fort Strother, and the Coosa bend.</p>"
            "<p><a class='btn' href='/history'>Open History</a></p></div>"
            "</div>"
        )
        return page_shell("home", "Purple/Pink Glow + Bubbles", cards, "Welcome")

    @app.route("/police")
    def police():
        items = "".join("<div class='card'><h3>"+p["title"]+"</h3><p>"+p["body"]+"</p></div>" for p in POLICE_NOTES)
        return page_shell("police", "Police Corner", "<div class='grid'>"+items+"</div>", "Transparent blue nav button")

    @app.route("/music")
    def music():
        cards = ""
        for pl in PLAYLISTS:
            cards += "<div class='card'><h3>"+pl["name"]+"</h3><p><a class='btn' target='_blank' rel='noopener' href='"+pl["url"]+"'>Play Now</a></p>"
            if "note" in pl:
                cards += "<p style='font-size:13px;opacity:.9'>"+pl["note"]+"</p>"
            cards += "</div>"
        return page_shell("music", "Music", "<div class='grid'>"+cards+"</div>", "Five playlists ready")

    @app.route("/weather")
    def weather():
        return page_shell("weather", "Weather", "<div class='card'><p>"+weather_text()+"</p></div>", "Live data")

    @app.route("/learn")
    def learn():
        rid = date.today().toordinal() % len(RIDDLES)
        r = RIDDLES[rid]
        inner = (
            "<div class='grid'>"
            "<div class='card'><h3>PEMDAS</h3><p>"+PEMDAS_TEXT+"</p></div>"
            "<div class='card'><h3>Riddle</h3><p>"+r['q']+"</p>"
            "<details><summary>Choices</summary><ul>"+ "".join("<li>"+c+"</li>" for c in r['choices']) +"</ul></details>"
            "<details><summary>Answer</summary><p><strong>"+r['answer']+"</strong></p></details></div>"
            "</div>"
        )
        return page_shell("learn", "PEMDAS & Riddle", inner, "Brain tickle time")

    @app.route("/history")
    def history():
        i = datetime.utcnow().timetuple().tm_yday % len(HISTORY_ROTATION)
        h = HISTORY_ROTATION[i]
        inner = (
            "<div class='grid'>"
            "<div class='card'><h3>Ten Islands • Creek War (1813–1814)</h3><div class='scroll'><p>"+TEN_ISLANDS_STORY+"</p></div></div>"
            "<div class='card'><h3>Today’s Mini-Story</h3><p><strong>"+h['title']+"</strong></p><p>"+h['blurb']+"</p></div>"
            "</div>"
        )
        return page_shell("history", "Historical Ten Islands", inner, "Andrew Jackson & Fort Strother")

    # Simple APIs if you ever need them
    @app.route("/api/police")
    def api_police():
        return jsonify({"notes": POLICE_NOTES})

    @app.route("/api/playlists")
    def api_playlists():
        return jsonify({"playlists": PLAYLISTS})

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
                    "windspeed_unit": "mph"
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

    # Catch-all → send visitors home (prevents 404s)
    @app.route("/<path:_unused>")
    def fallback(_unused):
        return redirect("/home", code=302)

    return app

# iOS-safe local run (no reloader)
if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
