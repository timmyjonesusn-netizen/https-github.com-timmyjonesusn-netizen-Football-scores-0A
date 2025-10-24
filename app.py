from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# keep-awake endpoint (you can ping this URL on a schedule)
@app.route("/ping")
def ping():
    return "OK", 200

if __name__ == "__main__":
    # DIRECT RUN. no gunicorn.
    app.run(host="0.0.0.0", port=5000)
