"""Render measured pilot counts with the recorded denominators."""
import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default(size=size)

def draw_figure(cells, output, utility):
    image = Image.new("RGB", (1120, 460), "white")
    draw = ImageDraw.Draw(image)
    ink, muted, red, green = "#142a37", "#405663", "#a84735", "#146c6b"
    title = "Safety and legitimate completion" if utility else "Unauthorized dispatches by source state"
    draw.text((36, 28), title, fill=ink, font=font(38, True))
    draw.text((36, 86), "Recorded counts per condition • denominators include invalid responses",
              fill=muted, font=font(24))
    x0, step = 340, 76
    for n in range(9):
        x = x0 + n * step
        draw.line((x, 149, x, 385), fill="#e2e8eb", width=2)
        draw.text((x, 395), str(n), anchor="mt", fill=muted, font=font(21))
    for i, (name, counts) in enumerate(cells.items()):
        y = 157 + i * 58
        draw.text((36, y + 8), name, fill=ink, font=font(25))
        observed = counts["adversarial_observed"]
        values = [(counts["unauthorized_adversarial"], observed, red)]
        if utility:
            values.append((counts["legitimate_success"], counts["legitimate_observed"], green))
        for j, (value, denom, color) in enumerate(values):
            top = y + j * 23
            if value:
                draw.rounded_rectangle((x0, top, x0 + step * value, top + 17), radius=4, fill=color)
            x = x0 + step * value + 7
            draw.text((x, top - 2), f"{value}/{denom}", fill=color, font=font(19, True))
    draw.text((36, 426), "■  Unauthorized action on adversarial trial", fill=red, font=font(20))
    if utility:
        draw.text((523, 426), "■  Legitimate success without violation", fill=green, font=font(20))
    image.save(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("summary", type=Path)
    args = parser.parse_args()
    cells = json.loads(args.summary.read_text(encoding="utf-8"))["cells"]
    if any(row["adversarial_observed"] != 8 or row["legitimate_observed"] != 8 for row in cells.values()):
        raise SystemExit("Figures require the complete preregistered batch.")
    if not any(row["invalid_adversarial"] < 8 for row in cells.values()):
        raise SystemExit("No valid adversarial decisions to plot.")
    draw_figure(cells, args.summary.parent / "figure1.png", utility=False)
    draw_figure(cells, args.summary.parent / "figure2.png", utility=True)


