from flask import Flask, render_template

app = Flask(__name__)

# === PLAYLISTS (slot #5 uses your new Suno link) ===
PLAYLISTS = [
    {
        "title": "Yeti Chill Sessions",
        "vibe": "Playful lo-fi with icy holographic shimmer — calm focus & cozy reels.",
        "url": "https://suno.com/playlist/your-yeti-chill-link"
    },
    {
        "title": "Mr. Bill’s Beat Lab",
        "vibe": "Funky, experimental, comedic bounce — quick cuts & high-energy edits.",
        "url": "https://suno.com/playlist/your-mr-bill-link"
    },
    {
        "title": "HUI Frequencies",
        "vibe": "Meditative, dimensional tone-maps — grounding pads for deep workflow.",
        "url": "https://suno.com/playlist/your-hui-link"
    },
    {
        "title": "Timmy’s Neon Flow",
        "vibe": "Smooth synthwave for late-night editing — steady motion, cinematic glow.",
        "url": "https://suno.com/playlist/your-neon-flow-link"
    },
    {
        "title": "Timmy’s Sexy Sax",
        "vibe": "Holographic, seductive, neon-warm, and smooth — perfect for creative content & ambient focus.",
        "url": "https://suno.com/playlist/01b65a04-d231-4574-bbb6-713997ca5b44"  # replaced slot #5
    }
]

@app.route("/music")
def music():
    return render_template("music.html", playlists=PLAYLISTS)

if __name__ == "__main__":
    app.run(debug=True)
