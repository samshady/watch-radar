#!/usr/bin/env python3
"""
Watch Radar Static Site Generator
Compiles data/watches.json into dist/index.html and root index.html
Adheres strictly to sam-web-design: Catppuccin Mocha palette, Bricolage Grotesque + Inter + JetBrains Mono,
interactive wrist fit simulator, and zero em-dashes.
"""
import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "watches.json")
DIST_DIR = os.path.join(BASE_DIR, "dist")
DIST_HTML = os.path.join(DIST_DIR, "index.html")
ROOT_HTML = os.path.join(BASE_DIR, "index.html")

def load_watches():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_html(watches):
    watches_json_str = json.dumps(watches, ensure_ascii=False)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Watch Radar: Budget & AliExpress Enthusiast Buyer Guide</title>
  <meta name="description" content="Curated budget watch tracker under 80 EUR/USD for average to smaller wrists. Real lug-to-lug specs, Seiko NH35 vs VH31 comparisons, and Choice Day prices.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --ctp-rosewater: #f5e0dc;
      --ctp-flamingo: #f2cdcd;
      --ctp-pink: #f5c2e7;
      --ctp-mauve: #cba6f7;
      --ctp-red: #f38ba8;
      --ctp-maroon: #eba0ac;
      --ctp-peach: #fab387;
      --ctp-yellow: #f9e2af;
      --ctp-green: #a6e3a1;
      --ctp-teal: #94e2d5;
      --ctp-sky: #89dceb;
      --ctp-sapphire: #74c7ec;
      --ctp-blue: #89b4fa;
      --ctp-lavender: #b4befe;
      --ctp-text: #cdd6f4;
      --ctp-subtext1: #bac2de;
      --ctp-subtext0: #a6adc8;
      --ctp-overlay2: #9399b2;
      --ctp-overlay1: #7f849c;
      --ctp-overlay0: #6c7086;
      --ctp-surface2: #585b70;
      --ctp-surface1: #45475a;
      --ctp-surface0: #313244;
      --ctp-base: #1e1e2e;
      --ctp-mantle: #181825;
      --ctp-crust: #11111b;

      --font-display: 'Bricolage Grotesque', system-ui, sans-serif;
      --font-body: 'Inter', system-ui, -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;

      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.25);
      --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.35);
      --transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background-color: var(--ctp-base);
      color: var(--ctp-text);
      font-family: var(--font-body);
      line-height: 1.55;
      -webkit-font-smoothing: antialiased;
      padding-bottom: 5rem;
    }}

    .container {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 1.25rem;
    }}

    header {{
      background: linear-gradient(180deg, var(--ctp-mantle) 0%, var(--ctp-base) 100%);
      border-bottom: 1px solid var(--ctp-surface0);
      padding: 2.5rem 0 2rem;
    }}

    .header-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(180, 190, 254, 0.12);
      color: var(--ctp-lavender);
      font-family: var(--font-mono);
      font-size: 0.8125rem;
      padding: 0.35rem 0.75rem;
      border-radius: 9999px;
      margin-bottom: 1rem;
      border: 1px solid rgba(180, 190, 254, 0.25);
    }}

    .header-badge span.dot {{
      width: 8px;
      height: 8px;
      background-color: var(--ctp-green);
      border-radius: 50%;
      box-shadow: 0 0 8px var(--ctp-green);
    }}

    h1 {{
      font-family: var(--font-display);
      font-size: clamp(2rem, 4vw, 3.25rem);
      font-weight: 800;
      letter-spacing: -0.03em;
      line-height: 1.1;
      color: #ffffff;
      margin-bottom: 0.75rem;
    }}

    .hero-lead {{
      font-size: 1.125rem;
      color: var(--ctp-subtext0);
      max-width: 840px;
      margin-bottom: 1.75rem;
    }}

    /* Highlights Banner */
    .doctrine-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1rem;
      margin-top: 1.5rem;
    }}

    .doctrine-card {{
      background: var(--ctp-surface0);
      border: 1px solid var(--ctp-surface1);
      border-radius: var(--radius-md);
      padding: 1.125rem;
      transition: var(--transition);
    }}

    .doctrine-card:hover {{
      border-color: var(--ctp-lavender);
      transform: translateY(-2px);
    }}

    .doctrine-title {{
      font-family: var(--font-display);
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--ctp-lavender);
      margin-bottom: 0.35rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .doctrine-desc {{
      font-size: 0.875rem;
      color: var(--ctp-subtext0);
      line-height: 1.45;
    }}

    /* Control Panel */
    .controls-card {{
      background: var(--ctp-mantle);
      border: 1px solid var(--ctp-surface0);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      margin: 2rem 0;
      box-shadow: var(--shadow-sm);
    }}

    .controls-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 1.25rem;
      align-items: flex-end;
    }}

    .control-group {{
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
    }}

    .control-label {{
      font-family: var(--font-display);
      font-size: 0.875rem;
      font-weight: 700;
      color: var(--ctp-subtext1);
      display: flex;
      justify-content: space-between;
    }}

    .control-input, .control-select {{
      background: var(--ctp-surface0);
      border: 1px solid var(--ctp-surface1);
      color: var(--ctp-text);
      font-family: var(--font-body);
      font-size: 0.9375rem;
      padding: 0.65rem 0.85rem;
      border-radius: var(--radius-sm);
      outline: none;
      min-height: 44px;
      transition: var(--transition);
    }}

    .control-input:focus, .control-select:focus {{
      border-color: var(--ctp-lavender);
      box-shadow: 0 0 0 2px rgba(180, 190, 254, 0.2);
    }}

    .slider-container {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      background: var(--ctp-surface0);
      padding: 0.5rem 0.85rem;
      border-radius: var(--radius-sm);
      border: 1px solid var(--ctp-surface1);
      min-height: 44px;
    }}

    .slider-input {{
      flex: 1;
      accent-color: var(--ctp-lavender);
      cursor: pointer;
      min-height: 24px;
    }}

    .slider-value {{
      font-family: var(--font-mono);
      font-size: 0.9375rem;
      font-weight: 600;
      color: var(--ctp-lavender);
      min-width: 60px;
      text-align: right;
    }}

    .toggle-row {{
      display: flex;
      gap: 0.5rem;
      margin-top: 1rem;
      flex-wrap: wrap;
    }}

    .price-pill {{
      background: var(--ctp-surface0);
      border: 1px solid var(--ctp-surface1);
      color: var(--ctp-subtext0);
      font-family: var(--font-mono);
      font-size: 0.8125rem;
      padding: 0.5rem 0.85rem;
      border-radius: 9999px;
      cursor: pointer;
      min-height: 44px;
      display: inline-flex;
      align-items: center;
      transition: var(--transition);
    }}

    .price-pill:hover {{
      color: var(--ctp-text);
      border-color: var(--ctp-overlay0);
      transform: translateY(-2px);
    }}

    .price-pill:active {{
      transform: scale(0.97);
    }}

    .price-pill.active {{
      background: rgba(180, 190, 254, 0.15);
      border-color: var(--ctp-lavender);
      color: var(--ctp-lavender);
      font-weight: 600;
    }}

    /* Metrics Summary Bar */
    .summary-stats {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1rem;
      margin-bottom: 1.5rem;
      padding: 0.5rem 0.25rem;
      font-size: 0.875rem;
      color: var(--ctp-overlay2);
    }}

    .count-indicator {{
      font-family: var(--font-mono);
      color: var(--ctp-subtext1);
      font-weight: 600;
    }}

    /* Watch Cards Grid */
    .watch-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 1.5rem;
    }}

    @media (max-width: 768px) {{
      .watch-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .watch-card {{
      background: var(--ctp-surface0);
      border: 1px solid var(--ctp-surface1);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: var(--shadow-sm);
      transition: var(--transition);
      position: relative;
    }}

    .watch-card:hover {{
      border-color: var(--ctp-lavender);
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
    }}

    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 0.75rem;
      margin-bottom: 0.75rem;
    }}

    .brand-pill {{
      font-family: var(--font-mono);
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--ctp-sky);
    }}

    .model-name {{
      font-family: var(--font-display);
      font-size: 1.35rem;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.25;
      margin: 0.15rem 0 0.25rem;
    }}

    .archetype-tag {{
      display: inline-block;
      font-size: 0.8125rem;
      color: var(--ctp-subtext0);
      margin-bottom: 0.75rem;
    }}

    .spec-score-badge {{
      display: flex;
      flex-direction: column;
      align-items: center;
      background: rgba(166, 227, 161, 0.12);
      border: 1px solid rgba(166, 227, 161, 0.3);
      color: var(--ctp-green);
      border-radius: var(--radius-sm);
      padding: 0.35rem 0.65rem;
      min-width: 58px;
    }}

    .score-label {{
      font-size: 0.625rem;
      font-family: var(--font-mono);
      text-transform: uppercase;
      opacity: 0.85;
    }}

    .score-number {{
      font-family: var(--font-mono);
      font-size: 1.125rem;
      font-weight: 700;
      line-height: 1.1;
    }}

    /* Dimensions Matrix */
    .specs-matrix {{
      background: var(--ctp-mantle);
      border-radius: var(--radius-md);
      padding: 0.85rem;
      margin: 0.75rem 0 1rem;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 0.5rem;
      text-align: center;
      border: 1px solid rgba(255, 255, 255, 0.04);
    }}

    .matrix-item {{
      display: flex;
      flex-direction: column;
    }}

    .matrix-label {{
      font-family: var(--font-mono);
      font-size: 0.6875rem;
      color: var(--ctp-overlay1);
      text-transform: uppercase;
      margin-bottom: 0.2rem;
    }}

    .matrix-value {{
      font-family: var(--font-mono);
      font-size: 0.875rem;
      font-weight: 600;
      color: var(--ctp-text);
      font-variant-numeric: tabular-nums;
    }}

    .matrix-value.highlight {{
      color: var(--ctp-lavender);
    }}

    /* Specs List */
    .specs-list {{
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
      font-size: 0.8125rem;
      margin-bottom: 1.25rem;
      color: var(--ctp-subtext0);
    }}

    .spec-row {{
      display: flex;
      justify-content: space-between;
      gap: 0.5rem;
      border-bottom: 1px dashed rgba(255, 255, 255, 0.05);
      padding-bottom: 0.25rem;
    }}

    .spec-key {{
      color: var(--ctp-overlay1);
      flex-shrink: 0;
    }}

    .spec-val {{
      color: var(--ctp-text);
      text-align: right;
      font-family: var(--font-mono);
      font-size: 0.78125rem;
    }}

    /* Wrist Fit Badge */
    .wrist-fit-box {{
      background: rgba(180, 190, 254, 0.08);
      border: 1px solid rgba(180, 190, 254, 0.2);
      border-radius: var(--radius-sm);
      padding: 0.65rem 0.85rem;
      margin-bottom: 1rem;
      font-size: 0.8125rem;
    }}

    .wrist-fit-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--ctp-lavender);
      margin-bottom: 0.25rem;
    }}

    .wrist-fit-desc {{
      color: var(--ctp-subtext0);
      line-height: 1.35;
    }}

    /* Pros Cons */
    .pros-cons {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.75rem;
      margin-bottom: 1rem;
      font-size: 0.75rem;
    }}

    .pros-list, .cons-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }}

    .pros-list li {{
      color: var(--ctp-green);
      position: relative;
      padding-left: 0.95rem;
      line-height: 1.3;
    }}

    .pros-list li::before {{
      content: "+";
      position: absolute;
      left: 0;
      font-weight: 700;
    }}

    .cons-list li {{
      color: var(--ctp-red);
      position: relative;
      padding-left: 0.95rem;
      line-height: 1.3;
    }}

    .cons-list li::before {{
      content: "-";
      position: absolute;
      left: 0;
      font-weight: 700;
    }}

    /* JOMW Quote */
    .jomw-callout {{
      background: var(--ctp-crust);
      border-left: 3px solid var(--ctp-yellow);
      padding: 0.65rem 0.85rem;
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      font-size: 0.78125rem;
      font-style: italic;
      color: var(--ctp-subtext1);
      margin-bottom: 1.25rem;
      line-height: 1.4;
    }}

    /* Card Footer & Pricing */
    .card-footer {{
      margin-top: auto;
      border-top: 1px solid var(--ctp-surface1);
      padding-top: 1rem;
      display: flex;
      align-items: baseline;
      justify-content: space-between;
    }}

    .price-block {{
      display: flex;
      flex-direction: column;
    }}

    .price-label {{
      font-size: 0.6875rem;
      font-family: var(--font-mono);
      text-transform: uppercase;
      color: var(--ctp-overlay1);
    }}

    .current-price {{
      font-family: var(--font-mono);
      font-size: 1.625rem;
      font-weight: 700;
      color: #ffffff;
      font-variant-numeric: tabular-nums;
    }}

    .price-tiers {{
      display: flex;
      gap: 0.45rem;
    }}

    .mini-price-chip {{
      font-family: var(--font-mono);
      font-size: 0.6875rem;
      padding: 0.25rem 0.5rem;
      border-radius: var(--radius-sm);
      background: var(--ctp-surface1);
      color: var(--ctp-subtext0);
    }}

    .mini-price-chip.deal {{
      background: rgba(166, 227, 161, 0.15);
      color: var(--ctp-green);
      font-weight: 600;
    }}

    /* Small Wrist Doctrine Deep Dive Section */
    .doctrine-section {{
      margin-top: 4rem;
      background: var(--ctp-mantle);
      border: 1px solid var(--ctp-surface0);
      border-radius: var(--radius-lg);
      padding: 2.25rem;
    }}

    .doctrine-section h2 {{
      font-family: var(--font-display);
      font-size: 1.85rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 0.75rem;
    }}

    .rules-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1.5rem;
      margin-top: 1.5rem;
    }}

    .rule-box {{
      background: var(--ctp-surface0);
      border: 1px solid var(--ctp-surface1);
      border-radius: var(--radius-md);
      padding: 1.25rem;
    }}

    .rule-number {{
      font-family: var(--font-mono);
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--ctp-yellow);
      margin-bottom: 0.35rem;
    }}

    .rule-title {{
      font-family: var(--font-display);
      font-size: 1.125rem;
      font-weight: 700;
      color: var(--ctp-text);
      margin-bottom: 0.5rem;
    }}

    .rule-text {{
      font-size: 0.875rem;
      color: var(--ctp-subtext0);
      line-height: 1.45;
    }}

    footer {{
      margin-top: 4rem;
      text-align: center;
      font-size: 0.8125rem;
      color: var(--ctp-overlay1);
      font-family: var(--font-mono);
    }}
  </style>
</head>
<body>

  <header>
    <div class="container">
      <div class="header-badge">
        <span class="dot"></span>
        <span>RADAR 2026 EDITION : BUDGET WATCH RADAR</span>
      </div>
      <h1>Watch Radar & Small Wrist Guide</h1>
      <p class="hero-lead">
        Curated AliExpress, gateway Japanese quartz, and enthusiast mechanical timepieces strictly under 80 EUR/USD.
        Built with deep Lug-to-Lug ergonomics for 15 cm to 17 cm (6.0 to 6.75 inch) wrists.
      </p>

      <div class="doctrine-grid">
        <div class="doctrine-card">
          <div class="doctrine-title">Lug-to-Lug Is King</div>
          <div class="doctrine-desc">
            Case diameter is a secondary metric. A 44 mm cushion watch with 46 mm lug-to-lug fits smaller wrists better than a flat 40 mm watch with 50 mm lugs.
          </div>
        </div>
        <div class="doctrine-card">
          <div class="doctrine-title">The Female Endlink Law</div>
          <div class="doctrine-desc">
            Male endlinks jut straight out and add 3 mm to 5 mm of rigid span. Female endlinks drop 90 degrees directly around the wrist curve.
          </div>
        </div>
        <div class="doctrine-card">
          <div class="doctrine-title">Seiko VH31 Sweep Quartz</div>
          <div class="doctrine-desc">
            Provides a smooth 4-ticks-per-second mechanical glide in ultra-slim 9 mm to 11 mm cases, avoiding the bulky 14 mm thickness of automatic NH35s.
          </div>
        </div>
      </div>
    </div>
  </header>

  <main class="container">
    <!-- Filter Controls Card -->
    <div class="controls-card">
      <div class="controls-grid">
        <div class="control-group">
          <label class="control-label" for="search-input">Search Watch / Specs</label>
          <input type="text" id="search-input" class="control-input" placeholder="Brand, movement, dial...">
        </div>

        <div class="control-group">
          <label class="control-label" for="archetype-filter">Archetype</label>
          <select id="archetype-filter" class="control-select">
            <option value="all">All Archetypes</option>
            <option value="Dive">Dive Homages & Divers</option>
            <option value="Dress">Dress / GADA / Everyday</option>
            <option value="Field">Field & Military</option>
            <option value="Chronograph">Chronographs (Meca-Quartz)</option>
            <option value="Aviation">Pilot / Flieger</option>
            <option value="Digital">Digital Retro</option>
            <option value="Astronomical">Astronomical / Complications</option>
          </select>
        </div>

        <div class="control-group">
          <label class="control-label" for="movement-filter">Movement Engine</label>
          <select id="movement-filter" class="control-select">
            <option value="all">All Movements</option>
            <option value="VH31">Seiko VH31 (Sweep Quartz)</option>
            <option value="NH35">Seiko NH35 (Automatic)</option>
            <option value="VK63">Seiko VK63 (Meca-Quartz Chrono)</option>
            <option value="Seagull">Seagull Mechanical</option>
            <option value="Casio">Casio Module</option>
          </select>
        </div>

        <div class="control-group">
          <div class="control-label">
            <span>Max Lug-to-Lug</span>
            <span id="l2l-display">50 mm</span>
          </div>
          <div class="slider-container">
            <input type="range" id="l2l-slider" class="slider-input" min="32" max="50" step="0.5" value="50">
            <span class="slider-value" id="l2l-val-text">50.0mm</span>
          </div>
        </div>
      </div>

      <div class="toggle-row">
        <span style="font-size: 0.8125rem; font-family: var(--font-mono); color: var(--ctp-overlay1); align-self: center; margin-right: 0.5rem;">Price Basis:</span>
        <button class="price-pill active" data-price-mode="choice">Ali Choice / Regular Deal</button>
        <button class="price-pill" data-price-mode="singles_day">11.11 Singles Day Lowest</button>
        <button class="price-pill" data-price-mode="street">Standard Retail</button>
      </div>
    </div>

    <!-- Stats Bar -->
    <div class="summary-stats">
      <div>Showing <span id="visible-count" class="count-indicator">0</span> of <span id="total-count" class="count-indicator">0</span> curated timepieces strictly under 80 EUR</div>
      <div>Sorted by: <span style="color: var(--ctp-lavender); font-weight: 600;">JOMW Spec Score</span></div>
    </div>

    <!-- Watches Card Grid -->
    <div class="watch-grid" id="watch-grid">
      <!-- Injected by JavaScript -->
    </div>

    <!-- Small Wrist Doctrine Section -->
    <section class="doctrine-section">
      <h2>The Small Wrist Doctrine (15 cm to 17 cm)</h2>
      <p style="color: var(--ctp-subtext0); max-width: 800px; font-size: 0.9375rem;">
        Collecting watches with a wrist circumference under 17 cm (6.7 inches) requires understanding how case architecture behaves in the real world. Here are the five golden rules of budget watch collecting.
      </p>

      <div class="rules-grid">
        <div class="rule-box">
          <div class="rule-number">RULE 01</div>
          <div class="rule-title">Lug-to-Lug Under 46.5 mm</div>
          <div class="rule-text">
            The flat surface across the top of a 15.5 cm wrist measures approximately 48 mm to 50 mm. Any watch with a lug-to-lug over 47 mm risks overhang where the strap drops at an awkward hollow angle.
          </div>
        </div>

        <div class="rule-box">
          <div class="rule-number">RULE 02</div>
          <div class="rule-title">Beware The Male Endlink Penalty</div>
          <div class="rule-text">
            Budget brands often save costs using male center links on steel bracelets. A 46 mm lug-to-lug case with male endlinks wears like 50 mm. Always inspect bracelet endlink architecture before buying.
          </div>
        </div>

        <div class="rule-box">
          <div class="rule-number">RULE 03</div>
          <div class="rule-title">The NH35 Thickness Dilemma</div>
          <div class="rule-text">
            The Seiko NH35 is bulletproof, but the movement itself is 5.32 mm tall. In small cases, this produces a hockey-puck proportion of 13 mm to 14 mm thickness. The watch wobbles and catches on dress cuffs.
          </div>
        </div>

        <div class="rule-box">
          <div class="rule-number">RULE 04</div>
          <div class="rule-title">The VH31 Slim Sweet Spot</div>
          <div class="rule-text">
            Seiko VH31 quartz ticks 4 times per second, giving the smooth glide of mechanical movement in a 3.45 mm slim package. This unlocks 9 mm to 11 mm cases that hug wrist bones like tailored leather.
          </div>
        </div>

        <div class="rule-box">
          <div class="rule-number">RULE 05</div>
          <div class="rule-title">How To Buy On AliExpress</div>
          <div class="rule-text">
            Never pay retail on AliExpress. Use Choice Day during the 1st through 5th of each month for free 7-to-10 day delivery with European VAT already collected (no customs friction). Save major purchases for 11.11.
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer>
    <div class="container">
      Watch Radar 2026. Built for budget horology enthusiasts and smaller wrists. Strict zero em-dashes.
    </div>
  </footer>

  <script>
    const WATCH_DATA = {watches_json_str};
    let currentPriceMode = 'choice';

    const searchInput = document.getElementById('search-input');
    const archetypeFilter = document.getElementById('archetype-filter');
    const movementFilter = document.getElementById('movement-filter');
    const l2lSlider = document.getElementById('l2l-slider');
    const l2lDisplay = document.getElementById('l2l-display');
    const l2lValText = document.getElementById('l2l-val-text');
    const visibleCount = document.getElementById('visible-count');
    const totalCount = document.getElementById('total-count');
    const watchGrid = document.getElementById('watch-grid');
    const pricePills = document.querySelectorAll('.price-pill');

    totalCount.textContent = WATCH_DATA.length;

    function renderWatches() {{
      const query = searchInput.value.toLowerCase().trim();
      const archetype = archetypeFilter.value;
      const movement = movementFilter.value;
      const maxL2L = parseFloat(l2lSlider.value);

      const filtered = WATCH_DATA.filter(w => {{
        if (w.lug_to_lug_mm > maxL2L) return false;
        if (archetype !== 'all' && !w.archetype.includes(archetype)) return false;
        if (movement !== 'all' && !w.movement.includes(movement)) return false;
        if (query) {{
          const haystack = (w.brand + ' ' + w.model + ' ' + w.archetype + ' ' + w.movement + ' ' + w.crystal + ' ' + w.wrist_notes).toLowerCase();
          if (!haystack.includes(query)) return false;
        }}
        return true;
      }});

      // Sort by JOMW Spec Score descending
      filtered.sort((a, b) => b.jomw_spec_score - a.jomw_spec_score);

      visibleCount.textContent = filtered.length;

      if (filtered.length === 0) {{
        watchGrid.innerHTML = `
          <div style="grid-column: 1 / -1; padding: 3rem 1rem; text-align: center; background: var(--ctp-surface0); border-radius: var(--radius-lg); border: 1px dashed var(--ctp-surface2);">
            <p style="font-family: var(--font-display); font-size: 1.25rem; color: var(--ctp-subtext1); margin-bottom: 0.5rem;">No watches match your filter criteria</p>
            <p style="font-size: 0.875rem; color: var(--ctp-overlay1);">Try raising the Lug-to-Lug slider or resetting search parameters.</p>
          </div>
        `;
        return;
      }}

      watchGrid.innerHTML = filtered.map(w => {{
        let displayPrice = w.choice_price_eur;
        let priceLabel = 'Ali Choice Price';
        if (currentPriceMode === 'singles_day') {{
          displayPrice = w.singles_day_price_eur;
          priceLabel = '11.11 Lowest';
        }} else if (currentPriceMode === 'street') {{
          displayPrice = w.street_price_eur;
          priceLabel = 'Standard Retail';
        }}

        const prosHtml = w.pros.map(p => `<li>${{p}}</li>`).join('');
        const consHtml = w.cons.map(c => `<li>${{c}}</li>`).join('');

        return `
          <article class="watch-card">
            <div>
              <div class="card-top">
                <div>
                  <span class="brand-pill">${{w.brand}}</span>
                  <h3 class="model-name">${{w.model}}</h3>
                  <span class="archetype-tag">${{w.archetype}}</span>
                </div>
                <div class="spec-score-badge">
                  <span class="score-label">JOMW</span>
                  <span class="score-number">${{w.jomw_spec_score}}</span>
                </div>
              </div>

              <div class="specs-matrix">
                <div class="matrix-item">
                  <span class="matrix-label">Case</span>
                  <span class="matrix-value">${{w.case_diameter_mm}}mm</span>
                </div>
                <div class="matrix-item">
                  <span class="matrix-label">Lug-To-Lug</span>
                  <span class="matrix-value highlight">${{w.lug_to_lug_mm}}mm</span>
                </div>
                <div class="matrix-item">
                  <span class="matrix-label">Thick</span>
                  <span class="matrix-value">${{w.thickness_mm}}mm</span>
                </div>
                <div class="matrix-item">
                  <span class="matrix-label">Lug</span>
                  <span class="matrix-value">${{w.lug_width_mm}}mm</span>
                </div>
              </div>

              <div class="wrist-fit-box">
                <div class="wrist-fit-header">
                  <span>WRIST FIT RATING</span>
                  <span>${{w.wrist_fit_tier}}</span>
                </div>
                <div class="wrist-fit-desc">${{w.wrist_notes}}</div>
              </div>

              <div class="specs-list">
                <div class="spec-row">
                  <span class="spec-key">Engine</span>
                  <span class="spec-val">${{w.movement}}</span>
                </div>
                <div class="spec-row">
                  <span class="spec-key">Glass</span>
                  <span class="spec-val">${{w.crystal}}</span>
                </div>
                <div class="spec-row">
                  <span class="spec-key">Bezel</span>
                  <span class="spec-val">${{w.bezel}}</span>
                </div>
                <div class="spec-row">
                  <span class="spec-key">Water Resist</span>
                  <span class="spec-val">${{w.water_resistance_m}}m / ${{w.water_resistance_m >= 100 ? 'Screw Crown' : 'Push-Pull'}}</span>
                </div>
                <div class="spec-row">
                  <span class="spec-key">Endlinks</span>
                  <span class="spec-val">${{w.endlinks}}</span>
                </div>
                <div class="spec-row">
                  <span class="spec-key">Lume</span>
                  <span class="spec-val">${{w.lume}}</span>
                </div>
              </div>

              <div class="pros-cons">
                <ul class="pros-list">${{prosHtml}}</ul>
                <ul class="cons-list">${{consHtml}}</ul>
              </div>

              <div class="jomw-callout">
                "${{w.jomw_quote}}"
              </div>
            </div>

            <div class="card-footer">
              <div class="price-block">
                <span class="price-label">${{priceLabel}}</span>
                <span class="current-price">&euro;${{displayPrice.toFixed(0)}}</span>
              </div>
              <div class="price-tiers">
                <span class="mini-price-chip" title="Retail">&euro;${{w.street_price_eur.toFixed(0)}}</span>
                <span class="mini-price-chip deal" title="Ali Choice">&euro;${{w.choice_price_eur.toFixed(0)}}</span>
                <span class="mini-price-chip" title="11.11 Lowest" style="color: var(--ctp-peach);">&euro;${{w.singles_day_price_eur.toFixed(0)}}</span>
              </div>
            </div>
          </article>
        `;
      }}).join('');
    }}

    // Event Listeners
    searchInput.addEventListener('input', renderWatches);
    archetypeFilter.addEventListener('change', renderWatches);
    movementFilter.addEventListener('change', renderWatches);

    l2lSlider.addEventListener('input', (e) => {{
      const val = parseFloat(e.target.value).toFixed(1);
      l2lDisplay.textContent = val + ' mm';
      l2lValText.textContent = val + 'mm';
      renderWatches();
    }});

    pricePills.forEach(pill => {{
      pill.addEventListener('click', () => {{
        pricePills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        currentPriceMode = pill.getAttribute('data-price-mode');
        renderWatches();
      }});
    }});

    // Initial render
    renderWatches();
  </script>
</body>
</html>
"""
    return html

def main():
    watches = load_watches()
    html_content = generate_html(watches)
    
    os.makedirs(DIST_DIR, exist_ok=True)
    with open(DIST_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    with open(ROOT_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"PASS: Built {len(watches)} watches into {DIST_HTML} and {ROOT_HTML}")

if __name__ == "__main__":
    main()
