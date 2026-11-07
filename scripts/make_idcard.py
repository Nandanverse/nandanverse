import os

STATIC = os.environ.get("STATIC", "0") == "1"

NAME = "Nandan Amin"
ROLE = "Cybersecurity Developer"
ORG = "Nandanverse"
LOCATION = "India"
ID_NUM = "ND-2026-SEC-001"
CLEARANCE = "Level 3"

W = 480
H = 260
BG = "#0d1117"
BORDER = "#30363d"
ACCENT = "#3fb950"
TEXT_MAIN = "#c9d1d9"
TEXT_DIM = "#8b949e"
FONT = "'SF Mono','Fira Code',Consolas,Menlo,monospace"
FONT_SIZE = 13

def main():
    out = "data/idcard.svg"
    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}" font-size="{FONT_SIZE}">')
    lines.append(f'  <defs>')
    lines.append(f'    <linearGradient id="shimmer" x1="0%" y1="0%" x2="100%" y2="0%">')
    lines.append(f'      <stop offset="0%" stop-color="white" stop-opacity="0"/>')
    lines.append(f'      <stop offset="50%" stop-color="white" stop-opacity="0.06"/>')
    lines.append(f'      <stop offset="100%" stop-color="white" stop-opacity="0"/>')
    lines.append(f'    </linearGradient>')
    lines.append(f'    <clipPath id="cardClip"><rect width="{W}" height="{H}" rx="12"/></clipPath>')
    lines.append(f'  </defs>')

    lines.append(f'  <rect width="{W}" height="{H}" rx="12" fill="{BG}" stroke="{BORDER}" stroke-width="1.5"/>')
    lines.append(f'  <rect x="0" y="0" width="{W}" height="3" rx="1.5" fill="{ACCENT}"/>')

    # Photo placeholder
    px, py, pw, ph = 24, 28, 80, 100
    lines.append(f'  <rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="6" fill="{TEXT_DIM}" opacity="0.2"/>')
    lines.append(f'  <text x="{px+pw//2}" y="{py+ph//2+5}" font-size="10" fill="{TEXT_DIM}" text-anchor="middle">PHOTO</text>')

    # Name and role
    tx = 120
    lines.append(f'  <text x="{tx}" y="50" font-size="16" font-weight="bold" fill="{TEXT_MAIN}">{NAME}</text>')
    lines.append(f'  <text x="{tx}" y="70" fill="{ACCENT}">{ROLE}</text>')
    lines.append(f'  <text x="{tx}" y="90" fill="{TEXT_DIM}">{ORG}</text>')

    # Details
    dy = 150
    details = [
        ("ID:", ID_NUM),
        ("Location:", LOCATION),
        ("Clearance:", CLEARANCE),
    ]
    for i, (key, val) in enumerate(details):
        y = dy + i * 24
        lines.append(f'  <text x="24" y="{y}" fill="{TEXT_DIM}">{key}</text>')
        lines.append(f'  <text x="120" y="{y}" fill="{TEXT_MAIN}">{val}</text>')

    # Bottom
    lines.append(f'  <line x1="24" y1="228" x2="{W-24}" y2="228" stroke="{BORDER}" stroke-width="1"/>')
    lines.append(f'  <text x="24" y="248" font-size="10" fill="{TEXT_DIM}">DEVELOPER IDENTITY CARD</text>')
    lines.append(f'  <text x="{W-24}" y="248" font-size="10" fill="{TEXT_DIM}" text-anchor="end">2026</text>')

    # Shimmer
    if not STATIC:
        lines.append(f'  <g clip-path="url(#cardClip)">')
        lines.append(f'    <rect x="-200" y="0" width="200" height="{H}" fill="url(#shimmer)">')
        lines.append(f'      <animate attributeName="x" from="-200" to="{W}" dur="3s" begin="0.5s" fill="freeze"/>')
        lines.append(f'    </rect>')
        lines.append(f'  </g>')

    lines.append('</svg>')

    os.makedirs("data", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Saved: {out}")

if __name__ == "__main__":
    main()
