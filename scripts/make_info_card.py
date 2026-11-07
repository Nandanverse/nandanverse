import os

STATIC = os.environ.get("STATIC", "0") == "1"

USER = "nandanverse"
NAME = "Nandan Amin"
ROLE = "Cybersecurity Analyst \u2022 Developer"
OS = "B.Tech CSc Cybersecurity"
KERNEL = "Cybersecurity \u2022 Network &amp; Cloud Security"
SHELL = "India"
STATUS = "Student"

PLAN_DONE = "Network Anomaly Detection System, Risk-Aware Autonomous Vulnerability Exploration Network"
PLAN_ACTIVE = "Share what I learn \u2193 Tech Content"

W = 900
H = 483
BG = "#0d1117"
BORDER = "#30363d"
TITLE_BG = "#161b22"
GREEN = "#3fb950"
GRAY = "#8b949e"
WHITE = "#c9d1d9"
FONT = "'SF Mono','Fira Code',Consolas,Menlo,monospace"

# Frame 1 (odd blink)
FRAME1 = "M115 115h20v20h-20zM137 115h20v20h-20zM159 115h20v20h-20zM181 115h20v20h-20zM203 115h20v20h-20zM93 137h20v20h-20zM115 137h20v20h-20zM137 137h20v20h-20zM159 137h20v20h-20zM181 137h20v20h-20zM203 137h20v20h-20zM225 137h20v20h-20zM71 159h20v20h-20zM93 159h20v20h-20zM115 159h20v20h-20zM137 159h20v20h-20zM159 159h20v20h-20zM181 159h20v20h-20zM203 159h20v20h-20zM225 159h20v20h-20zM247 159h20v20h-20zM71 181h20v20h-20zM137 181h20v20h-20zM159 181h20v20h-20zM181 181h20v20h-20zM247 181h20v20h-20zM71 203h20v20h-20zM137 203h20v20h-20zM159 203h20v20h-20zM181 203h20v20h-20zM247 203h20v20h-20zM71 225h20v20h-20zM93 225h20v20h-20zM115 225h20v20h-20zM137 225h20v20h-20zM159 225h20v20h-20zM181 225h20v20h-20zM203 225h20v20h-20zM225 225h20v20h-20zM247 225h20v20h-20zM71 247h20v20h-20zM93 247h20v20h-20zM115 247h20v20h-20zM137 247h20v20h-20zM159 247h20v20h-20zM181 247h20v20h-20zM203 247h20v20h-20zM225 247h20v20h-20zM247 247h20v20h-20zM71 269h20v20h-20zM93 269h20v20h-20zM115 269h20v20h-20zM137 269h20v20h-20zM159 269h20v20h-20zM181 269h20v20h-20zM203 269h20v20h-20zM225 269h20v20h-20zM247 269h20v20h-20zM71 291h20v20h-20zM93 291h20v20h-20zM137 291h20v20h-20zM159 291h20v20h-20zM181 291h20v20h-20zM225 291h20v20h-20zM247 291h20v20h-20zM71 313h20v20h-20zM159 313h20v20h-20zM247 313h20v20h-20z"

# Frame 2 (even blink)
FRAME2 = "M115 115h20v20h-20zM137 115h20v20h-20zM159 115h20v20h-20zM181 115h20v20h-20zM203 115h20v20h-20zM93 137h20v20h-20zM115 137h20v20h-20zM137 137h20v20h-20zM159 137h20v20h-20zM181 137h20v20h-20zM203 137h20v20h-20zM225 137h20v20h-20zM71 159h20v20h-20zM93 159h20v20h-20zM115 159h20v20h-20zM137 159h20v20h-20zM159 159h20v20h-20zM181 159h20v20h-20zM203 159h20v20h-20zM225 159h20v20h-20zM247 159h20v20h-20zM71 181h20v20h-20zM137 181h20v20h-20zM159 181h20v20h-20zM181 181h20v20h-20zM247 181h20v20h-20zM71 203h20v20h-20zM137 203h20v20h-20zM159 203h20v20h-20zM181 203h20v20h-20zM247 203h20v20h-20zM71 225h20v20h-20zM93 225h20v20h-20zM115 225h20v20h-20zM137 225h20v20h-20zM159 225h20v20h-20zM181 225h20v20h-20zM203 225h20v20h-20zM225 225h20v20h-20zM247 225h20v20h-20zM71 247h20v20h-20zM93 247h20v20h-20zM115 247h20v20h-20zM137 247h20v20h-20zM159 247h20v20h-20zM181 247h20v20h-20zM203 247h20v20h-20zM225 247h20v20h-20zM247 247h20v20h-20zM71 269h20v20h-20zM93 269h20v20h-20zM115 269h20v20h-20zM137 269h20v20h-20zM159 269h20v20h-20zM181 269h20v20h-20zM203 269h20v20h-20zM225 269h20v20h-20zM247 269h20v20h-20zM71 291h20v20h-20zM115 291h20v20h-20zM137 291h20v20h-20zM159 291h20v20h-20zM181 291h20v20h-20zM203 291h20v20h-20zM247 291h20v20h-20zM115 313h20v20h-20zM203 313h20v20h-20z"

def main():
    out = "data/info-card.svg"

    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}" font-size="15">')
    lines.append(f'  <rect width="{W}" height="{H}" rx="12" fill="{BG}" stroke="{BORDER}"/>')
    lines.append(f'  <path d="M0 12a12 12 0 0 1 12-12h{W-24}a12 12 0 0 1 12 12v28H0z" fill="{TITLE_BG}"/>')
    lines.append(f'  <circle cx="26" cy="20" r="7" fill="#ff5f56"/>')
    lines.append(f'  <circle cx="50" cy="20" r="7" fill="#ffbd2e"/>')
    lines.append(f'  <circle cx="74" cy="20" r="7" fill="#27c93f"/>')
    lines.append(f'  <text x="{W//2}" y="25" text-anchor="middle" fill="{GRAY}" font-size="13">{USER}@github: ~ \u2014 zsh</text>')

    # neofetch command
    lines.append(f'  <text x="30" y="72" fill="{GREEN}" font-weight="bold">{USER}@github<tspan fill="{GRAY}">:~$</tspan><tspan fill="{WHITE}"> neofetch</tspan></text>')

    # Blinking ASCII (two frames alternating)
    if not STATIC:
        lines.append(f'  <g opacity="1"><path fill="{GREEN}" d="{FRAME1}"/><animate attributeName="opacity" calcMode="discrete" values="1;0;0" keyTimes="0;0.5;1" dur="1s" repeatCount="indefinite"/></g>')
        lines.append(f'  <g opacity="0"><path fill="{GREEN}" d="{FRAME2}"/><animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;0.5" dur="1s" repeatCount="indefinite"/></g>')
    else:
        lines.append(f'  <path fill="{GREEN}" d="{FRAME1}"/>')

    # Info
    lines.append(f'  <text x="340" y="110" fill="{GREEN}" font-weight="bold">{USER}@github</text>')
    lines.append(f'  <text x="340" y="128" fill="{GRAY}">{"-" * 18}</text>')
    lines.append(f'  <text x="340" y="156" fill="{GREEN}" font-weight="bold">Name:</text>')
    lines.append(f'  <text x="414" y="156" fill="{WHITE}">{NAME}</text>')
    lines.append(f'  <text x="340" y="182" fill="{GREEN}" font-weight="bold">Role:</text>')
    lines.append(f'  <text x="414" y="182" fill="{WHITE}">{ROLE}</text>')
    lines.append(f'  <text x="340" y="208" fill="{GREEN}" font-weight="bold">OS:</text>')
    lines.append(f'  <text x="414" y="208" fill="{WHITE}">{OS}</text>')
    lines.append(f'  <text x="340" y="234" fill="{GREEN}" font-weight="bold">Kernel:</text>')
    lines.append(f'  <text x="414" y="234" fill="{WHITE}">{KERNEL}</text>')
    lines.append(f'  <text x="340" y="260" fill="{GREEN}" font-weight="bold">Shell:</text>')
    lines.append(f'  <text x="414" y="260" fill="{WHITE}">{SHELL}</text>')
    lines.append(f'  <text x="340" y="286" fill="{GREEN}" font-weight="bold">Status:</text>')
    lines.append(f'  <text x="414" y="286" fill="{WHITE}">{STATUS}</text>')

    # Color palette
    colors = ["#ff7b72","#ffa657","#e3b341","#3fb950","#56d4dd","#79c0ff","#d2a8ff","#c9d1d9"]
    for i, c in enumerate(colors):
        lines.append(f'  <rect x="{340 + i*36}" y="308" width="36" height="22" fill="{c}"/>')

    # Plan
    lines.append(f'  <text x="30" y="375" fill="{GREEN}" font-weight="bold">{USER}@github<tspan fill="{GRAY}">:~$</tspan><tspan fill="{WHITE}"> cat ~/.plan</tspan></text>')
    lines.append(f'  <text x="30" y="399" fill="{WHITE}"><tspan fill="{GRAY}">[x]</tspan> {PLAN_DONE}</text>')
    lines.append(f'  <text x="30" y="421" fill="{WHITE}"><tspan fill="{GRAY}">[~]</tspan> {PLAN_ACTIVE}</text>')

    # Cursor
    lines.append(f'  <text x="30" y="451" fill="{GREEN}" font-weight="bold">{USER}@github<tspan fill="{GRAY}">:~$</tspan></text>')
    lines.append(f'  <rect x="227" y="437" width="9" height="17" fill="{GREEN}"><animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1.1s" repeatCount="indefinite"/></rect>')

    lines.append('</svg>')

    os.makedirs("data", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Saved: {out}")

if __name__ == "__main__":
    main()
