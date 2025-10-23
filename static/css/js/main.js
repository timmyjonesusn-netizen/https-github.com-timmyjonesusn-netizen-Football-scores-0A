// Purple bubble field — lightweight, no libs
(function(){
  const c = document.getElementById('bubbles');
  const ctx = c.getContext('2d');
  let W, H, dots;

  function resize(){
    W = c.width = window.innerWidth;
    H = c.height = window.innerHeight;
    makeDots();
  }

  function makeDots(){
    const count = Math.min(120, Math.floor((W*H)/12000)); // “good amount” auto scales
    dots = Array.from({length: count}).map(()=>({
      x: Math.random()*W,
      y: Math.random()*H,
      r: 2 + Math.random()*6,
      vx: (Math.random()-.5)*0.3,
      vy: (Math.random()-.5)*0.6,
      a: 0.2 + Math.random()*0.5
    }));
  }

  function step(){
    ctx.clearRect(0,0,W,H);
    for (const d of dots){
      d.x += d.vx; d.y += d.vy;
      if (d.x<-10) d.x=W+10; if (d.x>W+10) d.x=-10;
      if (d.y<-10) d.y=H+10; if (d.y>H+10) d.y=-10;

      // soft pink/purple glow without specifying exact color values in CSS
      ctx.beginPath();
      ctx.arc(d.x, d.y, d.r, 0, Math.PI*2);
      ctx.fillStyle = `rgba(255, 120, 220, ${d.a})`;
      ctx.shadowBlur = 20;
      ctx.shadowColor = 'rgba(255,120,220,.6)';
      ctx.fill();
      ctx.shadowBlur = 0;
    }
    requestAnimationFrame(step);
  }

  window.addEventListener('resize', resize);
  resize(); step();
})();
