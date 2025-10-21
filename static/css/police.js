// =====================================
// 🐾 Reggie the Dog — Police Corner JS
// 3D vibe, greenery, daily story, quips
// =====================================

const STORIES = [
  {
    title: "Dumpster Raccoon, Level: Boss",
    story: "Deputy said, “Reggie, quit negotiating with the raccoon.” I said, “Sir, he’s got leverage — he’s sitting on the donuts.”",
    moral: "Keep your tail clean, your bark friendly, and never bargain with wildlife holding pastries."
  },
  {
    title: "Parade Duty & The Tuba Incident",
    story: "I marched two blocks in formation until the tuba player dropped a C note. I chased it. For science.",
    moral: "If the beat moves you, move — but maybe not during the mayor’s speech."
  },
  {
    title: "Speed Trap at Ten Islands",
    story: "Officer says, “Reggie, that’s not a radar gun.” I says, “No sir, it’s a squeaky toy. But it detects suspicious squirrels.”",
    moral: "Tools matter. So does enthusiasm. Use both with wisdom."
  },
  {
    title: "Noise Complaint: Midnight Howlin’",
    story: "Neighbor filed on me for ‘moon-sync vocalization.’ I requested a permit for art.",
    moral: "When the moon is full, be respectful… but don’t smother your song."
  },
  {
    title: "Lost & Found: Sandwich Edition",
    story: "Officer asked if I’d seen a missing BLT. I said yes… briefly.",
    moral: "Confession is good for the soul, but next time bring extra bacon."
  }
];

// Quips Reggie says when tapped
const QUIPS = [
  "K-9 division? I thought they said dine.",
  "Sir, my tail is a metronome for justice.",
  "License and registration? I got treats and reputation.",
  "Ten-four! Or ten snacks. Either works.",
  "I’m not spoiled; I’m community supported.",
  "Protect and serve… and sometimes swerve.",
  "That’s not contraband, that’s my emotional support tennis ball."
];

// Deterministic “story of the day”
function dayOfYear(d){
  const start = new Date(d.getFullYear(),0,0);
  return Math.floor((d - start) / 86400000);
}
function storyOfTheDay(){
  const t = new Date();
  const idx = (t.getFullYear()*400 + dayOfYear(t)) % STORIES.length;
  return STORIES[idx];
}

function setText(id, text){ const el = document.getElementById(id); if(el) el.textContent = text; }

document.addEventListener("DOMContentLoaded", () => {
  // Set date and daily story
  const today = new Date();
  setText("the-date", today.toLocaleDateString());
  const s = storyOfTheDay();
  setText("story-title", s.title);
  setText("story-text", s.story);
  setText("moral-text", s.moral);

  // Reggie quip on tap/enter
  const reggie = document.getElementById("reggie");
  const sayQuip = () => {
    const q = QUIPS[Math.floor(Math.random()*QUIPS.length)];
    // Temporary toast using title swap for fun
    const old = document.getElementById("story-title").textContent;
    document.getElementById("story-title").textContent = `🐾 Reggie says: "${q}"`;
    reggie.setAttribute("aria-pressed","true");
    setTimeout(()=>{
      document.getElementById("story-title").textContent = old;
      reggie.setAttribute("aria-pressed","false");
    }, 2600);
  };

  reggie.addEventListener("click", sayQuip);
  reggie.addEventListener("keydown", (e)=>{ if(e.key === "Enter" || e.key === " "){ e.preventDefault(); sayQuip(); }});
});
