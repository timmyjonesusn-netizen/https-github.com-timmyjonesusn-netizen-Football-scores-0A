# run.py — Render entry point
from serv_timmyapp import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
