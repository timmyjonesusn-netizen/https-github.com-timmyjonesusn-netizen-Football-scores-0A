# serv_timmyapp.py — Timmyapp multipage preview (no external APIs yet)
from flask import Flask, render_template
from datetime import datetime

APP_NAME = "Timmyapp"

def create_app():
    app = Flask(__name__, static_folder="static", static_url_path="/static")

    @app.route("/")
    def home():
        return render_template("home.html", app_name=APP_NAME, now=datetime.utcnow())

    @app.route("/scores")
    def scores():
        # demo data so you can SEE the layout
        games = [
            {"team":"Alabama","opponent":"Georgia","when":"Sat 7:00 PM","status":"Preview","note":"SEC showdown"},
            {"team":"Auburn","opponent":"LSU","when":"Sat 3:30 PM","status":"Preview","note":"Tiger vs Tiger"},
            {"team":"JSU","opponent":"Sam Houston","when":"Fri 8:00 PM","status":"Preview","note":"CUSA tilt"},
        ]
        return render_template("scores.html", app_name=APP_NAME, games=games)

    @app.route("/events")
    def events():
        items = [
            {"city":"Ragland","title":"Fall Fest at Ten Islands","time":"Sat 10:00 AM","place":"Historical Park"},
            {"city":"Pell City","title":"Farmers Market","time":"Sun 9:00 AM","place":"Downtown"},
            {"city":"Oxford","title":"Music in the Park","time":"Fri 6:30 PM","place":"Choccolocco Park"},
        ]
        return render_template("events.html", app_name=APP_NAME, items=items)

    @app.route("/weather")
    def weather():
        # static demo values (°F) just to preview the look
        data = {"city":"Ragland, AL","now":"76°F","hi":"81°F","lo":"59°F","summary":"Partly Cloudy"}
        return render_template("weather.html", app_name=APP_NAME, data=data)

    @app.route("/music")
    def music():
        # placeholder for your Suno playlist
        suno_url = "https://suno.com/playlist/457d7e00-938e-4bf0-bd59-f070729200df"
        return render_template("music.html", app_name=APP_NAME, suno_url=suno_url)

    @app.route("/health")
    def health():
        return {"status":"ok","app":APP_NAME,"utc":datetime.utcnow().isoformat()}

    # minimal offline-capable service worker
    @app.route("/service-worker.js")
    def sw():
        js = (
            "self.addEventListener('install',e=>self.skipWaiting());"
            "self.addEventListener('activate',e=>self.clients.claim());"
            "self.addEventListener('fetch',e=>{e.respondWith(fetch(e.request)"
            ".catch(()=>new Response('Offline',{status:200})));});"
        )
        from flask import make_response
        resp = make_response(js)
        resp.headers["Content-Type"] = "application/javascript"
        return resp

    return app
