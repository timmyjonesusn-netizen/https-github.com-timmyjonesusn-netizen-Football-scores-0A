// Gentle background glow effect for extra life
setInterval(() => {
  document.body.style.background = `radial-gradient(circle at ${Math.random()*100}% ${Math.random()*100}%, #2b0040, #000)`;
}, 8000);

