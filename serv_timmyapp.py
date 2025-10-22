# serv_timmyapp.py — ZERO-dependency glow (no templates/static needed)
import os
from flask import Flask, Response, jsonify

app = Flask(__name__)

INLINE = """<!doctype html><html lang="en"><head>
<meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>TimmyApp</title><meta name="theme-color" content="#7a3cff"/>
<meta property="og:title" content="TimmyApp is LIVE"/>
<meta property="og:description" content="Purple-pink glow, floating bubbles, and good vibes."/>
<style>
  html,body{margin:0;height:100%;overflow:hidden;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;color:#fff;
    background:
      radial-gradient(1200px 800px at 20% 20%, #ff66cc 0%, rgba(255,102,204,.25) 30%, transparent 60%),
      radial-gradient(1200px 800px at 80% 80%, #7a3cff 0%, rgba(122,60,255,.25) 30%, transparent 60%),
      #1a0f2b; animation:throb 6s ease-in-out infinite;}
  @keyframes throb{0%,100%{filter:brightness(1)}50%{filter:brightness(1.2)}}
  #bubbles{position:fixed;inset:0;width:100%;height:100%;display:block}
  .center{position:absolute;inset:0;display:grid;place-items:center;text-align:center;padding:2rem;pointer-events:none}
  h1{margin:0 0 .25rem;font-size:clamp(28px,6vw,56px);
     text-shadow:0 6px 24px rgba(255,102,204,.4),0 2px 10px rgba(122,60,255,.35)}
  .tag{opacity:.9}
</style>
</head><body>
<canvas id="bubbles"></canvas>
<div class="center">
  <h1>TimmyApp is LIVE</h1>
  <p class="tag">Purple-pink glow, floating bubbles, and good vibes.</p>
</div>
<script>
(function(){
  const c=document.getElementById('bubbles');
  const x=c.getContext('2d',{alpha:true});
  function size(){c.width=innerWidth;c.height=innerHeight}
  size(); addEventListener('resize',size,{passive:true});
  const N=Math.min(80,Math.floor((c.width*c.height)/30000));
  const R=(a,b)=>Math.random()*(b-a)+a;
  const B=[...Array(N)].map(()=>({x:R(0,c.width),y:R(0,c.height),r:R(6,22),a:R(.25,.9),vx:R(-.15,.15),vy:R(-.35,-.05),h:R
