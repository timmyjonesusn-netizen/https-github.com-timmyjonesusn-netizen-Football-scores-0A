const eateries = [
  "Mama Dee’s Southern Kitchen — Fried Catfish & Sweet Tea Heaven 🐟🍋",
  "The Biscuit Barn — Chicken, honey butter & Alabama pride 🍗🍯",
  "Big Earl’s Smokehouse — Ribs so good you’ll forget your manners 🍖🔥",
  "Lula Mae’s Café — Peach cobbler & gospel on Sundays 🍑🎶",
  "Grits & Gravy — Shrimp, hushpuppies, and porch swing hospitality 🍤🪶"
];

// daily rotation by calendar date
const today = new Date().getDate();
const eateryIndex = today % eateries.length;
document.getElementById("eatery-name").textContent = eateries[eateryIndex];

// manual random shuffle
document.getElementById("next-eatery").addEventListener("click", () => {
  const randomEatery = eateries[Math.floor(Math.random() * eateries.length)];
  document.getElementById("eatery-name").textContent = randomEatery;
});

