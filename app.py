"""
╔══════════════════════════════════════════════════════════════╗
║      🎂 PREMIUM BIRTHDAY SURPRISE WEBSITE                   ║
║      Built with Python Streamlit + HTML/CSS/JavaScript      ║
║      Passcode: 04/06/2005  |  Dark Cinematic Theme          ║
╚══════════════════════════════════════════════════════════════╝
"""

import streamlit as st

# ── Page Configuration ─────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Happy Birthday ❤️",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Make the iframe cover the entire viewport ──────────────────────────────────
st.markdown("""
<style>
    #MainMenu { visibility: hidden; }
    footer     { visibility: hidden; }
    header     { visibility: hidden; }
    .stApp { overflow: hidden; height: 100vh; background: #05000f; }
    .main .block-container { padding: 0 !important; max-width: 100% !important; margin: 0 !important; }
    section[data-testid="stSidebar"] { display: none !important; }
    /* Lock the component iframe to full-screen */
    iframe {
        position: fixed !important;
        top: 0 !important; left: 0 !important;
        width: 100vw !important; height: 100vh !important;
        border: none !important; z-index: 9999 !important;
    }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#                         FULL HTML PAGE CONTENT
# ══════════════════════════════════════════════════════════════════════════════
HTML_PAGE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Happy Birthday Ankita ❤️</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,600;0,700;0,800;0,900;1,300&family=Dancing+Script:wght@600;700&family=Cinzel+Decorative:wght@400;700&display=swap" rel="stylesheet">

<style>
/* ═══════════════════════════════════════════════════
   ROOT VARIABLES & RESET
═══════════════════════════════════════════════════ */
:root {
  --pink:      #ff6b9d;
  --pink-dark: #e0447b;
  --purple:    #c44dff;
  --blue:      #4d79ff;
  --cyan:      #00d4ff;
  --gold:      #ffd700;
  --dark:      #05000f;
  --dark2:     #0d0020;
  --glass:     rgba(255,255,255,0.055);
  --glass-b:   rgba(255,255,255,0.14);
  --gp: 0 0 16px rgba(255,107,157,.75), 0 0 36px rgba(255,107,157,.35), 0 0 70px rgba(255,107,157,.15);
  --gu: 0 0 16px rgba(196,77,255,.75),  0 0 36px rgba(196,77,255,.35);
  --gb: 0 0 16px rgba(77,121,255,.75),  0 0 36px rgba(77,121,255,.35);
}
*, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
html { scroll-behavior: smooth; }
body {
  font-family: 'Poppins', sans-serif;
  background: var(--dark);
  color: #fff;
  overflow-x: hidden;
}
/* cursor:none must cover html+body+* — body alone misses the html root in some browsers */
html, body, * { cursor: none !important; }

/* ─── CUSTOM CURSOR ──────────────────────────────── */
#cur {
  position: fixed; top: 0; left: 0;      /* explicit origin — no layout flash */
  width: 10px; height: 10px;
  background: var(--pink); border-radius: 50%;
  pointer-events: none;
  z-index: 2147483647;                    /* absolute maximum — nothing sits above this */
  will-change: transform;                 /* own GPU compositing layer */
  box-shadow: var(--gp);
}
#cur2 {
  position: fixed; top: 0; left: 0;
  width: 28px; height: 28px;
  border: 1.5px solid rgba(255,107,157,.45); border-radius: 50%;
  pointer-events: none;
  z-index: 2147483646;
  will-change: transform;
}

/* ═══════════════════════════════════════════════════
   LOCK SCREEN
═══════════════════════════════════════════════════ */
#lockScreen {
  position:fixed; inset:0; z-index:500;
  display:flex; align-items:center; justify-content:center;
  overflow:hidden;
  background: radial-gradient(ellipse at 60% 40%, #1f0040 0%, #05000f 65%);
}
#pCanvas { position:absolute; inset:0; pointer-events:none; }

/* floating hearts / balloons */
.fheart, .fball {
  position:absolute; pointer-events:none;
  animation: floatUp linear infinite; opacity:0;
}
@keyframes floatUp {
  0%  { transform:translateY(105vh) rotate(0deg) scale(.6); opacity:0; }
  8%  { opacity:.85; }
  92% { opacity:.4; }
  100%{ transform:translateY(-8vh)  rotate(360deg) scale(1.3); opacity:0; }
}

/* ── GLASSMORPHISM CARD ───────────────────────────── */
.lcard {
  position:relative; z-index:10;
  background: rgba(255,255,255,.035);
  backdrop-filter: blur(22px);
  -webkit-backdrop-filter: blur(22px);
  border: 1px solid rgba(255,107,157,.28);
  border-radius: 32px;
  padding: 52px 46px 44px;
  width: min(430px, 92vw);
  text-align:center;
  box-shadow: 0 0 50px rgba(196,77,255,.18),
              0 0 100px rgba(255,107,157,.08),
              inset 0 1px 0 rgba(255,255,255,.09);
  animation: cPulse 4s ease-in-out infinite;
}
@keyframes cPulse {
  0%,100%{ box-shadow:0 0 50px rgba(196,77,255,.18),0 0 100px rgba(255,107,157,.08),inset 0 1px 0 rgba(255,255,255,.09); }
  50%    { box-shadow:0 0 70px rgba(196,77,255,.32),0 0 140px rgba(255,107,157,.18),inset 0 1px 0 rgba(255,255,255,.09); }
}
.lcard::before {
  content:''; position:absolute; inset:-1px; border-radius:33px;
  background:linear-gradient(135deg,rgba(255,107,157,.2),rgba(196,77,255,.15),rgba(77,121,255,.1));
  z-index:-1; pointer-events:none;
}
.lstar { position:absolute; top:-18px; left:50%; transform:translateX(-50%);
  font-size:1.1rem; letter-spacing:6px;
  animation:starT 2s ease-in-out infinite; }
@keyframes starT { 0%,100%{opacity:1;filter:brightness(1)} 50%{opacity:.5;filter:brightness(2.5)} }

.licon {
  width:82px; height:82px; margin:0 auto 22px;
  background:linear-gradient(135deg,var(--purple),var(--pink));
  border-radius:50%; display:flex; align-items:center; justify-content:center;
  font-size:2.1rem; box-shadow:var(--gu);
  animation: iconBeat 2s ease-in-out infinite;
}
@keyframes iconBeat {
  0%,100%{ transform:scale(1); }
  40%    { transform:scale(1.12) rotate(-6deg); }
  60%    { transform:scale(1.08) rotate(4deg); }
}
.ltitle {
  font-size:1.85rem; font-weight:800; letter-spacing:-.4px;
  background:linear-gradient(135deg,#fff 0%,var(--pink) 50%,var(--purple) 100%);
  -webkit-background-clip:text; -webkit-text-fill-color:transparent;
  background-clip:text; margin-bottom:6px;
}
.lsub { font-size:.88rem; color:rgba(255,255,255,.42); margin-bottom:34px; font-weight:300; }

/* neon input */
.iwrap { position:relative; margin-bottom:18px; }
.iwrap::before {
  content:''; position:absolute; inset:-2px; border-radius:16px;
  background:linear-gradient(135deg,var(--pink),var(--purple),var(--blue));
  z-index:-1; opacity:0; filter:blur(5px); transition:opacity .3s;
}
.iwrap:focus-within::before { opacity:1; }
#pInput {
  width:100%; padding:16px 20px;
  font-size:1.15rem; font-family:'Poppins',sans-serif; font-weight:700;
  letter-spacing:5px; text-align:center;
  background:rgba(255,255,255,.055);
  border:1.5px solid rgba(255,107,157,.38);
  border-radius:14px; color:#fff; outline:none;
  transition:all .3s; caret-color:var(--pink);
}
#pInput::placeholder { letter-spacing:2px; font-weight:300; color:rgba(255,255,255,.28); }
#pInput:focus { border-color:var(--pink); box-shadow:var(--gp); background:rgba(255,107,157,.07); }
#pInput.err { border-color:#ff4444; box-shadow:0 0 18px rgba(255,68,68,.55); animation:shake .45s ease; }
@keyframes shake {
  0%,100%{transform:translateX(0)} 20%{transform:translateX(-10px)}
  40%{transform:translateX(10px)} 60%{transform:translateX(-7px)} 80%{transform:translateX(7px)}
}
.ulbtn {
  width:100%; padding:16px; font-size:1.05rem; font-family:'Poppins',sans-serif;
  font-weight:700; letter-spacing:.8px;
  background:linear-gradient(135deg,var(--pink),var(--purple));
  border:none; border-radius:14px; color:#fff; cursor:pointer;
  position:relative; overflow:hidden; transition:all .3s;
  box-shadow:var(--gp);
}
.ulbtn::after {
  content:''; position:absolute; top:0; left:-100%;
  width:100%; height:100%;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.22),transparent);
  transition:left .55s;
}
.ulbtn:hover::after { left:110%; }
.ulbtn:hover { transform:translateY(-2px); box-shadow:0 12px 36px rgba(255,107,157,.5),var(--gp); }
.ulbtn:active { transform:translateY(0); }
#errMsg { margin-top:14px; font-size:.82rem; color:#ff7eb3; min-height:18px; }
.hint { margin-top:18px; font-size:.72rem; color:rgba(255,255,255,.22); font-style:italic; }

/* ═══════════════════════════════════════════════════
   FIREWORKS OVERLAY
═══════════════════════════════════════════════════ */
#fwOverlay {
  position:fixed; inset:0; z-index:600; display:none; pointer-events:none;
}
#fwCanvas { width:100%; height:100%; }

/* ═══════════════════════════════════════════════════
   BIRTHDAY PAGE
═══════════════════════════════════════════════════ */
#bPage {
  display:none; min-height:100vh;
  overflow-y:auto; overflow-x:hidden;
  position:relative;
}
#bgC { position:fixed; inset:0; z-index:0; pointer-events:none; }
.pcnt { position:relative; z-index:1; }

/* ── HERO ────────────────────────────────────────── */
.hero {
  min-height:100vh; display:flex; flex-direction:column;
  align-items:center; justify-content:center;
  text-align:center; padding:60px 20px 80px; position:relative; overflow:hidden;
}
.hero::before {
  content:''; position:absolute; top:50%; left:50%;
  transform:translate(-50%,-50%);
  width:700px; height:700px;
  background:radial-gradient(ellipse,rgba(196,77,255,.14) 0%,transparent 68%);
  animation:hPulse 5s ease-in-out infinite; pointer-events:none;
}
@keyframes hPulse {
  0%,100%{transform:translate(-50%,-50%) scale(1); opacity:.7}
  50%{transform:translate(-50%,-50%) scale(1.25); opacity:1}
}
.badge {
  display:inline-block; padding:8px 22px;
  background:rgba(255,107,157,.12);
  border:1px solid rgba(255,107,157,.4);
  border-radius:50px; font-size:.8rem; font-weight:700;
  color:var(--pink); letter-spacing:3px; text-transform:uppercase;
  margin-bottom:32px;
  animation:fdU 1s ease both; box-shadow:var(--gp);
}
.htitle {
  font-family:'Dancing Script',cursive;
  font-size:clamp(3.2rem,11vw,7.5rem); font-weight:700;
  line-height:1.05; margin-bottom:28px;
  animation:fdU 1s .3s ease both;
  background:linear-gradient(135deg,#fff 0%,var(--pink) 38%,var(--purple) 68%,var(--blue) 100%);
  -webkit-background-clip:text; -webkit-text-fill-color:transparent;
  background-clip:text;
  filter:drop-shadow(0 0 35px rgba(255,107,157,.42));
}
.htyping {
  font-size:clamp(1rem,3.2vw,1.45rem); font-weight:300;
  color:rgba(255,255,255,.82); min-height:2.2rem;
  animation:fdU 1s .6s ease both; margin-bottom:18px;
}
.cblink { display:inline-block; width:2px; height:1.15em;
  background:var(--pink); margin-left:3px;
  animation:blink 1s step-end infinite; vertical-align:middle; }
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }
.hmsg {
  font-size:clamp(.88rem,2.4vw,1rem); color:rgba(255,255,255,.48);
  max-width:560px; line-height:1.9; margin-bottom:44px;
  font-style:italic; animation:fdU 1s .9s ease both;
}
.scroll-ind {
  position:absolute; bottom:36px; left:50%; transform:translateX(-50%);
  color:rgba(255,255,255,.32); font-size:.72rem; letter-spacing:3px;
  text-transform:uppercase; animation:bounce 2.2s ease-in-out infinite;
}
.scroll-ind .arr {
  display:block; width:18px; height:18px; margin:7px auto 0;
  border-right:2px solid rgba(255,255,255,.32);
  border-bottom:2px solid rgba(255,255,255,.32);
  transform:rotate(45deg);
}
@keyframes bounce {
  0%,100%{transform:translateX(-50%) translateY(0)}
  50%{transform:translateX(-50%) translateY(10px)}
}

/* ── SECTION COMMONS ─────────────────────────────── */
.sec { padding:90px 20px; max-width:1080px; margin:0 auto; position:relative; }
.slabel {
  display:block; text-align:center; font-size:.75rem;
  letter-spacing:4px; text-transform:uppercase; color:var(--pink); margin-bottom:14px;
}
.stitle {
  text-align:center; font-size:clamp(1.75rem,5vw,3rem); font-weight:800;
  margin-bottom:12px;
  background:linear-gradient(135deg,#fff,rgba(255,255,255,.65));
  -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
}
.sdiv {
  width:78px; height:3px; margin:0 auto 56px;
  background:linear-gradient(90deg,var(--pink),var(--purple));
  border-radius:3px; box-shadow:var(--gp);
}
.reveal { opacity:0; transform:translateY(55px); transition:opacity .85s ease, transform .85s ease; }
.reveal.vis { opacity:1; transform:translateY(0); }

/* ── CAKE ────────────────────────────────────────── */
.csec { text-align:center; }
.cakeWrap { display:inline-block; position:relative; margin:30px auto; }

.candles { display:flex; justify-content:center; gap:18px; position:relative; z-index:5; }
.candle  { position:relative; width:13px; }
.cbody   { width:13px; height:38px; border-radius:6px 6px 0 0; }
.flame   {
  position:absolute; top:-20px; left:50%; transform:translateX(-50%);
  width:11px; height:20px;
  background:linear-gradient(180deg,#fff 0%,#ffd700 40%,#ff6b00 72%,transparent 100%);
  border-radius:50% 50% 30% 30%;
  animation:flicker .28s ease-in-out infinite alternate;
  box-shadow:0 0 12px rgba(255,200,0,.85), 0 0 24px rgba(255,100,0,.4);
}
@keyframes flicker {
  0% {transform:translateX(-50%) scaleX(1)   scaleY(1)   rotate(-2deg);}
  100%{transform:translateX(-50%) scaleX(.88) scaleY(1.12) rotate(2deg);}
}
.fglow {
  position:absolute; top:-4px; left:50%; transform:translateX(-50%);
  width:22px; height:28px;
  background:radial-gradient(ellipse,rgba(255,200,0,.42) 0%,transparent 70%);
  border-radius:50%; animation:gP .45s ease-in-out infinite alternate;
}
@keyframes gP { 0%{opacity:.5;transform:translateX(-50%) scale(1)} 100%{opacity:1;transform:translateX(-50%) scale(1.35)} }

.cake { position:relative; width:210px; margin:0 auto; }
.tier { position:relative; border-radius:10px 10px 6px 6px; margin:0 auto; overflow:hidden; }
.tier::before { content:''; position:absolute; inset:0;
  background:linear-gradient(90deg,rgba(255,255,255,.1) 0%,transparent 45%,rgba(255,255,255,.05) 100%); }
.t3 { width:210px; height:72px;
  background:linear-gradient(180deg,#ff6b9d,#d63070);
  box-shadow:0 6px 22px rgba(255,107,157,.55),var(--gp); }
.t2 { width:168px; height:63px;
  background:linear-gradient(180deg,#c44dff,#9427cc);
  box-shadow:0 6px 22px rgba(196,77,255,.55),var(--gu); }
.t1 { width:120px; height:52px;
  background:linear-gradient(180deg,#4d79ff,#2d54c4);
  box-shadow:0 6px 22px rgba(77,121,255,.55),var(--gb); }
.frost {
  position:absolute; top:-9px; left:0; width:100%; height:18px;
  background:rgba(255,255,255,.88); border-radius:50% 50% 0 0 / 100% 100% 0 0;
}
.frost::after {
  content:''; position:absolute; bottom:-14px; left:8%; width:84%; height:16px;
  background:inherit;
  clip-path:polygon(0 0,8% 100%,16% 0,24% 100%,32% 0,40% 100%,48% 0,56% 100%,64% 0,72% 100%,80% 0,88% 100%,96% 0,100% 0);
}
.tage {
  position:absolute; top:50%; left:50%;
  transform:translate(-50%,-50%);
  font-family:'Dancing Script',cursive; font-size:2.4rem; font-weight:700;
  color:rgba(255,255,255,.92); text-shadow:0 2px 8px rgba(0,0,0,.5);
}
.tlabel {
  position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
  font-size:.6rem; letter-spacing:2px; color:rgba(255,255,255,.72); font-weight:700;
  white-space:nowrap;
}
.cakeGlow {
  position:absolute; inset:-20px; z-index:-1;
  background:radial-gradient(ellipse,rgba(255,107,157,.18) 0%,transparent 70%);
  animation:hPulse 3s ease-in-out infinite;
}

/* ── SURPRISE BTN ────────────────────────────────── */
.ssec { text-align:center; }
.sbtn {
  display:inline-block; padding:22px 58px;
  font-size:1.18rem; font-family:'Poppins',sans-serif;
  font-weight:700; letter-spacing:.8px;
  background:linear-gradient(135deg,var(--pink),var(--purple),var(--blue));
  background-size:200% 200%;
  animation:gShift 3.5s ease infinite;
  border:none; border-radius:50px; color:#fff; cursor:pointer;
  position:relative; overflow:hidden;
  box-shadow:var(--gp); transition:transform .3s, box-shadow .3s;
}
@keyframes gShift { 0%{background-position:0% 50%} 50%{background-position:100% 50%} 100%{background-position:0% 50%} }
.sbtn:hover { transform:translateY(-5px) scale(1.04); box-shadow:0 22px 55px rgba(255,107,157,.52),var(--gp); }
.sbtn::before {
  content:''; position:absolute; top:0; left:-100%; width:60%; height:100%;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.28),transparent);
  animation:shine 2.8s ease infinite;
}
@keyframes shine { 0%{left:-100%} 100%{left:160%} }

/* confetti canvas */
#cCanvas { position:fixed; inset:0; pointer-events:none; z-index:800; display:none; }

/* popup */
#sPopup {
  display:none; position:fixed; inset:0; z-index:900;
  background:rgba(5,0,15,.88); backdrop-filter:blur(12px);
  align-items:center; justify-content:center;
}
#sPopup.on { display:flex; }
.popcard {
  background:rgba(255,255,255,.045);
  backdrop-filter:blur(30px); -webkit-backdrop-filter:blur(30px);
  border:1px solid rgba(255,107,157,.38); border-radius:32px;
  padding:52px 42px; width:min(500px,90vw);
  text-align:center;
  box-shadow:0 0 70px rgba(255,107,157,.28),0 0 130px rgba(196,77,255,.14);
  animation:popIn .5s cubic-bezier(.34,1.56,.64,1) both;
  position:relative; overflow:hidden;
}
.popcard::before {
  content:''; position:absolute; top:-50%; left:-50%; width:200%; height:200%;
  background:conic-gradient(transparent,rgba(255,107,157,.04),transparent 30%);
  animation:rot 5s linear infinite;
}
@keyframes rot { 100%{transform:rotate(360deg)} }
@keyframes popIn {
  0%{opacity:0;transform:scale(.45) rotate(-6deg)}
  100%{opacity:1;transform:scale(1) rotate(0deg)}
}
.pemo { font-size:3.8rem; margin-bottom:14px; animation:wgl 1.2s ease-in-out infinite; }
@keyframes wgl { 0%,100%{transform:rotate(-6deg)} 50%{transform:rotate(6deg)} }
.ptitle {
  font-family:'Dancing Script',cursive; font-size:2.6rem; font-weight:700;
  background:linear-gradient(135deg,var(--pink),var(--purple));
  -webkit-background-clip:text; -webkit-text-fill-color:transparent;
  background-clip:text; margin-bottom:14px;
}
.pmsg { font-size:.96rem; color:rgba(255,255,255,.72); line-height:1.85; margin-bottom:30px; }
.pclose {
  padding:12px 38px;
  background:linear-gradient(135deg,var(--pink),var(--purple));
  border:none; border-radius:50px; color:#fff;
  font-family:'Poppins',sans-serif; font-weight:600; font-size:.93rem;
  cursor:pointer; box-shadow:var(--gp); transition:transform .2s;
}
.pclose:hover { transform:scale(1.06); }

/* ── GALLERY ─────────────────────────────────────── */
.ggrid {
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:18px; margin-top:56px;
}
.gcard {
  position:relative; border-radius:22px; overflow:hidden;
  aspect-ratio:4/5; background:var(--glass);
  border:1px solid var(--glass-b);
  cursor:pointer;
  transition:transform .42s cubic-bezier(.34,1.56,.64,1), box-shadow .4s;
}
.gcard::after {
  content:''; position:absolute; inset:0;
  background:linear-gradient(180deg,transparent 38%,rgba(5,0,15,.88) 100%);
  z-index:1; opacity:0; transition:opacity .32s;
}
.gcard:hover::after { opacity:1; }
.gcard:hover {
  transform:translateY(-10px) scale(1.02);
  box-shadow:0 22px 55px rgba(255,107,157,.28), 0 0 0 2px rgba(255,107,157,.38);
}
.gcard img {
  width:100%; height:100%; object-fit:cover;
  transition:transform .52s ease; filter:brightness(.82) saturate(1.25);
}
.gcard:hover img { transform:scale(1.09); }
.gcap {
  position:absolute; bottom:18px; left:16px; right:16px; z-index:2;
  font-size:.88rem; font-weight:600; color:rgba(255,255,255,.88);
  opacity:0; transform:translateY(10px);
  transition:opacity .32s, transform .32s;
}
.gcard:hover .gcap { opacity:1; transform:translateY(0); }
.gcard.feat { grid-column:span 2; aspect-ratio:16/9; }
@media(max-width:600px) {
  .ggrid { grid-template-columns:1fr 1fr; }
  .gcard.feat { grid-column:span 2; aspect-ratio:16/9; }
}
@media(max-width:420px) {
  .ggrid { grid-template-columns:1fr; }
  .gcard.feat { grid-column:span 1; aspect-ratio:4/5; }
}

/* ── QUOTES ──────────────────────────────────────── */
.qsec { text-align:center; }
.qcont {
  position:relative; max-width:680px;
  margin:56px auto 0; min-height:220px;
  display:flex; align-items:center; justify-content:center;
}
.qslide {
  position:absolute; inset:0; display:flex; flex-direction:column;
  align-items:center; justify-content:center;
  padding:36px; opacity:0; transition:opacity .75s ease, transform .75s ease;
  transform:translateX(50px);
}
.qslide.qon { opacity:1; transform:translateX(0); position:relative; }
.qslide.qout { opacity:0; transform:translateX(-50px); }
.qmark {
  font-size:5rem; line-height:.45;
  font-family:'Dancing Script',cursive;
  background:linear-gradient(135deg,var(--pink),var(--purple));
  -webkit-background-clip:text; -webkit-text-fill-color:transparent;
  background-clip:text; margin-bottom:18px;
}
.qtxt {
  font-size:clamp(.96rem,3vw,1.32rem); font-weight:300;
  font-style:italic; color:rgba(255,255,255,.82);
  line-height:1.75; margin-bottom:22px;
}
.qauth { font-size:.8rem; color:var(--pink); letter-spacing:2px; text-transform:uppercase; font-weight:600; }
.qdots { display:flex; gap:7px; justify-content:center; margin-top:26px; }
.qdot {
  width:8px; height:8px; border-radius:50%;
  background:rgba(255,255,255,.18); transition:all .35s; cursor:pointer;
}
.qdot.don { background:var(--pink); width:22px; border-radius:4px; box-shadow:var(--gp); }

/* ── COUNTDOWN ───────────────────────────────────── */
.cdsec { text-align:center; }
.cdgrid {
  display:flex; justify-content:center; gap:18px;
  margin-top:56px; flex-wrap:wrap;
}
.cdcard {
  background:var(--glass); backdrop-filter:blur(20px);
  border:1px solid var(--glass-b);
  border-radius:22px; padding:30px 24px;
  min-width:108px; text-align:center; position:relative; overflow:hidden;
  transition:transform .3s, box-shadow .3s;
}
.cdcard:hover { transform:translateY(-6px); box-shadow:var(--gp); }
.cdcard::before {
  content:''; position:absolute; inset:-1px; border-radius:22px;
  background:linear-gradient(135deg,var(--pink),var(--purple),var(--blue));
  z-index:-1; opacity:.24;
}
.cdnum {
  font-size:2.9rem; font-weight:900; display:block; line-height:1;
  background:linear-gradient(135deg,#fff,var(--pink));
  -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
  margin-bottom:7px;
}
.cdlbl { font-size:.72rem; letter-spacing:2.5px; text-transform:uppercase; color:rgba(255,255,255,.45); }
.cdnote { margin-top:28px; font-size:.94rem; color:rgba(255,255,255,.48); font-style:italic; }

/* ── WISHES MARQUEE ──────────────────────────────── */
.wsec { text-align:center; overflow:hidden; }
.wtrack {
  display:flex; gap:16px; width:max-content;
  animation:wScroll 28s linear infinite; margin-top:46px;
}
.wtrack:hover { animation-play-state:paused; }
@keyframes wScroll { 0%{transform:translateX(0)} 100%{transform:translateX(-50%)} }
.wbub {
  background:var(--glass); backdrop-filter:blur(14px);
  border:1px solid var(--glass-b);
  border-radius:50px; padding:14px 24px;
  white-space:nowrap; font-size:.93rem;
  color:rgba(255,255,255,.75);
  transition:all .32s; flex-shrink:0;
}
.wbub:hover {
  background:rgba(255,107,157,.1);
  border-color:rgba(255,107,157,.4); color:#fff; box-shadow:var(--gp);
}

/* ── MUSIC PLAYER ────────────────────────────────── */
#mplayer {
  position:fixed; bottom:28px; right:28px; z-index:400;
  background:rgba(255,255,255,.045);
  backdrop-filter:blur(22px); -webkit-backdrop-filter:blur(22px);
  border:1px solid rgba(255,107,157,.28);
  border-radius:22px; padding:14px 18px;
  display:none; align-items:center; gap:14px;
  box-shadow:0 12px 36px rgba(0,0,0,.55),var(--gp);
  animation:mSlide .55s ease 1.2s both;
}
#mplayer.show { display:flex; }
@keyframes mSlide { from{transform:translateX(160%);opacity:0} to{transform:translateX(0);opacity:1} }
.mart {
  width:44px; height:44px; border-radius:50%;
  background:linear-gradient(135deg,var(--pink),var(--purple));
  display:flex; align-items:center; justify-content:center;
  font-size:1.2rem; box-shadow:var(--gp);
  animation:spin 4.5s linear infinite; animation-play-state:paused;
}
.mart.pl { animation-play-state:running; }
@keyframes spin { 100%{transform:rotate(360deg)} }
.minfo { flex:1; min-width:0; }
.mtitle { font-size:.78rem; font-weight:600; color:#fff; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
.martist { font-size:.68rem; color:rgba(255,255,255,.45); }
.mctrl { display:flex; align-items:center; gap:9px; }
.pbtn {
  width:34px; height:34px;
  background:linear-gradient(135deg,var(--pink),var(--purple));
  border:none; border-radius:50%; color:#fff; font-size:.78rem;
  cursor:pointer; display:flex; align-items:center; justify-content:center;
  box-shadow:var(--gp); transition:transform .2s;
}
.pbtn:hover { transform:scale(1.12); }
.vslider {
  -webkit-appearance:none; width:58px; height:3px;
  background:rgba(255,255,255,.18); border-radius:3px; outline:none;
}
.vslider::-webkit-slider-thumb {
  -webkit-appearance:none; width:11px; height:11px;
  background:var(--pink); border-radius:50%; cursor:pointer; box-shadow:var(--gp);
}
@media(max-width:768px) {
  #mplayer { bottom:14px; right:14px; left:14px; }
  .vslider { display:none; }
}

/* ── FOOTER ──────────────────────────────────────── */
.foot {
  text-align:center; padding:60px 20px;
  border-top:1px solid rgba(255,255,255,.055);
}
.foot-h { font-size:2rem; animation:hb 1.6s ease-in-out infinite; }
@keyframes hb { 0%,100%{transform:scale(1)} 50%{transform:scale(1.32)} }
.foot-t { font-size:.88rem; color:rgba(255,255,255,.32); margin-top:14px; font-style:italic; }

/* ── GENERAL ANIMATIONS ──────────────────────────── */
@keyframes fdU { from{opacity:0;transform:translateY(30px)} to{opacity:1;transform:translateY(0)} }
@keyframes fdD { from{opacity:0;transform:translateY(-30px)} to{opacity:1;transform:translateY(0)} }

/* sparkle trail */
.spk {
  position:fixed; pointer-events:none; z-index:99997;
  font-size:.9rem;
  animation:spkf .75s ease forwards;
}
@keyframes spkf {
  0%  { opacity:1; transform:scale(1) translate(0,0) rotate(0deg); }
  100%{ opacity:0; transform:scale(0) translate(var(--dx),var(--dy)) rotate(360deg); }
}

/* scrollbar */
::-webkit-scrollbar { width:4px; }
::-webkit-scrollbar-track { background:transparent; }
::-webkit-scrollbar-thumb { background:linear-gradient(var(--pink),var(--purple)); border-radius:4px; }
</style>
</head>
<body>

<!-- Custom cursor -->
<div id="cur"></div>
<div id="cur2"></div>
</body>
</html>

<!-- ╔══════════════════════════════════╗
     ║       LOCK SCREEN               ║
     ╚══════════════════════════════════╝ -->
<div id="lockScreen">
  <canvas id="pCanvas"></canvas>
  <div id="floats"></div>

  <div class="lcard">
    <div class="lstar">✦ ✦ ✦</div>
    <div class="licon">🎂</div>
    <h1 class="ltitle">Secret Surprise</h1>
    <p class="lsub">Enter the special date to unlock ✨</p>

    <div class="iwrap">
      <input id="pInput" type="text" placeholder="DD/MM/YYYY"
             maxlength="10" autocomplete="off" spellcheck="false">
    </div>

    <button class="ulbtn" id="ulBtn" onclick="checkCode()">🔓 Unlock the Surprise</button>
    <p id="errMsg"></p>
    <p class="hint">Hint: A very special birthday date 💝</p>
  </div>
</div>

<!-- ╔══════════════════════════════════╗
     ║     FIREWORKS OVERLAY           ║
     ╚══════════════════════════════════╝ -->
<div id="fwOverlay"><canvas id="fwCanvas"></canvas></div>

<!-- ╔══════════════════════════════════╗
     ║     BIRTHDAY PAGE               ║
     ╚══════════════════════════════════╝ -->
<div id="bPage">
  <canvas id="bgC"></canvas>
  <canvas id="cCanvas"></canvas>

  <!-- ── Surprise Popup ── -->
  <div id="sPopup">
    <div class="popcard">
      <div class="pemo">🎁</div>
      <div class="ptitle">A Message From My Heart 💌</div>
      <p class="pmsg">
        On this magical day, I want you to know something beautiful...<br><br>
        Every memory we share is precious to me, and your presence brings a kind of happiness that words can never fully describe. ❤️ <br><br>
        You deserve every good thing life has to offer — all the love, all the joy,
        all the laughter. Today, tomorrow, always. 🌹<br><br>
        <strong style="color:var(--pink);">Happy Birthday, Ankita . This day was made for YOU. ✨</strong>
      </p>
      <button class="pclose" onclick="closePopup()">Close with Love 💕</button>
    </div>
  </div>

  <div class="pcnt">

    <!-- ── HERO ── -->
    <div class="hero">
      <div class="badge">✨ &nbsp;Your Special Day&nbsp; ✨</div>
      <h1 class="htitle">Happy Birthday Ankita ❤️</h1>
      <div class="htyping">
        <span id="tText"></span><span class="cblink"></span>
      </div>
      <p class="hmsg">
        On this day, the universe conspired to bring you into this world...<br>
        and into my life. Thank you for existing, and for making everything brighter. 🌙
      </p>
      <div id="hHrts"></div>
      <div class="scroll-ind">Scroll<span class="arr"></span></div>
    </div>

    <!-- ── CAKE SECTION ── -->
    <section class="sec csec reveal">
      <span class="slabel">🎂 Make a Wish</span>
      <h2 class="stitle">Blow the Candles</h2>
      <div class="sdiv"></div>

      <div class="cakeWrap" id="cakeWrap">
        <div class="cakeGlow"></div>
        <!-- Candles -->
        <div class="candles">
          <div class="candle"><div class="fglow"></div><div class="flame"></div><div class="cbody" style="background:linear-gradient(180deg,#ffccdd,var(--pink))"></div></div>
          <div class="candle"><div class="fglow"></div><div class="flame"></div><div class="cbody" style="background:linear-gradient(180deg,#e0f7fa,#00bcd4)"></div></div>
          <div class="candle"><div class="fglow"></div><div class="flame"></div><div class="cbody" style="background:linear-gradient(180deg,#f3e5f5,var(--purple))"></div></div>
          <div class="candle"><div class="fglow"></div><div class="flame"></div><div class="cbody" style="background:linear-gradient(180deg,#e8f5e9,#4caf50)"></div></div>
          <div class="candle"><div class="fglow"></div><div class="flame"></div><div class="cbody" style="background:linear-gradient(180deg,#fff9c4,#ffc107)"></div></div>
        </div>
        <!-- Tiers -->
        <div class="cake">
          <div class="tier t1">
            <div class="frost" style="background:rgba(255,255,255,.88)"></div>
            <div class="tlabel">TOP TIER 🌟</div>
          </div>
          <div class="tier t2">
            <div class="frost" style="background:rgba(255,255,255,.88)"></div>
            <div class="tage">21</div>
          </div>
          <div class="tier t3">
            <div class="frost" style="background:rgba(255,255,255,.88)"></div>
            <div class="tlabel">HAPPY BDAY 🎉</div>
          </div>
        </div>
      </div>
      <p style="margin-top:26px;color:rgba(255,255,255,.42);font-style:italic;font-size:.88rem">
        Close your eyes... Make a wish 🌟 It's going to come true.
      </p>
    </section>

    <!-- ── SURPRISE BUTTON ── -->
    <section class="sec ssec reveal">
      <span class="slabel">🎁 Just for You</span>
      <h2 class="stitle">A Little Surprise</h2>
      <div class="sdiv"></div>
      <p style="color:rgba(255,255,255,.42);margin-bottom:40px;font-size:.93rem">
        I've been keeping something special... just for this moment.
      </p>
      <button class="sbtn" onclick="openSurprise()">🎁 &nbsp;Click for Surprise</button>
    </section>

    <!-- ── PHOTO GALLERY ── -->
    <section class="sec reveal">
      <span class="slabel">📸 Memories</span>
      <h2 class="stitle">Beautiful Moments</h2>
      <div class="sdiv"></div>
      <div class="ggrid">
        <div class="gcard feat">
          <img src="image/first.jpeg" alt="Our Story" loading="lazy">
          <div class="gcap">💕 Our Story Begins Here</div>
        </div>
        <div class="gcard">
          <img src="https://picsum.photos/seed/bday-a/400/500" alt="Memory" loading="lazy">
          <div class="gcap">🌸 Beautiful Soul</div>
        </div>
        <div class="gcard">
          <img src="https://picsum.photos/seed/bday-b/400/500" alt="Memory" loading="lazy">
          <div class="gcap">✨ Magic Moments</div>
        </div>
        <div class="gcard">
          <img src="https://picsum.photos/seed/bday-c/400/500" alt="Memory" loading="lazy">
          <div class="gcap">🎉 Celebrating You</div>
        </div>
        <div class="gcard">
          <img src="https://picsum.photos/seed/bday-d/400/500" alt="Memory" loading="lazy">
          <div class="gcap">🌙 Sweet Memories</div>
        </div>
        <div class="gcard">
          <img src="https://picsum.photos/seed/bday-e/400/500" alt="Memory" loading="lazy">
          <div class="gcap">💫 Forever Cherished</div>
        </div>
      </div>
      <p style="text-align:center;margin-top:28px;color:rgba(255,255,255,.3);font-size:.78rem;font-style:italic">
        💡 Replace images by adding your own photos to assets/images/
      </p>
    </section>

    <!-- ── LOVE QUOTES ── -->
    <section class="sec qsec reveal">
      <span class="slabel">💬 Words for You</span>
      <h2 class="stitle">Love & Wishes</h2>
      <div class="sdiv"></div>
      <div class="qcont" id="qCont"></div>
      <div class="qdots" id="qDots"></div>
    </section>

    <!-- ── COUNTDOWN ── -->
    <section class="sec cdsec reveal">
      <span class="slabel">⏳ Counting Down</span>
      <h2 class="stitle">To Your Special Day</h2>
      <div class="sdiv"></div>
      <div id="cdMsg"></div>
      <div class="cdgrid">
        <div class="cdcard"><span class="cdnum" id="cd-d">--</span><span class="cdlbl">Days</span></div>
        <div class="cdcard"><span class="cdnum" id="cd-h">--</span><span class="cdlbl">Hours</span></div>
        <div class="cdcard"><span class="cdnum" id="cd-m">--</span><span class="cdlbl">Minutes</span></div>
        <div class="cdcard"><span class="cdnum" id="cd-s">--</span><span class="cdlbl">Seconds</span></div>
      </div>
      <p class="cdnote" id="cdNote">Until your next birthday 🎂</p>
    </section>

    <!-- ── WISHES MARQUEE ── -->
    <section class="sec wsec reveal">
      <span class="slabel">🌟 Wishes</span>
      <h2 class="stitle">Birthday Wishes</h2>
      <div class="sdiv"></div>
      <div class="wtrack" id="wTrack"></div>
    </section>

    <!-- ── FOOTER ── -->
    <footer class="foot">
      <div class="foot-h">❤️</div>
      <p class="foot-t">Made with all my love, just for you 💝</p>
      <p style="color:rgba(255,255,255,.14);font-size:.72rem;margin-top:10px">Today is your day. Shine bright always. ✨</p>
    </footer>

  </div><!-- /pcnt -->

  <!-- Music Player -->
  <div id="mplayer">
    <div class="mart" id="mart">🎵</div>
    <div class="minfo">
      <div class="mtitle">Birthday Melody 🎶</div>
      <div class="martist">Just for you 💕</div>
    </div>
    <div class="mctrl">
      <button class="pbtn" id="pbtn" onclick="toggleMusic()">▶</button>
      <input type="range" class="vslider" id="vslider"
             min="0" max="1" step="0.05" value="0.5"
             oninput="setVol(this.value)">
    </div>
  </div>
  <audio id="bgAudio" loop>
    <source src="C:/Users/SHIVAM GUPTA/OneDrive/Desktop/birthday/music.mpeg" type="audio/mpeg">
  </audio>

</div><!-- /bPage -->

<!-- ════════════════════════════════════════════════════
     JAVASCRIPT
════════════════════════════════════════════════════ -->
<script>
/* ── CUSTOM CURSOR ─────────────────────────────────────────────────────
   FIX 1: transform instead of left/top  → works reliably in Streamlit
           iframe because it triggers GPU compositing layer
   FIX 2: start at screen centre         → no 0,0 flash before first move
   FIX 3: { passive:true } on mousemove  → browser won't delay the event
──────────────────────────────────────────────────────────────────────── */
/* ── CUSTOM CURSOR ─────────────────────────────────────────────────────
   WHY transform instead of left/top:
   Streamlit renders components in a sandboxed iframe. Writing left/top
   triggers a layout pass that the browser can defer or batch; writing
   transform goes straight to the GPU compositor and is never deferred.
   Starting mx/my at screen centre prevents a 0,0 corner flash before
   the first mousemove event fires.
──────────────────────────────────────────────────────────────────────── */
const cur  = document.getElementById('cur');
const cur2 = document.getElementById('cur2');

let mx = window.innerWidth  / 2;
let my = window.innerHeight / 2;
let tx = mx, ty = my;

// Pre-position both dots so they are never stuck at (0,0)
cur.style.transform  = 'translate(' + (mx - 5)  + 'px,' + (my - 5)  + 'px)';
cur2.style.transform = 'translate(' + (tx - 14) + 'px,' + (ty - 14) + 'px)';

document.addEventListener('mousemove', function(e) {
  mx = e.clientX;
  my = e.clientY;
  cur.style.transform = 'translate(' + (mx - 5) + 'px,' + (my - 5) + 'px)';
  if (document.getElementById('bPage').style.display !== 'none') spawnSparkle(mx, my);
}, { passive: true });

(function trail() {
  tx += (mx - tx) * 0.15;
  ty += (my - ty) * 0.15;
  cur2.style.transform = 'translate(' + (tx - 14) + 'px,' + (ty - 14) + 'px)';
  requestAnimationFrame(trail);
})();

const SPK=['✨','💫','⭐','🌟','💕','🌸','💖','🩷'];
let lastSpk=0;
function spawnSparkle(x,y){
  const now=Date.now(); if(now-lastSpk<75) return; lastSpk=now;
  const el=document.createElement('div'); el.className='spk';
  el.textContent=SPK[Math.floor(Math.random()*SPK.length)];
  el.style.left = '0'; el.style.top = '0';
  el.style.transform = 'translate(' + (x-9) + 'px,' + (y-9) + 'px)';
  el.style.setProperty('--dx',(Math.random()-.5)*65+'px');
  el.style.setProperty('--dy',(Math.random()-.5)*65+'px');
  document.body.appendChild(el);
  setTimeout(()=>el.remove(),780);
}

/* ── LOCK SCREEN PARTICLES ─────────────────────────── */
const pC=document.getElementById('pCanvas');
const pc=pC.getContext('2d');
let pts=[];
function resP(){ pC.width=window.innerWidth; pC.height=window.innerHeight; }
resP(); window.addEventListener('resize',resP);
for(let i=0;i<130;i++) pts.push({
  x:Math.random()*pC.width, y:Math.random()*pC.height,
  r:Math.random()*2.2+.4,
  dx:(Math.random()-.5)*.55, dy:(Math.random()-.5)*.55,
  op:Math.random()*.8+.15, h:Math.random()*60+280
});
(function animPts(){
  pc.clearRect(0,0,pC.width,pC.height);
  pts.forEach(p=>{
    p.x+=p.dx; p.y+=p.dy;
    if(p.x<0||p.x>pC.width)  p.dx*=-1;
    if(p.y<0||p.y>pC.height) p.dy*=-1;
    pc.beginPath(); pc.arc(p.x,p.y,p.r,0,Math.PI*2);
    pc.fillStyle=`hsla(${p.h},100%,70%,${p.op})`; pc.fill();
    pts.forEach(q=>{
      const d=Math.hypot(p.x-q.x,p.y-q.y);
      if(d<85){ pc.beginPath(); pc.moveTo(p.x,p.y); pc.lineTo(q.x,q.y);
        pc.strokeStyle=`hsla(${p.h},100%,70%,${.07*(1-d/85)})`;
        pc.lineWidth=.5; pc.stroke(); }
    });
  });
  if(document.getElementById('lockScreen').style.display!=='none')
    requestAnimationFrame(animPts);
})();

/* floating hearts + balloons */
const fC=document.getElementById('floats');
const HE=['❤️','💕','💖','💗','💝','🩷'];
const BE=['🎈','🎀','🎊','🎉'];
for(let i=0;i<16;i++){
  const el=document.createElement('div'); el.className='fheart';
  el.textContent=HE[i%HE.length];
  el.style.cssText=`left:${Math.random()*100}%;font-size:${Math.random()*1.5+.7}rem;
    animation-duration:${Math.random()*8+5}s;animation-delay:${Math.random()*12}s;`;
  fC.appendChild(el);
}
for(let i=0;i<8;i++){
  const el=document.createElement('div'); el.className='fball';
  el.textContent=BE[i%BE.length];
  el.style.cssText=`left:${Math.random()*100}%;font-size:${Math.random()*1.5+1.5}rem;
    animation-duration:${Math.random()*10+7}s;animation-delay:${Math.random()*14}s;`;
  fC.appendChild(el);
}

/* ── PASSCODE CHECK ────────────────────────────────── */
const PASS='04/06/2005';
function checkCode(){
  const inp=document.getElementById('pInput');
  const err=document.getElementById('errMsg');
  const btn=document.getElementById('ulBtn');
  const v=inp.value.trim();
  if(v===PASS){
    err.textContent='';
    inp.style.borderColor='#4caf50';
    inp.style.boxShadow='0 0 22px rgba(76,175,80,.55)';
    btn.textContent='🎉 Unlocked! Loading...';
    btn.style.background='linear-gradient(135deg,#4caf50,#2e7d32)';
    setTimeout(()=>showFireworks(),250);
    setTimeout(()=>goBirthday(),3200);
  } else {
    inp.classList.add('err');
    err.textContent='❌ Wrong passcode! Try again... 💔';
    inp.value='';
    setTimeout(()=>{ inp.classList.remove('err'); err.textContent=''; },1600);
  }
}
// Enter key
document.getElementById('pInput').addEventListener('keydown',e=>{ if(e.key==='Enter') checkCode(); });
// Auto-format DD/MM/YYYY
document.getElementById('pInput').addEventListener('input',e=>{
  let d=e.target.value.replace(/[^0-9/]/g,'').replace(/\//g,'');
  if(d.length>4) d=d.slice(0,2)+'/'+d.slice(2,4)+'/'+d.slice(4,8);
  else if(d.length>2) d=d.slice(0,2)+'/'+d.slice(2);
  e.target.value=d;
});

/* ── FIREWORKS ─────────────────────────────────────── */
function showFireworks(){
  const ov=document.getElementById('fwOverlay');
  const fc=document.getElementById('fwCanvas');
  const fx=fc.getContext('2d');
  ov.style.display='block';
  fc.width=window.innerWidth; fc.height=window.innerHeight;

  let fws=[],fps=[];

  class FW{
    constructor(){
      this.sx=Math.random()*fc.width;
      this.sy=fc.height;
      this.tx=100+Math.random()*(fc.width-200);
      this.ty=60+Math.random()*(fc.height*.45);
      this.h=Math.random()*360;
      this.done=false;
      const a=Math.atan2(this.ty-this.sy,this.tx-this.sx);
      const sp=12+Math.random()*4;
      this.vx=Math.cos(a)*sp; this.vy=Math.sin(a)*sp;
      this.trail=[];
    }
    update(){
      this.trail.push({x:this.sx,y:this.sy});
      if(this.trail.length>9) this.trail.shift();
      this.sx+=this.vx; this.sy+=this.vy;
      if(Math.hypot(this.sx-this.tx,this.sy-this.ty)<12){ this.boom(); this.done=true; }
    }
    boom(){
      for(let i=0;i<90;i++){
        const a=(i/90)*Math.PI*2,sp=Math.random()*6+2;
        fps.push({x:this.sx,y:this.sy,vx:Math.cos(a)*sp,vy:Math.sin(a)*sp,
          h:this.h,life:1,dc:Math.random()*.022+.008});
      }
    }
    draw(){
      fx.beginPath();
      this.trail.forEach((p,i)=>{ if(i===0) fx.moveTo(p.x,p.y); else fx.lineTo(p.x,p.y); });
      fx.lineTo(this.sx,this.sy);
      fx.strokeStyle=`hsl(${this.h},100%,72%)`; fx.lineWidth=2.5; fx.stroke();
    }
  }
  const si=setInterval(()=>fws.push(new FW()),280);
  setTimeout(()=>clearInterval(si),2600);

  (function aFW(){
    fx.fillStyle='rgba(5,0,15,.14)';
    fx.fillRect(0,0,fc.width,fc.height);
    fws=fws.filter(f=>{ f.update(); f.draw(); return !f.done; });
    fps=fps.filter(p=>{
      p.vx*=.98; p.vy*=.98; p.vy+=.1;
      p.x+=p.vx; p.y+=p.vy; p.life-=p.dc;
      fx.beginPath(); fx.arc(p.x,p.y,2.5,0,Math.PI*2);
      fx.fillStyle=`hsla(${p.h},100%,70%,${p.life})`; fx.fill();
      return p.life>0;
    });
    requestAnimationFrame(aFW);
  })();
}

/* ── TRANSITION ────────────────────────────────────── */
function goBirthday(){
  const ls=document.getElementById('lockScreen');
  const bp=document.getElementById('bPage');
  const fw=document.getElementById('fwOverlay');
  ls.style.transition='opacity 1.1s ease'; ls.style.opacity='0';
  setTimeout(()=>{
    ls.style.display='none'; fw.style.display='none';
    bp.style.display='block';
    bp.style.opacity='0'; bp.style.transition='opacity 1.1s ease';
    requestAnimationFrame(()=>{ bp.style.opacity='1'; });
    initBirthday();
  },1100);
}

/* ── INIT BIRTHDAY PAGE ────────────────────────────── */
function initBirthday(){
  initBgCanvas();
  initTyping();
  initHeroHearts();
  initQuotes();
  initCountdown();
  initWishes();
  initReveal();
  setTimeout(()=>{ document.getElementById('mplayer').classList.add('show'); initMusic(); },1400);
}

/* ── BG CANVAS (birthday) ──────────────────────────── */
function initBgCanvas(){
  const cv=document.getElementById('bgC');
  const cx=cv.getContext('2d');
  const resize=()=>{ cv.width=window.innerWidth; cv.height=window.innerHeight; };
  resize(); window.addEventListener('resize',resize);
  const stars=Array.from({length:220},()=>({
    x:Math.random()*cv.width, y:Math.random()*cv.height,
    r:Math.random()*1.6+.2, op:Math.random()*.85+.1,
    tw:Math.random()*Math.PI*2, sp:Math.random()*.04+.01,
    dx:(Math.random()-.5)*.18, dy:(Math.random()-.5)*.18,
  }));
  (function drawBg(){
    cx.clearRect(0,0,cv.width,cv.height);
    const g=cx.createRadialGradient(cv.width/2,cv.height/2,0,cv.width/2,cv.height/2,cv.width*.85);
    g.addColorStop(0,'rgba(22,0,45,.96)'); g.addColorStop(1,'rgba(5,0,15,.99)');
    cx.fillStyle=g; cx.fillRect(0,0,cv.width,cv.height);
    stars.forEach(s=>{
      s.tw+=s.sp; s.x+=s.dx; s.y+=s.dy;
      if(s.x<0) s.x=cv.width; if(s.x>cv.width) s.x=0;
      if(s.y<0) s.y=cv.height; if(s.y>cv.height) s.y=0;
      const op=s.op*(.48+.52*Math.sin(s.tw));
      cx.beginPath(); cx.arc(s.x,s.y,s.r,0,Math.PI*2);
      cx.fillStyle=`rgba(255,195,255,${op})`; cx.fill();
    });
    requestAnimationFrame(drawBg);
  })();
}

/* ── TYPING ANIMATION ──────────────────────────────── */
function initTyping(){
  const msgs=[
    "You are the most special person in my life ✨",
    "Every single day with you is a blessing 💕",
    "You deserve all the happiness in the world 🌟",
    "May every dream of yours come true today 🎂",
    "You make everything brighter just by being you 🌸",
    "Today and always — you are my everything 💖",
  ];
  let mi=0,ci=0,del=false;
  const el=document.getElementById('tText');
  (function type(){
    const cur=msgs[mi];
    if(!del){ el.textContent=cur.slice(0,++ci); if(ci===cur.length){del=true;setTimeout(type,2600);return;} }
    else { el.textContent=cur.slice(0,--ci); if(ci===0){del=false;mi=(mi+1)%msgs.length;} }
    setTimeout(type,del?52:88);
  })();
}

/* ── HERO HEARTS ───────────────────────────────────── */
function initHeroHearts(){
  const hc=document.getElementById('hHrts');
  const emo=['❤️','💕','💖','✨','🌸','💫','🩷','⭐'];
  setInterval(()=>{
    const h=document.createElement('div');
    h.style.cssText=`position:absolute;left:${Math.random()*100}%;bottom:0;
      font-size:${Math.random()*1.5+.7}rem;
      animation:floatUp ${Math.random()*3+3}s linear forwards;
      pointer-events:none;`;
    h.textContent=emo[Math.floor(Math.random()*emo.length)];
    hc.appendChild(h); setTimeout(()=>h.remove(),5500);
  },380);
}

/* ── SURPRISE POPUP ────────────────────────────────── */
function openSurprise(){
  document.getElementById('sPopup').classList.add('on');
  startConfetti();
}
function closePopup(){
  document.getElementById('sPopup').classList.remove('on');
  stopConfetti();
}

/* ── CONFETTI ──────────────────────────────────────── */
const cCv=document.getElementById('cCanvas');
const ccx=cCv.getContext('2d');
let cPts=[],cRun=false,cAnim;

function startConfetti(){
  cCv.style.display='block';
  cCv.width=window.innerWidth; cCv.height=window.innerHeight;
  cRun=true;
  function addBurst(n){
    for(let i=0;i<n;i++) cPts.push({
      x:Math.random()*cCv.width, y:-18,
      vx:(Math.random()-.5)*9, vy:Math.random()*5+1.5,
      col:['#ff6b9d','#c44dff','#4d79ff','#ffd700','#00d4ff','#ff3388','#50fa7b'][Math.floor(Math.random()*7)],
      sz:Math.random()*11+4, rot:Math.random()*360,
      rs:(Math.random()-.5)*9, sh:Math.random()>.5?'r':'c', lf:1
    });
  }
  addBurst(220);
  const si=setInterval(()=>{ if(!cRun){clearInterval(si);return;} addBurst(22); },220);
  (function aConf(){
    if(!cRun){ccx.clearRect(0,0,cCv.width,cCv.height);return;}
    ccx.clearRect(0,0,cCv.width,cCv.height);
    cPts=cPts.filter(p=>{
      p.x+=p.vx; p.y+=p.vy; p.vy+=.09; p.vx*=.992; p.rot+=p.rs;
      if(p.y>cCv.height+20) return false;
      ccx.save(); ccx.translate(p.x,p.y); ccx.rotate(p.rot*Math.PI/180);
      ccx.fillStyle=p.col; ccx.globalAlpha=p.lf;
      if(p.sh==='r') ccx.fillRect(-p.sz/2,-p.sz/4,p.sz,p.sz/2);
      else { ccx.beginPath(); ccx.arc(0,0,p.sz/2,0,Math.PI*2); ccx.fill(); }
      ccx.restore(); return true;
    });
    cAnim=requestAnimationFrame(aConf);
  })();
}
function stopConfetti(){
  cRun=false; cPts=[];
  if(cAnim) cancelAnimationFrame(cAnim);
  setTimeout(()=>cCv.style.display='none',80);
}

/* ── QUOTES SLIDER ─────────────────────────────────── */
const QUOTES=[
  {t:"In a world full of temporary things, you are a perpetual feeling.",a:"Sanober Khan"},
  {t:"You deserve to be celebrated every single day — but today especially. The world became better when you entered it.",a:"A Heart Full of Love"},
  {t:"Birthday candles can't hold a flame to the light you bring into every room.",a:"Anonymous"},
  {t:"May your birthday be the beginning of a year filled with love, laughter, and all the magic your heart deserves.",a:"With All My Love"},
  {t:"You are not just a year older — you are a year more wonderful, a year more beautifully you.",a:"Forever Yours"},
  {t:"The most beautiful thing in the world is watching you smile. Happy Birthday.",a:"From My Heart"},
];
let qIdx=0;
function initQuotes(){
  const qc=document.getElementById('qCont');
  const qd=document.getElementById('qDots');
  QUOTES.forEach((q,i)=>{
    const s=document.createElement('div');
    s.className='qslide'+(i===0?' qon':'');
    s.innerHTML=`<div class="qmark">"</div><p class="qtxt">${q.t}</p><span class="qauth">— ${q.a}</span>`;
    qc.appendChild(s);
    const d=document.createElement('div');
    d.className='qdot'+(i===0?' don':'');
    d.onclick=()=>goQ(i); qd.appendChild(d);
  });
  setInterval(()=>goQ((qIdx+1)%QUOTES.length),5200);
}
function goQ(i){
  const ss=document.querySelectorAll('.qslide');
  const dd=document.querySelectorAll('.qdot');
  ss[qIdx].classList.remove('qon'); ss[qIdx].classList.add('qout');
  setTimeout(()=>{ const el=ss[qIdx]; if(el) el.classList.remove('qout'); },800);
  qIdx=i; ss[qIdx].classList.add('qon');
  dd.forEach((d,j)=>d.classList.toggle('don',j===qIdx));
}

/* ── COUNTDOWN ─────────────────────────────────────── */
function initCountdown(){
  function tick(){
    const now=new Date();
    let bd=new Date(now.getFullYear(),5,4,0,0,0); // June 4
    if(now>bd) bd=new Date(now.getFullYear()+1,5,4,0,0,0);
    const diff=bd-now;
    if(diff<=0){
      document.getElementById('cdMsg').innerHTML=
        `<p style="font-size:1.5rem;font-weight:700;color:var(--pink);margin-bottom:18px;animation:hPulse 2s infinite">🎉 TODAY IS YOUR DAY! 🎉</p>`;
      ['d','h','m','s'].forEach(k=>document.getElementById('cd-'+k).textContent='00');
      document.getElementById('cdNote').textContent="It's your birthday today! 🎂✨";
      return;
    }
    const d=Math.floor(diff/864e5);
    const h=Math.floor(diff%864e5/36e5);
    const m=Math.floor(diff%36e5/6e4);
    const s=Math.floor(diff%6e4/1e3);
    document.getElementById('cd-d').textContent=String(d).padStart(2,'0');
    document.getElementById('cd-h').textContent=String(h).padStart(2,'0');
    document.getElementById('cd-m').textContent=String(m).padStart(2,'0');
    document.getElementById('cd-s').textContent=String(s).padStart(2,'0');
  }
  tick(); setInterval(tick,1e3);
}

/* ── WISHES MARQUEE ────────────────────────────────── */
function initWishes(){
  const wishes=[
    "🎂 Happy Birthday beautiful!","💕 Wishing you endless love",
    "✨ May your dreams come true","🌸 You deserve the world",
    "🎉 Cheers to 21!","💝 You are so loved",
    "🌟 Shine bright always","🎊 So happy you exist",
    "💫 Here's to you!","🎈 Make it magical",
    "🩷 You mean everything","🌺 Beautiful soul",
    "🎂 Happy Birthday beautiful!","💕 Wishing you endless love",
    "✨ May your dreams come true","🌸 You deserve the world",
    "🎉 Cheers to 21!","💝 You are so loved",
  ];
  const t=document.getElementById('wTrack');
  wishes.forEach(w=>{ const b=document.createElement('div'); b.className='wbub'; b.textContent=w; t.appendChild(b); });
}

/* ── SCROLL REVEAL ─────────────────────────────────── */
function initReveal(){
  const obs=new IntersectionObserver(entries=>{
    entries.forEach(e=>{ if(e.isIntersecting) e.target.classList.add('vis'); });
  },{threshold:.12});
  document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));
}

/* ── MUSIC PLAYER ──────────────────────────────────── */
function initMusic(){
  const a=document.getElementById('bgAudio');
  a.volume=.5;
  a.play().then(()=>updatePBtn(true)).catch(()=>updatePBtn(false));
}
function toggleMusic(){
  const a=document.getElementById('bgAudio');
  if(a.paused){ a.play(); updatePBtn(true); }
  else { a.pause(); updatePBtn(false); }
}
function updatePBtn(pl){
  document.getElementById('pbtn').textContent=pl?'⏸':'▶';
  const art=document.getElementById('mart');
  pl ? art.classList.add('pl') : art.classList.remove('pl');
}
function setVol(v){ document.getElementById('bgAudio').volume=v; }
</script>

"""

# ── Render the full HTML as a fullscreen iframe ────────────────────────────────
st.iframe(HTML_PAGE, height=800)
