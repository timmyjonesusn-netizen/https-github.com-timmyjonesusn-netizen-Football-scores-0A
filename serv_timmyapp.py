# serv_timmyapp.py — Flask app with redirect + catch-all (no f-strings)
import os
from datetime import datetime
from flask import Flask, make_response, redirect

APP_NAME = "TimmyApp"

def create_app():
    app = Flask(__name__)

    # ---- Inline home page (no static files required) ----
    def home_html():
        return (
            "<!doctype html><meta charset='utf-8'/>"
            "<meta name='viewport' content='width=device-width, initial-scale=1'/>"
            "<title>TimmyApp — Home</title>"
            "<style>"
            ":root{--bg1:#1a0731;--bg2:#3b0b5e;--ink:#f7e9ff;--glow:#ff4fd8}"
            "*{box-sizing:border-box}html,body{height:100%;margin:0}"
            "body{font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;"
            "color:var(--ink);background:radial-gradient(120% 120% at 50% 0%,var(--bg2),var(--bg1));overflow:hidden}"
            "@keyframes pulse{0%,100%{box-shadow:0 0 20px 4px rgba(255,79,216,.2)}50%{box-shadow:0 0 40px 10px rgba(255,79,216,.45)}}"
            ".container{position:relative;z-index:2;padding:24px;max-width:980px;margin:0 auto}"
            "h1{margin:0 0 12px;text-shadow:0 0 12px rgba(255,79,216,.6)}"
            ".cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}"
            ".card{background:linear-gradient(180deg,rgba(255,79,216,.07),rgba(255,79,216,.01));border:1px solid rgba(255,79,216,.25);"
            "border-radius:14px;padding:14px;animation:pulse 3s ease-in-out infinite}"
            ".scrollbox{max-height:180px;overflow:auto;padding-right:6px}"
            "#bubbles{position:fixed;inset:0;z-index:1}"
            "a.btn{display:inline-block;margin-top:14px;padding:8px 12px;border:1px solid rgba(255,79,216,.6);"
            "border-radius:10px;text-decoration:none;color:var(--ink)}"
            "</style>"
            "<canvas id='bubbles'></canvas>"
            "<div class='container'>"
            "<h1>Purple/Pink Glow + Bubbles</h1>"
            "<p>Deployed at: " + datetime.utcnow().isoformat() + "Z</p>"
            "<section class='cards'>"
            "<div class='card'><h3>Events</h3><p>Display-only boxes. No inputs.</p></div>"
            "<div class='card'><h3>Whodunnit</h3><div class='scrollbox'>"
            "<p>Ragland’s mystery unfolded under the stadium lights…</p>"
            "</div></div></section>"
            "<a class='btn' href='/home'>Refresh Home</a>"
            "</div>"
            "<script>(function(){"
            "const c=document.getElementById('bubbles');const x=c.getContext('2d');let W,H,B=[];"
            "function R(){W=c.width=innerWidth;H=c.height=innerHeight}addEventListener('resize',R);R();"
            "function S(){const n=24;B=new Array(n).fill(0).map(()=>({x:Math.random()*W,y:H+Math.random()*H,r:4+Math.random()*18,"
            "s:.4+Math.random()*1.6,d:(Math.random()*.6)-.3,a:.15+Math.random()*.35}))}S();"
            "function T(){x.clearRect(0,0,W,H);for(const b of B){b.y-=b.s;b.x+=b.d;if(b.y+b.r<-20){b.y=H+20;b.x=Math.random()*W}"
            "x.beginPath();const g=x.createRadialGradient(b.x,b.y,0,b.x,b.y,b.r);"
            "g.addColorStop(0,'rgba(255,79,216,'+(b.a+.25)+')');g.addColorStop(1,'rgba(255,255,255,0)');x.fillStyle=g;"
            "x.arc(b.x,b.y,b.r,0,Math.PI*2);x.fill()}requestAnimationFrame(T)}T();"
            "})();</script>"
        )

    # Root -> redirect to /home so the main URL always works
    @app.route("/")
    def root():
        return redirect("/home", code=302)

    @app.route("/home")
    def home():
        html = home_html()
        resp = make_response(html, 200)
        resp.headers["Content-Type"] = "text/html; charset=utf-8"
        return resp

    @app.route("/healthz")
    def healthz():
        return "ok", 200

    # Catch-all: anything not matched serves the Home page (prevents 404s)
    @app.route("/<path:_unused>")
    def fallback(_unused):
        html = home_html()
        resp = make_response(html, 200)
        resp.headers["Content-Type"] = "text/html; charset=utf-8"
        return resp

    return app

# iOS-safe local run (no reloader)
if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
