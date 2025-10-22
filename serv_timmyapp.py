@app.route("/events")
def events():
    # Sample data; replace with your feed later
    sample_events = [
        {
            "title": "Ragland Friday Night Lights",
            "when": "Fri 7:00 PM · Stadium",
            "blurb": "Purple Devils host a rivalry showdown. Bring the cowbells.",
            "story": "The mascot tunnel is getting an LED glow-up. Rumor says the Yeti might do a halftime cameo..."
        },
        {
            "title": "Ten Islands Picnic & Jam",
            "when": "Sat 11:00 AM · Ten Islands Park",
            "blurb": "Local pickers, BBQ, and kid zone.",
            "story": ""
        },
        {
            "title": "Fort Strother Walk & Talk",
            "when": "Sun 2:00 PM · Fort Strother",
            "blurb": "Short walk + living history chat.",
            "story": "Captain Reggie recounts the ‘Midnight Mascot’ mystery and how glitter paw-prints changed case law. 😉"
        }
    ]
    return render_template("events.html", title="Events", events=sample_events)
