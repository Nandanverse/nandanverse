import os
import json

STATIC = os.environ.get("STATIC", "0") == "1"

# Read real stats from contributions.json
with open("data/contributions.json") as f:
    data = json.load(f)

stats = data.get("stats", {})
total = stats.get("total", 0)
current_streak = stats.get("current_streak", 0)
longest_streak = stats.get("longest_streak", 0)
monthly = stats.get("monthly", {})

# Monthly bar chart data (last 12 months)
months_sorted = sorted(monthly.keys())[-12:]
max_monthly = max((monthly.get(m, 0) for m in months_sorted), default=1)
bars = [(m, monthly.get(m, 0)) for m in months_sorted]

W = 860
H = 200
BG = "#0d1117"
BORDER = "#30363d"
GREEN = "#3fb950"
GRAY = "#8b949e"
WHITE = "#c9d1d9"
FONT = "'SF Mono','Fira Code',Consolas,Menlo,monospace"

def main():
    out = "data/stats.svg"
    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}" font-size="14">')
    lines.append(f'  <style>')
    lines.append(f'    @keyframes barGrow {{ from {{ transform: scaleY(0); }} to {{ transform: scaleY(1); }} }}')
    lines.append(f'    .bar {{ transform-origin: bottom; animation: barGrow 1s cubic-bezier(0.4,0,0.2,1) forwards; }}')
    lines.append(f'  </style>')
    lines.append(f'  <rect width="{W}" height="{H}" rx="12" fill="{BG}" stroke="{BORDER}"/>')

    # Top stats row
    stats_data = [
        (f"{total:,}", "Total Contributions"),
        (f"{current_streak}", "Day Streak"),
        (f"{longest_streak}", "Longest Streak"),
        (f"{len([d for d in data.get('days',[]) if d['count']>0])}", "Active Days"),
    ]
    col_w = W // 4
    for i, (val, label) in enumerate(stats_data):
        x = 40 + i * col_w
        lines.append(f'  <text x="{x}" y="50" font-size="28" font-weight="bold" fill="{GREEN}">{val}</text>')
        lines.append(f'  <text x="{x}" y="72" font-size="11" fill="{GRAY}">{label}</text>')

    # Separator
    lines.append(f'  <line x1="30" y1="85" x2="{W-30}" y2="85" stroke="{BORDER}" stroke-width="1"/>')

    # Monthly bar chart
    bar_area_x = 60
    bar_area_y = 100
    bar_area_h = 70
    bar_w = 30
    bar_gap = (W - 120 - len(bars) * bar_w) // max(len(bars) - 1, 1)

    for i, (month, count) in enumerate(bars):
        x = bar_area_x + i * (bar_w + bar_gap)
        h = int((count / max_monthly) * bar_area_h) if max_monthly > 0 else 0
        h = max(h, 2)
        y = bar_area_y + bar_area_h - h
        delay = 0.1 + i * 0.05
        lines.append(f'  <rect x="{x}" y="{y}" width="{bar_w}" height="{h}" rx="3" fill="{GREEN}" opacity="0.8" class="bar" style="animation-delay:{delay:.2f}s"/>')
        # Month label
        month_short = month[5:]  # "MM"
        lines.append(f'  <text x="{x + bar_w//2}" y="{bar_area_y + bar_area_h + 14}" font-size="9" fill="{GRAY}" text-anchor="middle">{month_short}</text>')

    lines.append('</svg>')

    os.makedirs("data", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Saved: {out}")

if __name__ == "__main__":
    main()
