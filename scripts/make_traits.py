import os

STATIC = os.environ.get("STATIC", "0") == "1"

TRAITS = [
    ("Offensive Security", "#ff7b72"),
    ("Network Security", "#79c0ff"),
    ("Cloud Security", "#56d4dd"),
    ("ML / AI", "#d2a8ff"),
    ("Blockchain", "#ffa657"),
    ("Security Automation", "#3fb950"),
    ("Web App Security", "#e3b341"),
    ("SIEM / SOC", "#f778ba"),
]

W = 860
H = 120
BG = "#0d1117"
BORDER = "#30363d"
FONT = "'SF Mono','Fira Code',Consolas,Menlo,monospace"

def main():
    out = "data/traits.svg"
    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}" font-size="12">')
    lines.append(f'  <style>')
    lines.append(f'    @keyframes popIn {{ from {{ opacity:0; transform:scale(0.8); }} to {{ opacity:1; transform:scale(1); }} }}')
    lines.append(f'    .pill {{ animation: popIn 0.4s cubic-bezier(0.4,0,0.2,1) forwards; opacity:0; }}')
    lines.append(f'  </style>')
    lines.append(f'  <rect width="{W}" height="{H}" rx="12" fill="{BG}" stroke="{BORDER}"/>')

    # Two rows of 4
    col_w = W // 4
    for i, (trait, color) in enumerate(TRAITS):
        row = i // 4
        col = i % 4
        x = 30 + col * col_w
        y = 30 + row * 45
        delay = 0.1 + i * 0.08

        # Estimate pill width based on text length
        pill_w = len(trait) * 7.5 + 20

        if not STATIC:
            lines.append(f'  <g class="pill" style="animation-delay:{delay:.2f}s">')
        lines.append(f'    <rect x="{x}" y="{y}" width="{pill_w}" height="28" rx="14" fill="{color}" opacity="0.12" stroke="{color}" stroke-width="0.8"/>')
        lines.append(f'    <text x="{x + pill_w//2}" y="{y + 18}" fill="{color}" text-anchor="middle">{trait}</text>')
        if not STATIC:
            lines.append(f'  </g>')

    lines.append('</svg>')

    os.makedirs("data", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Saved: {out}")

if __name__ == "__main__":
    main()
