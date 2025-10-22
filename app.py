from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def home():
    html = "<body style='background-color:#6a0dad;color:white;font-family:sans-serif;display:flex;align-items:center;justify-content:center;height:100vh'><h1>🟣 Timmy Comms Online</h1></body>"
    return Response(html, mimetype='text/html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
