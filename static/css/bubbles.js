// =====================================
// 🫧 Timmy Bubbles — Interactive Verses
// =====================================

// Verse vault (clean, classy, Timmy swagger)
const VERSES = [
  "Keep your blessings louder than your bragging.",
  "Grace moves at the speed of swagger.",
  "A humble shine outlasts a loud flex.",
  "Peace is gangster — wear it daily.",
  "You can’t outrun purpose, Chief.",
  "When the hustle’s holy, Mondays feel divine.",
  "Talk less, glow more.",
  "Stay kind, stay sharp — let the haters choke on grace.",
  "The storm taught me a better dance.",
  "Protect your peace like it’s payroll.",
  "Build so solid even doubt can’t shake it.",
  "Faith that lifts others never runs out.",
  "Don’t flex what you can’t bless.",
  "If it costs your soul, it’s overpriced.",
  "Boundaries are love wearing steel-toed boots.",
  "The soft answer flips the hardest day.",
  "Shine steady — neon doesn’t need applause.",
  "You’re the seed and the season — grow.",
  "Favor finds those still doing the work.",
  "Forgiveness is freedom with better lighting."
];

// Deterministic “Verse of the Day”
function dayOfYear(d){
  const start = new Date(d.getFullYear(),0,0);
  return Math.floor((d - start)/86400000);
}
function verseOfTheDay(){
  const t = new Date();
  const idx = (t.getFullYear() * 400 + dayOfYear(t)) % VERSES.length;
  return { text: VERSES[idx], index: idx };
}

const SKY = document.getElementById("sky");
const TOAST = document.getElementById("verse-toast");

// Create a bubble element
function createBubble(text, { votd=false } = {}){
  const b = document.createElement("div");
  b.className = "bubble";
  if(votd) b.classList.add("votd");

  // Randomize size & speed
  const size = rand(70, 140) * (votd ? 1.15 : 1);
  b.style.width = size + "px";
  const x = rand(2, 98); // percent from left
  b.style.left = x + "vw";

  // Animation tuning
  const dur = rand(18, 36) * (votd ? 1.2 : 1);
  const delay = rand(0, 12);
  const startY = rand(20, 120) + "vh";   // start off-screen below
  const scale = (0.96 + Math.random() * 0.1).toFixed(3);

  b.style.setProperty("--startY", startY);
  b.style.setProperty("--scale", scale);
  b.style.animation = `floatUp ${dur}s linear ${delay}s forwards`;

  // Verse label inside
  const v = document.createElement("div");
  v.className = "verse";
  v.textContent = text;
  b.appendChild(v);

  // Click to pop -> toast the verse
  b.addEventListener("click", () => {
    popBubble(b, text);
  });

  // When bubble finishes floating, recycle it
  b.addEventListener("animationend", () => {
    b.remove();
    spawnOne(); // keep field populated
  });

  SKY.appendChild(b);
}

// Pop a bubble (visual burst + toast line)
function popBubble(el, text){
  try{
    el.classList.add("pop");
    setTimeout(() => el.remove(), 220);
  }catch(e){/* ignore */}

  showToast(text);
  // Immediately spawn another to keep density
  spawnOne();
}

// Toast display
let toastTimer = null;
function showToast(text){
  TOAST.textContent = `“${text}”`;
  TOAST.classList.add("show");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => {
    TOAST.classList.remove("show");
  }, 3000);
}

// Spawn helpers
function rand(min, max){ return Math.floor(Math.random()*(max-min+1))+min; }

function spawnOne(){
  // Pick a random verse (not necessarily unique)
  const text = VERSES[rand(0, VERSES.length-1)];
  createBubble(text);
}

function populateField(){
  // Initial population
  const baseCount = Math.min(18, Math.max(10, Math.floor(window.innerWidth / 60)));
  const votd = verseOfTheDay();
  // One special bubble for Verse of the Day
  createBubble(votd.text, { votd:true });

  for(let i=0;i<baseCount;i++){
    spawnOne();
  }
}

// Init
document.addEventListener("DOMContentLoaded", populateField);
window.addEventListener("resize", () => {
  // Optional: could adapt density on resize. Keeping it simple/steady.
});
