// static/js/bubbles.js
(() => {
  const c = document.getElementById('bubble-canvas');
  if (!c) return;
  const ctx = c.getContext('2d');
  let W, H, bubbles=[];
  const N = 42;

  function size(){ W = c.width = window.innerWidth; H = c.height = window.innerHeight; }
  window.addEventListener('resize', size); size();

  function makeBubble(){
    const r = 6 + Math.random()*24;
    return {
      x: Math.random()*W,
      y: H + Math.random()*H*0.5,
      r,
      vy: 0.4 + Math.random()*1.1,
      vx: (Math.random()-0.5)*0.3,
      hue: Math.random()<.5 ? 285 : 315 // purple or pink
    };
  }

  bubbles = Array.from({length:N}, makeBubble);

  function step(){
    ctx.clearRect(0,0,W,H);
    for (const b of bubbles){
      b.y -= b.vy; b.x += b.vx;
      if (b.y < -b.r) Object.assign(b, makeBubble(), {y:H+b.r});
      const g = ctx.createRadialGradient(b.x, b.y, 1, b.x, b.y, b.r*1.4);
      g.addColorStop(0, `hsla(${b.hue},100%,70%,.8)`);
      g.addColorStop(1, `hsla(${b.hue},100%,70%,0)`);
      ctx.beginPath(); ctx.fillStyle = g;
      ctx.arc(b.x, b.y, b.r, 0, Math.PI*2); ctx.fill();

      // rim
      ctx.strokeStyle = `hsla(${b.hue},100%,85%,.35)`;
      ctx.lineWidth = 1; ctx.stroke();
    }
    requestAnimationFrame(step);
  }
  step();
})();
