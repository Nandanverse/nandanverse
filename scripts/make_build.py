import os

STATIC = os.environ.get("STATIC", "0") == "1"

ITEMS = [
    ("Python",     "#3fb950"),
    ("FastAPI",    "#3fb950"),
    ("React",      "#79c0ff"),
    ("Docker",     "#56d4dd"),
    ("Go",         "#56d4dd"),
    ("Flutter",    "#79c0ff"),
    ("PostgreSQL", "#3fb950"),
    ("Redis",      "#ff7b72"),
    ("Kali Linux", "#ffa657"),
    ("Wazuh",      "#d2a8ff"),
    ("Grafana",    "#ffa657"),
    ("Nmap",       "#3fb950"),
    ("Burp Suite", "#ff7b72"),
    ("Metasploit", "#ff7b72"),
    ("Wireshark",  "#79c0ff"),
    ("scikit-learn","#3fb950"),
    ("Hyperledger","#d2a8ff"),
    ("ESP32",      "#ffa657"),
    ("Zeek",       "#56d4dd"),
    ("GitHub Actions", "#c9d1d9"),
]

COLS = 5
ROWS = (len(ITEMS) + COLS - 1) // COLS
CELL_W = 140
CELL_H = 40
PAD_X = 30
PAD_Y = 55
GAP = 10
W = PAD_X * 2 + COLS * CELL_W + (COLS - 1) * GAP
H = PAD_Y + ROWS * CELL_H + (ROWS - 1) * GAP + 20
BG = "#0d1117"
BORDER = "#30363d"
GREEN = "#3fb950"
FONT = "'SF Mono','Fira Code',Consolas,Menlo,monospace"

def main():
    out = "data/build.svg"
    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}" font-size="12">')
    lines.append(f'  <style>')
    lines.append(f'    @keyframes fadeSlide {{ from {{ opacity:0; transform:translateY(10px); }} to {{ opacity:1; transform:translateY(0); }} }}')
    lines.append(f'    .item {{ animation: fadeSlide 0.4s cubic-bezier(0.4,0,0.2,1) forwards; opacity:0; }}')
    lines.append(f'  </style>')
    lines.append(f'  <rect width="{W}" height="{H}" rx="12" fill="{BG}" stroke="{BORDER}"/>')

    # Title
    lines.append(f'  <text x="{W//2}" y="32" font-size="14" font-weight="bold" fill="{GREEN}" text-anchor="middle">&gt; let\'s build together_</text>')

    # Grid
    for i, (name, color) in enumerate(ITEMS):
        row = i // COLS
        col = i % COLS
        x = PAD_X + col * (CELL_W + GAP)
        y = PAD_Y + row * (CELL_H + GAP)
        delay = 0.2 + i * 0.05

        if not STATIC:
            lines.append(f'  <g class="item" style="animation-delay:{delay:.2f}s">')
        lines.append(f'    <rect x="{x}" y="{y}" width="{CELL_W}" height="{CELL_H}" rx="6" fill="{color}" opacity="0.1" stroke="{color}" stroke-width="0.6"/>')
        lines.append(f'    <text x="{x + CELL_W//2}" y="{y + CELL_H//2 + 4}" fill="{color}" text-anchor="middle">{name}</text>')
        if not STATIC:
            lines.append(f'  </g>')

    lines.append('</svg>')

    os.makedirs("data", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Saved: {out}")

if __name__ == "__main__":
    main()
