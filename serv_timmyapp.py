# serv_timmyapp.py — TimmyApp Full Package v1 (no f-strings, iOS-safe local run)
import os, json, time
from datetime import datetime
from flask import Flask, make_response, redirect, jsonify
import requests

APP_NAME = "TimmyApp"

# --- Simple data (you can replace/update these anytime) ---
RAGLAND_LAT = 33.744  # close to Ragland, AL
RAGLAND_LON = -86.150

EVENTS = [
    {"title": "Friday Night Lights", "body": "Ragland vs. Pell City at 7:00 PM. Tailgate opens at 5:30."},
    {"title": "Ten Islands Park Cleanup", "body": "Community meetup at 9:00 AM. Gloves and bags provided."},
    {"title": "Fort Strother Walk", "body": "Guided tour at 3:00 PM. Bring water and comfy shoes."}
]

WHODUNNIT = (
    "It started with a whisper rolling across the bleachers. The Purple Devils had led by seven, "
    "but the scoreboard flickered, then froze. Coach glanced up just as the moon slid behind a cloud, "
    "and the band hit a note that wasn't in the sheet music. Someone cut the field lights—only for a breath—"
    "but long enough to send a hush over Ragland. When the glow returned, the football sat at the fifty, "
    "and a single muddy footprint faced the wrong way. The sheriff swore it was nothing but mischief, "
    "though he couldn't explain the fresh chalk mark shaped like a question. Folks filed out slow, "
    "watching the shadows in the pines. By morning, somebody had stenciled a tiny devil on the press box door—"
    "not our devil, but one grinning sideways—like he knew which play we'd call next friday."
)

def create_app():
    app = Flask(__name__)

    # ---------- Inline pages (no static files required) ----------
    def page_home_html(weather_text):
        # inline CSS + JS; no f-strings, build strings the old-school way
        head = (
            "<!doctype html><meta charset='utf-8'/>"
            "<meta name='viewport' content='width=device-width, initial-scale=1'/>"
            "<title>TimmyApp — Home</title>"
            "<style>"
            ":root{--bg1:#1a0731;--bg2:#3b0b5e;--ink:#f7e9ff;--glow:#ff4fd8}"
            "*{box-sizing:border-box}html,body{height:100%;margin:0}"
            "body{font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;"
            "color:var(--ink);background:radial-gradient(120% 120% at 50% 0%,var(--bg2),var(--bg1));overflow-x:hidden;overflow-y:auto}"
            "@keyframes pulse{0%,100%{box-shadow:0 0 20px 4px rgba(255,79,216,.20)}50%{box-shadow:0 0 40px 10px rgba(255,79,216,.45)}}"
            ".wrap{position:relative;z-index:2;padding:24px;max-width:980px;margin:0 auto}"
            "h1{margin:16px 0 12px;font-size:44px;line-height:1.05;letter-spacing:.2px;"
            "text-shadow:0 0 16px rgba(255,79,216,.55)}"
            "p.lead{opacity:.9;margin:6px 0 18px}"
            ".grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}"
            ".card{background:linear-gradient(180deg,rgba(255,79,216,.07),rgba(255,79,216,.01));"
            "border:1px solid rgba(255,79,216,.25);border-radius:18px;padding:16px;animation:pulse 3s ease-in-out infinite}"
            ".card h3{margin:0 0 8px}"
            ".scroll{max-height:220px;overflow:auto;padding-right:8px}"
            ".row{display:flex;gap:10px;flex-wrap:wrap;margin:12px 0}"
            "a.btn{display:inline-block;padding:10px 14px;border:1px solid rgba(255,79,216,.6);border-radius:12px;"
            "text-decoration:none;color:var(--ink)}"
            "#bubbles{position:fixed;inset:0;z-index:1;pointer-events:none}"
            ".pill{display:inline-block;background:rgba(255,79,216,.15);border:1px solid rgba(255,79,216,.35);"
            "padding:6px 10px;border-radius:999px;font-size:14px}"
            "</style>"
        )
        header = (
            "<canvas id='bubbles'></canvas>"
            "<div class='wrap'>"
            "<h1>Purple/Pink Glow + Bubbles</h1>"
            "<p class='lead'>Deployed at: " + datetime.utcnow().isoformat() + "Z</p>"
        )
        weather_block = (
            "<div class='row'><span class='pill'>Weather: " + weather_text + "</span>"
            "<a class='btn' href='/home'>Refresh</a>"
            "<a class='btn' href='/music'>Music</a>"
            "<a class='btn' href='/events'>Events</a>"
            "<a class='btn' href='/whodunnit'>Whodunnit</a>"
            "</div>"
        )
        cards = (
            "<div class='grid'>"
            "<div class='card'><h3>Events</h3>"
            "<p>Display-only boxes. No inputs.</p>"
            "<p><a class='btn' href='/events'>Open Events</a></p>"
            "</div>"
            "<div class='card'><h3>Whodunnit</h3>"
            "<div class='scroll'><p>" + WHODUNNIT + "</p></div>"
            "<p><a class='btn' href='/whodunnit'>Read Story</a></p>"
            "</div>"
            "<div class='card'><h3>Music</h3>"
            "<p>Jump to your Suno playlist page.</p>"
            "<p><a class='btn' href='/music'>Open Music</a></p>"
            "</div>"
            "</div>"
        )
        footer = "</div>"
        bubbles_js = (
            "<script>(function(){"
            "const c=document.getElementById('bubbles');const x=c.getContext('2d');let W,H,B=[];"
            "function R(){W=c.width=innerWidth;H=c.height=innerHeight}addEventListener('resize',R);R();"
            "function S(){const n=28;B=new Array(n).fill(0).map(()=>({x:Math.random()*W,y:H+Math.random()*H,r:5+Math.random()*20,"
            "s:.35+Math.random()*1.65,d:(Math.random()*.7)-.35,a:.15+Math.random()*.35}))}S();"
            "function T(){x.clearRect(0,0,W,H);for(const b of B){b.y-=b.s;b.x+=b.d;if(b.y+b.r<-24){b.y=H+24;b.x=Math.random()*W}"
            "x.beginPath();const g=x.createRadialGradient(b.x,b.y,0,b.x,b.y,b.r);"
            "g.addColorStop(0,'rgba(255,79,216,'+(b.a+.25)+')');g.addColorStop(1,'rgba(255,255,255,0)');x.fillStyle=g;"
            "x.arc(b.x,b.y,b.r,0,Math.PI*2);x.fill()}requestAnimationFrame(T)}T();"
            "})();</script>"
        )
        return head + header + weather_block + cards + footer + bubbles_js

    def page_events_html():
        items = ""
        for e in EVENTS:
            items += (
                "<div class='card'><h3>" + e["title"] + "</h3>"
                "<p>" + e["body"] + "</p></div>"
            )
        return (
            "<!doctype html><meta charset='utf-8'/>"
            "<meta name='viewport' content='width=device-width, initial-scale=1'/>"
            "<title>Events — TimmyApp</title>"
            "<style>"
            ":root{--bg1:#1a0731;--bg2:#3b0b5e;--ink:#f7e9ff;--glow:#ff4fd8}"
            "body{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;"
            "color:var(--ink);background:radial-gradient(120% 120% at 50% 0%,var(--bg2),var(--bg1))}"
            ".wrap{max-width:980px;margin:0 auto;padding:24px}"
            "h1{margin:0 0 14px;text-shadow:0 0 14px rgba(255,79,216,.55)}"
            ".grid{display:grid;grid-template-columns:1fr;gap:14px}"
            ".card{background:linear-gradient(180deg,rgba(255,79,216,.07),rgba(255,79,216,.01));"
            "border:1px solid rgba(255,79,216,.25);border-radius:16px;padding:16px}"
            "a.btn{display:inline-block;margin-top:10px;padding:8px 12px;border:1px solid rgba(255,79,216,.6);"
            "border-radius:10px;text-decoration:none;color:var(--ink)}"
            "</style>"
            "<div class='wrap'><h1>Events</h1>"
            "<div class='grid'>" + items + "</div>"
            "<p><a class='btn' href='/home'>Back Home</a></p></div>"
        )

    def page_whodunnit_html():
        return (
            "<!doctype html><meta charset='utf-8'/>"
            "<meta name='viewport' content='width=device-width, initial-scale=1'/>"
            "<title>Whodunnit — TimmyApp</title>"
            "<style>"
            ":root{--bg1:#1a0731;--bg2:#3b0b5e;--ink:#f7e9ff}"
            "body{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;"
            "color:var(--ink);background:radial-gradient(120% 120% at 50% 0%,var(--bg2),var(--bg1))}"
            ".wrap{max-width:880px;margin:0 auto;padding:24px}"
            "h1{margin:0 0 12px}"
            ".story{max-height:70vh;overflow:auto;line-height:1.55;background:rgba(0,0,0,.15);"
            "border:1px solid rgba(255,79,216,.25);border-radius:14px;padding:14px}"
            "a.btn{display:inline-block;margin-top:12px;padding:8px 12px;border:1px solid rgba(255,79,216,.6);"
            "border-radius:10px;text-decoration:none;color:var(--ink)}"
            "</style>"
            "<div class='wrap'>"
            "<h1>Whodunnit</h1>"
            "<div class='story'><p>" + WHODUNNIT + "</p></div>"
            "<p><a class='btn' href='/home'>Back Home</a></p>"
            "</div>"
        )

    def page_music_html():
        return (
            "<!doctype html><meta charset='utf-8'/>"
            "<meta name='viewport' content='width=device-width, initial-scale=1'/>"
            "<title>Music — TimmyApp</title>"
            "<style>"
            ":root{--bg1:#1a0731;--bg2:#3b0b5e;--ink:#f7e9ff}"
            "body{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;"
            "color:var(--ink);background:radial-gradient(120% 120% at 50% 0%,var(--bg2),var(--bg1))}"
            ".wrap{max-width:880px;margin:0 auto;padding:24px}"
            "a.btn{display:inline-block;margin-top:10px;padding:10px 14px;border:1px solid rgba(255,79,216,.6);"
            "border-radius:12px;text-decoration:none;color:var(--ink)}"
            "p{opacity:.95}"
            "</style>"
            "<div class='wrap'>"
            "<h1>Music</h1>"
            "<p>Open your Suno playlist in a new tab:</p>"
            "<p><a class='btn' target='_blank' rel='noopener' href='https://suno.com/playlist/457d7e00-938e-4bf0-bd59-f070729200df'>Open Suno Playlist</a></p>"
            "<p><a class='btn' href='/home'>Back Home</a></p>"
            "</div>"
        )

    # ---------- Routes ----------
    @app.route("/")
    def root():
        return redirect("/home", code=302)

    @app.route("/home")
    def home():
        # pull a quick weather string from our API (safe if it errors)
        wt = "Loading weather…"
        try:
            resp = requests.get(
                "https://api.open-meteo.com/v1/forecast",
                params={
                    "latitude": RAGLAND_LAT,
                    "longitude": RAGLAND_LON,
                    "curr
