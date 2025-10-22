(()=> {
  const c = document.getElementById('bubbles');
  const ctx = c.getContext('2d', { alpha: true });
  let W, H, dpr;

  function size(){
    dpr = window.devicePixelRatio || 1;
    W = c.width = Math.floor(innerWidth*dpr);
    H = c.height = Math.floor(innerHeight*dpr);
    c.style.width = innerWidth+'px'; c.style.height = innerHeight+'px';
  }
  addEventListener('resize', size, {passive:true}); size();

  const N=36, R=(a,b)=>a+Math.random()*(b-a), bubbles=[];
  function make(){const r=R(10,70)*dpr;return{x:R(r,W-r),y:R(r,H-r),r,vx:R(-.12,.12)*dpr,vy:-R(.2,.9)*dpr,h:R(285,320),a:R(.15,.35),t:R(0,6.28)}}
  for(let i=0;i<N;i++) bubbles.push(make());

  function draw(b){
    const g=ctx.createRadialGradient(b.x,b.y,b.r*.1,b.x,b.y,b.r);
    g.addColorStop(0,`hsla(${b.h},80%,70%,${b.a})`); g.addColorStop(1,`hsla(${b.h},80%,20%,0)`);
    ctx.fillStyle=g; ctx.beginPath(); ctx.arc(b.x,b.y,b.r,0,Math.PI*2); ctx.fill();
    ctx.beginPath(); ctx.arc(b.x-b.r*.25,b.y-b.r*.25,b.r*.45,0,Math.PI*2);
    ctx.fillStyle=`hsla(${b.h},85%,85%,${b.a*.6})`; ctx.fill();
  }

  function tick(){
    ctx.clearRect(0,0,W,H);
    for(const b of bubbles){
      b.t+=.015; b.x+=b.vx+Math.sin(b.t)*.2*dpr; b.y+=b.vy+Math.cos(b.t*.8)*.1*dpr;
      if(b.y+b.r<0){Object.assign(b,make(),{y:H+b.r});}
      if(b.x-b.r<0||b.x+b.r>W) b.vx*=-1;
      draw(b);
    }
    requestAnimationFrame(tick);
  }
  tick();
})();
