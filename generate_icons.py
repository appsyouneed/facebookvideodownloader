#!/usr/bin/env python3
"""
Generates simple PNG launcher icons for the app.
Run this once to create the mipmap resources.
Requires: pip install Pillow
"""

import os
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PILLOW = True
except ImportError:
    HAS_PILLOW = False
    print("Pillow not found. Install with: pip install Pillow")
    print("Generating SVG placeholder instead...")

SIZES = {
    "mipmap-mdpi":    48,
    "mipmap-hdpi":    72,
    "mipmap-xhdpi":   96,
    "mipmap-xxhdpi":  144,
    "mipmap-xxxhdpi": 192,
}

BASE = Path("app/src/main/res")

def generate_png_icon(size: int, path: Path, round_icon: bool = False):
    """Generate a simple blue icon with download arrow."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    padding = int(size * 0.05)
    radius = size // 2 if round_icon else int(size * 0.2)

    # Background
    bg_color = (24, 119, 242, 255)  # Facebook blue
    draw.rounded_rectangle(
        [padding, padding, size - padding, size - padding],
        radius=radius,
        fill=bg_color
    )

    # Download arrow (simplified)
    cx = size // 2
    stem_top = int(size * 0.2)
    stem_bottom = int(size * 0.58)
    stem_w = max(2, int(size * 0.12))

    # Arrow stem
    draw.rectangle(
        [cx - stem_w // 2, stem_top, cx + stem_w // 2, stem_bottom],
        fill=(255, 255, 255, 255)
    )

    # Arrow head
    head_size = int(size * 0.22)
    head_y = stem_bottom - int(size * 0.02)
    arrow_points = [
        (cx, head_y + head_size),
        (cx - head_size, head_y),
        (cx + head_size, head_y),
    ]
    draw.polygon(arrow_points, fill=(255, 255, 255, 255))

    # Base line
    base_y = int(size * 0.78)
    base_h = max(2, int(size * 0.08))
    draw.rectangle(
        [int(size * 0.2), base_y, int(size * 0.8), base_y + base_h],
        fill=(255, 255, 255, 255)
    )

    img.save(str(path), "PNG")

def generate_svg_placeholder(path: Path, size: int):
    """Generate a simple SVG icon if Pillow is not available."""
    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{size}" height="{size}" rx="{size//5}" fill="#1877F2"/>
  <rect x="{size*0.44:.0f}" y="{size*0.18:.0f}" width="{size*0.12:.0f}" height="{size*0.42:.0f}" fill="white"/>
  <polygon points="{size//2},{size*0.76:.0f} {size*0.28:.0f},{size*0.54:.0f} {size*0.72:.0f},{size*0.54:.0f}" fill="white"/>
  <rect x="{size*0.2:.0f}" y="{size*0.78:.0f}" width="{size*0.6:.0f}" height="{size*0.08:.0f}" fill="white"/>
</svg>"""
    # Save as XML (Android also accepts XML vector drawables for mipmap on API 26+)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(str(path), "w") as f:
        f.write(svg)

if __name__ == "__main__":
    for folder, size in SIZES.items():
        dir_path = BASE / folder
        dir_path.mkdir(parents=True, exist_ok=True)

        for filename in ["ic_launcher.png", "ic_launcher_round.png"]:
            out_path = dir_path / filename
            is_round = "round" in filename

            if HAS_PILLOW:
                generate_png_icon(size, out_path, round_icon=is_round)
                print(f"✅ Generated {folder}/{filename} ({size}x{size})")
            else:
                # Save SVG with .png extension won't work, but create a placeholder note
                note_path = dir_path / "README_ICONS.txt"
                with open(str(note_path), "w") as f:
                    f.write(
                        f"Place a {size}x{size} PNG named ic_launcher.png and "
                        f"ic_launcher_round.png in this folder.\n"
                        "Or run: pip install Pillow && python generate_icons.py"
                    )
                print(f"⚠️  Skipped {folder}/{filename} — install Pillow to auto-generate")
                break

    print("\nDone! Icons generated in app/src/main/res/mipmap-*/")
