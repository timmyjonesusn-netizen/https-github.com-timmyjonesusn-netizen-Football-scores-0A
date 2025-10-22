# serv_timmyapp.py — Impossible-to-miss neon test + version pings
import os, time
from flask import Flask, Response, jsonify

app = Flask(__name__)
BUILD_TS = os.environ.get("TIMMY_BUILD_TS", str(int(time.time())))

INLINE = f"""<!doctype html><html lang="en"><head>
<meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>TimmyApp — Neon Check</title>
<style>
  html,body{{margin:0;height:100%;overflow:hidden;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}}
  body{{background:#ff00ff}} /* MAGENTA wall. If you see white, this code isn't running. */
  .wrap{{position:fixed;inset:0;display:grid;place-items:center;color:#000;text-align:center}}
  h1{{font-size:clamp(32px,8vw,84px);margin:0 0 10px}}
  p{{font-size:clamp(16px,3.6vw,28px);margin:0}}
  .chip{{display:inline-block;background:#fff;padding:.35rem .6rem;border-radius:999px;margin-top:12px;border:2px solid #000}}
</style>
</head><body>
<div class="wrap">
  <div>
    <h1>NEON ONLINE ✅</h1>
    <p>If this isn’t bright magenta, you’re not seeing this build.</p>
    <div class="chip">build: {BUILD_TS}</div>
  </div>
</div>
</body></html>"""

@app.route("/")
def home():
    # Hard no-cache; if you still see white, it’s not this code.
    resp = Response(INLINE, mimetype="text/html; charset=utf-8")
    resp.headers["Cache-Control"] = "no-store, max-age=0, must-revalidate"
    resp.headers["Pragma"] = "no-cache"
    resp.headers["Expires"] = "0"
    return resp

@app.route("/health")
def health():
    return jsonify(
        status="ok",
        build=BUILD_TS,
        python=os.getenv("PYTHON_VERSION", "unknown"),
        cwd=os.getcwd()
    )

@app.route("/__version")
def version():
    # Plain text, easy to eyeball
    return Response(f"TIMMY BUILD {BUILD_TS}\n", mimetype="text/plain")
