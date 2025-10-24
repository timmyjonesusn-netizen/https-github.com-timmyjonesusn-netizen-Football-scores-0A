from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# tiny ping route to keep service warm
# you (or an external uptime pinger) can hit /ping on an interval
# Render free tiers will still spin down if nobody hits it,
# but this gives you a stable URL you can "poke" so it stays alive.
@app.route("/ping")
def ping():
    return "OK", 200

if __name__ == "__main__":
    # NO GUNICORN. direct run.
    app.run(host="0.0.0.0", port=5000)
