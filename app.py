from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather")
def weather():
    # dummy safe fallback data so page always loads
    weather = {
        "wind_mph": 5,
        "temp_f": 72,
        "condition": "Clear skies",
        "warning": None
    }
    return render_template("weather.html", weather=weather)

@app.route("/music")
def music():
    return render_template("music.html")

@app.route("/story")
def story():
    # add your daily story content here
    story = {
        "title": "The Neon Night in Ragland",
        "body": "As the pink pulse lit the sky, the Yeti tuned his guitar..."
    }
    return render_template("story.html", story=story)

@app.route("/events")
def events():
    events = [
        {"name": "Community Bowling Night", "time": "Friday 7:00 PM", "place": "Strikers Alley"},
        {"name": "Open Mic", "time": "Saturday 8:30 PM", "place": "Main Street"},
        {"name": "Sunday Jam", "time": "Sunday 6:00 PM", "place": "Park Pavilion"},
    ]
    return render_template("events.html", events=events)

if __name__ == "__main__":
    app.run(debug=True)
