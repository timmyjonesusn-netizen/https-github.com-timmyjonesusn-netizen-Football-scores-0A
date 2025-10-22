# run.py
from serv_timmyapp import create_app

if __name__ == "__main__":
    app = create_app()
    # 0.0.0.0 so it works on Render/local; port 8000 default
    app.run(host="0.0.0.0", port=8000, debug=True)
