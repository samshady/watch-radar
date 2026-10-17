#!/usr/bin/env python3
"""
Watch Radar Static Site Generator
Assembles templates into dist/index.html and root index.html.
Complies strictly with sam-web-design: Catppuccin Mocha palette + Atelier Champagne Gold,
Bricolage Grotesque + Inter + JetBrains Mono, interactive L2L caliper simulator,
Lume Darkroom mode, Care Lab manuals, and strict zero em-dashes.
"""
import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "watches.json")
DIST_DIR = os.path.join(BASE_DIR, "dist")
DIST_HTML = os.path.join(DIST_DIR, "index.html")
ROOT_HTML = os.path.join(BASE_DIR, "index.html")

sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))
from templates.head_css import HEAD_CSS
from templates.nav_header import NAV_HEADER_HTML
from templates.care_panels import CARE_PANELS_HTML
from templates.card_js import CARD_JS

def main():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        watches = json.load(f)

    watches_json_str = json.dumps(watches, ensure_ascii=False)
    js_section = CARD_JS.replace("__WATCH_DATA_PLACEHOLDER__", watches_json_str)

    full_html = HEAD_CSS + NAV_HEADER_HTML + CARE_PANELS_HTML + js_section

    os.makedirs(DIST_DIR, exist_ok=True)
    with open(DIST_HTML, "w", encoding="utf-8") as f:
        f.write(full_html)

    with open(ROOT_HTML, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"SUCCESS: Built {len(watches)} watches into {DIST_HTML} and {ROOT_HTML}")

if __name__ == "__main__":
    main()
