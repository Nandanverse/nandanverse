import numpy as np
import cv2
import os

RAMP = "@%#*+=-:. "
COLS = 240
ROWS = 125
CHAR_W = 6
CHAR_H = 12
FILL = "#b0b0b0"
BG = "#111111"

def main():
    img_path = "data/source-prepped.png"
    out_path = "data/avi-ascii.svg"

    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: cannot open {img_path}")
        return

    # Lighter blur (sigmaX=1.5) — preserves hair strands
    img = cv2.GaussianBlur(img, (0, 0), sigmaX=1.5)

    # Unsharp mask — brings back fine edges lost to blur
    blurred = cv2.GaussianBlur(img, (0, 0), sigmaX=3)
    img = cv2.addWeighted(img, 1.5, blurred, -0.5, 0)

    img = cv2.resize(img, (COLS, ROWS), interpolation=cv2.INTER_AREA)

    grid = []
    for r in range(ROWS):
        row = []
        for c in range(COLS):
            idx = int((1.0 - img[r, c] / 255.0) * (len(RAMP) - 1))
            row.append(RAMP[idx])
        grid.append(row)

    svg_w = COLS * CHAR_W + 20
    svg_h = ROWS * CHAR_H + 20
    pad_x = 10
    pad_y = 10
    row_stagger = 0.04
    wipe_dur = 1.8

    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">')
    lines.append(f'  <rect width="100%" height="100%" fill="{BG}"/>')

    for r in range(ROWS):
        y = pad_y + r * CHAR_H
        x_start = pad_x
        delay = r * row_stagger
        clip_id = f"clip{r}"

        lines.append(f'  <clipPath id="{clip_id}">')
        lines.append(f'    <rect x="{x_start}" y="{y-1}" width="0" height="{CHAR_H+2}">')
        lines.append(f'      <animate attributeName="width" from="0" to="{COLS*CHAR_W}" dur="{wipe_dur}s" begin="{delay:.2f}s" fill="freeze"/>')
        lines.append(f'    </rect>')
        lines.append(f'  </clipPath>')

        text = "".join(grid[r])
        text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        lines.append(f'  <text x="{x_start}" y="{y+CHAR_H-2}" font-family="Consolas,monospace" font-size="{CHAR_H-2}" fill="{FILL}" clip-path="url(#{clip_id})">{text}</text>')

        lines.append(f'  <rect x="{x_start}" y="{y-1}" width="{CHAR_W}" height="{CHAR_H+2}" fill="{FILL}" opacity="0.7">')
        lines.append(f'    <animate attributeName="x" from="{x_start}" to="{x_start+COLS*CHAR_W}" dur="{wipe_dur}s" begin="{delay:.2f}s" fill="freeze"/>')
        lines.append(f'    <animate attributeName="opacity" from="0.7" to="0" dur="0.2s" begin="{delay+wipe_dur:.2f}s" fill="freeze"/>')
        lines.append(f'  </rect>')

    lines.append('</svg>')

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Saved: {out_path}")

if __name__ == "__main__":
    main()
