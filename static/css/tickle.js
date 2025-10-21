// ===================================
// 🌊 Ten Islands Daily Tickle (Jokes)
// Deterministic daily + extras
// ===================================

const JOKES = [
  "Why did the Yeti refuse to be arrested? He didn’t want to be booked.",
  "Officer said, “You under arrest.” I said, “Cool—do you validate parking at Ten Islands?”",
  "Reggie swears a bass jumped in the boat to turn itself in for loitering.",
  "I told the deputy I’d be silent; my tail said otherwise.",
  "Speed limit at the lake? However fast your laugh travels.",
  "The raccoon testified. His lawyer was a trash can.",
  "I asked if I could plead the fifth. They handed me a sweet tea.",
  "Warning for loud music: guilty of possessing excessive vibes.",
  "Lost-and-found called: your Monday is here; it was napping by the docks.",
  "Why don’t geese get tickets? They always signal when they honk."
];

// Day-of-year for deterministic rotation
function dayOfYear(d){
  const start = new Date(d.getFullYear(),0,0);
  return Math.floor((d - start) / 86400000);
}
function todaysIndex(){
  const t = new Date();
  return (t.getFullYear()*400 + dayOfYear(t)) % JOKES.length;
}

const lbl = document.getElementById("today-label");
const title = document.getElementById("joke-title");
const text = document.getElementById("joke-text");

function setJoke(i, label="🗓️ Today"){
  lbl.textContent = label;
  title.textContent = (label.includes("Random") || label.includes("Another"))
    ? "Fresh Splash"
    : "Today’s Tickle";
  text.textContent = JOKES[i];
}

document.addEventListener("DOMContentLoaded", () => {
  // Load today's joke
  setJoke(todaysIndex(), "🗓️ Today");

  // Controls
  document.getElementById("btn-next").addEventListener("click", () => {
    // Next joke in list (wrap) — marked as "Another"
    const current = JOKES.indexOf(text.textContent);
    const next = (current + 1) % JOKES.length;
    setJoke(next, "💦 Another");
  });

  document.getElementById("btn-random").addEventListener("click", () => {
    let idx = Math.floor(Math.random()*JOKES.length);
    // avoid repeating current
    if (JOKES[idx] === text.textContent) idx = (idx + 1) % JOKES.length;
    setJoke(idx, "🔀 Random");
  });
});
