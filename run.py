from flask import Flask, render_template_string
app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("<h1 style='color:#fff;background:#000;padding:2rem;text-align:center'>TimmyApp is Live</h1>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
