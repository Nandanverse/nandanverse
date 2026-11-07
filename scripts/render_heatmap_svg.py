import json
import os
from datetime import datetime, timedelta

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]
CELL = 13
GAP = 2
PAD_X = 60
PAD_Y = 40
WEEKS = 53
DAYS = 7
R = 3

IN_PATH = "data/contributions.json"
OUT_PATH = "data/contrib-heatmap.svg"

def level(count):
    if count == 0:
        return 0
    elif count <= 2:
        return 1
    elif count <= 5:
        return 2
    elif count <= 10:
        return 3
    elif count <= 19:
        return 4
    else:
        return 5

def main():
    with open(IN_PATH) as f:
        data = json.load(f)

    days = data.get("days", [])
    stats = data.get("stats", {})
    total = stats.get("total", sum(d["count"] for d in days))

    date_map = {d["date"]: d["count"] for d in days}

    today = datetime.now()
    start = today - timedelta(weeks=WEEKS - 1)
    start -= timedelta(days=start.weekday())

    grid_w = WEEKS * (CELL + GAP)
    grid_h = DAYS * (CELL + GAP)
    svg_w = PAD_X * 2 + grid_w
    svg_h = PAD_Y + grid_h + 80

    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_w}" height="{svg_h}" viewBox="0 0 {svg_w} {svg_h}">')
    lines.append(f'  <defs>')
    lines.append(f'    <linearGradient id="sweep" x1="0%" y1="0%" x2="100%" y2="100%">')
    lines.append(f'      <stop offset="0%" stop-color="white"/>')
    lines.append(f'      <stop offset="60%" stop-color="white"/>')
    lines.append(f'      <stop offset="100%" stop-color="black"/>')
    lines.append(f'      <animate attributeName="x1" from="-100%" to="100%" dur="4s" fill="freeze"/>')
    lines.append(f'      <animate attributeName="y1" from="-100%" to="100%" dur="4s" fill="freeze"/>')
    lines.append(f'      <animate attributeName="x2" from="0%" to="200%" dur="4s" fill="freeze"/>')
    lines.append(f'      <animate attributeName="y2" from="0%" to="200%" dur="4s" fill="freeze"/>')
    lines.append(f'    </linearGradient>')
    lines.append(f'    <mask id="diagMask">')
    lines.append(f'      <rect width="100%" height="100%" fill="url(#sweep)"/>')
    lines.append(f'    </mask>')
    lines.append(f'  </defs>')
    lines.append(f'  <rect width="100%" height="100%" rx="12" fill="#0d1117" stroke="#30363d"/>')

    # Day labels
    day_labels = ["", "Mon", "", "Wed", "", "Fri", ""]
    for i, label in enumerate(day_labels):
        if label:
            y = PAD_Y + i * (CELL + GAP) + CELL - 3
            lines.append(f'  <text x="10" y="{y}" font-family="Consolas,monospace" font-size="10" fill="#8b949e">{label}</text>')

    # Month labels
    month_labels = []
    for w in range(WEEKS):
        d = start + timedelta(weeks=w)
        prev_d = start + timedelta(weeks=max(0, w-1))
        if d.month != prev_d.month:
            month_labels.append((w, d.strftime("%b")))

    for w, label in month_labels:
        x = PAD_X + w * (CELL + GAP)
        lines.append(f'  <text x="{x}" y="{PAD_Y - 8}" font-family="Consolas,monospace" font-size="10" fill="#8b949e">{label}</text>')

    # Grid with diagonal soft fade mask
    lines.append(f'  <g mask="url(#diagMask)">')
    for day_idx in range(DAYS):
        for week in range(WEEKS):
            d = start + timedelta(weeks=week, days=day_idx)
            if d > today:
                continue
            date_str = d.strftime("%Y-%m-%d")
            count = date_map.get(date_str, 0)
            lvl = level(count)
            x = PAD_X + week * (CELL + GAP)
            y = PAD_Y + day_idx * (CELL + GAP)
            lines.append(f'    <rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="{R}" fill="{PALETTE[lvl]}"/>')
    lines.append(f'  </g>')

    # Legend
    legend_y = PAD_Y + grid_h + 20
    legend_x = PAD_X
    lines.append(f'  <text x="{legend_x}" y="{legend_y + 10}" font-family="Consolas,monospace" font-size="11" fill="#8b949e">Less</text>')
    for i in range(6):
        lines.append(f'  <rect x="{legend_x + 35 + i*16}" y="{legend_y}" width="{CELL}" height="{CELL}" rx="{R}" fill="{PALETTE[i]}"/>')
    lines.append(f'  <text x="{legend_x + 35 + 6*16 + 5}" y="{legend_y + 10}" font-family="Consolas,monospace" font-size="11" fill="#8b949e">More</text>')

    # Stats footer
    stats_y = legend_y + 35
    lines.append(f'  <text x="{PAD_X}" y="{stats_y}" font-family="Consolas,monospace" font-size="13" fill="#c9d1d9">{total:,} contributions in the last year</text>')

    lines.append('</svg>')

    os.makedirs("data", exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Saved: {OUT_PATH}")

if __name__ == "__main__":
    main()
