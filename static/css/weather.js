// ☀️ Ragland Weather (°F) — no lat/long, public source
// Uses wttr.in JSON (free). If blocked by the client, shows a friendly fallback.

const T = document.getElementById("t");
const C = document.getElementById("c");
const TIME = document.getElementById("time");
const HOURS = document.getElementById("hours");

function fmtHour(s){
  // wttr returns "0", "300", "600" ... local-ish. We'll format to 12h.
  if(!s) return "";
  const n = parseInt(s, 10);
  const hh = Math.floor(n/100);
  const ampm = hh >= 12 ? "PM" : "AM";
  const h12 = ((hh + 11) % 12) + 1;
  return `${h12} ${ampm}`;
}

async function loadWeather(){
  try{
    const res = await fetch("https://wttr.in/Ragland?format=j1", {mode:"cors"});
    const data = await res.json();

    // Current
    const cur = data.current_condition?.[0];
    const tempF = cur?.temp_F ?? cur?.FeelsLikeF ?? "--";
    const cond  = cur?.weatherDesc?.[0]?.value ?? "Fair";
    T.textContent = tempF;
    C.textContent = cond;
    TIME.textContent = new Date().toLocaleTimeString([], {hour:'numeric', minute:'2-digit'});

    // Next hours (today)
    HOURS.innerHTML = "";
    const hours = (data.weather?.[0]?.hourly || []).slice(0, 8); // next ~24h in 3h steps
    hours.forEach(h => {
      const card = document.createElement("div");
      card.className = "hour";
      card.innerHTML = `
        <div class="h">${fmtHour(h.time)}</div>
        <div class="v">${h.tempF}°</div>
        <div class="c">${(h.weatherDesc?.[0]?.value)||""}</div>
      `;
      HOURS.appendChild(card);
    });

  }catch(e){
    T.textContent = "—";
    C.textContent = "Couldn’t reach weather service. Try again shortly.";
    TIME.textContent = new Date().toLocaleTimeString([], {hour:'numeric', minute:'2-digit'});
  }
}

document.addEventListener("DOMContentLoaded", loadWeather);
