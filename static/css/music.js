// ======================================
// 🎶 TimmyTunes — Suno Playlist Control
// ======================================

const PLAYLISTS = [
  { name: "Neon Nights",  url: "https://suno.com/playlist/2ec04889-1c23-4e2d-9c27-8a2b6475da4b" },
  { name: "Vibe Supply",  url: "https://suno.com/playlist/06b80fa9-8c72-4e0a-b277-88d00c441316" },
  { name: "Spirit Drive", url: "https://suno.com/playlist/e95ddd12-7e37-43e2-b3e0-fe342085a19f" },
  { name: "Midnight Gospel", url: "https://suno.com/playlist/a2e8eb9c-2d15-44d9-831b-89bf66ede586" }
];

const btnAll = document.getElementById("btn-play-all");
const btnShuffle = document.getElementById("btn-shuffle");

// Some mobile browsers block multiple auto-opened tabs.
// We'll try with short delays; if blocked, user can tap cards individually.
btnAll.addEventListener("click", async () => {
  for (let i = 0; i < PLAYLISTS.length; i++) {
    const u = PLAYLISTS[i].url;
    // Open each in a new tab; small delay improves success chances on iOS
    window.open(u, "_blank", "noopener");
    // eslint-disable-next-line no-await-in-loop
    await sleep(300);
  }
});l

btnShuffle.addEventListener("click", () => {me
  const i = Math.floor(Math.random() * PLAYLISTS.length);
  window.open(PLAYLISTS[i].url, "_blank", "noopener");
});

function sleep(ms){ return new Promise(r => setTimeout(r, ms)); }
