(() => {
  const field = document.getElementById('bubble-field');
  if (!field) return;

  const COUNT = 28;                 // number of bubbles
  const minSize = 18;               // px
  const maxSize = 140;              // px
  const vh = () => Math.max(window.innerHeight, 600);

  // helper: random in range
  const rnd = (a,b) => a + Math.random()*(b-a);

  for (let i=0;i<COUNT;i++){
    const b = document.createElement('div');
    b.className = 'bubble';

    // size & horizontal lane
    const size = rnd(minSize, maxSize);
    const laneX = rnd(0, 100);          // %
    const sway = rnd(-15, 15) + 'vw';   // side wander
    const scale = rnd(.75, 1.35);

    // timings
    const riseDur = rnd(16, 42);        // seconds
    const driftDur = rnd(6, 12);
    const twinkleDur = rnd(4, 10);
    const delay = rnd(0, 18);

    // write CSS vars
    b.style.setProperty('--x', laneX + 'vw');
    b.style.setProperty('--sway', sway);
    b.style.setProperty('--s', scale.toFixed(3));

    // place + size
    b.style.left = laneX + 'vw';
    b.style.width = size + 'px';
    b.style.height = size + 'px';

    // animation
    b.style.animationDuration = `${riseDur}s, ${driftDur}s, ${twinkleDur}s`;
    b.style.animationDelay = `${delay}s, ${delay/2}s, ${delay/3}s`;

    field.appendChild(b);
  }

  // subtle parallax on scroll
  let lastY = 0;
  window.addEventListener('scroll', () => {
    const y = window.scrollY;
    const delta = (y - lastY) * 0.02;
    field.style.transform = `translateY(${ -y * 0.06 }px)`;
    lastY = y;
  }, {passive:true});

  // on resize, re-trigger a tiny layout change to keep the flow natural
  let t;
  window.addEventListener('resize', () => {
    clearTimeout(t);
    t = setTimeout(() => {
      field.style.opacity = '0.99';
      requestAnimationFrame(() => field.style.opacity = '1');
    }, 90);
  });
})();
