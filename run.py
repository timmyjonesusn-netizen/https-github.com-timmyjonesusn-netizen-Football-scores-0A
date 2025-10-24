from flask import Flask
app = Flask(__name__)          # <-- MUST exist at module top level

@app.get("/")
def index():
    return "hello"

if __name__ == "__main__":
    app.run()
