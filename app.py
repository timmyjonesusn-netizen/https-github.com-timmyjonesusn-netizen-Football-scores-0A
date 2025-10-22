# app.py — ultra-minimal Flask app for "color signal"
from flask import Flask, Response

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Timmy Comms Online</title>
<style>
  html,body { height:100%; margin:0; }
  body {
    background:#6a0dad; /* deep purple */
    color:#fff;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    display:flex; align-items:center; justify-content:center;
  }
  .wrap { text-align:center }
  .tag { opacity:.85; font-size:1rem; margin-top:.5rem }
</style>
</head>
<body>
  <div class="wrap">
    <h1>🟣 Timmy Comms Online</h1>
    <div class="tag">Baseline color signal</div>
  </div>
</body>
</html>
"""

@app.route("/")
def home():
    return Response(HTML, mimetype="text/html")

@app.route("/health")
def health():
    return "OK", 200
