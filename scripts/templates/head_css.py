# scripts/templates/head_css.py
# Styling and head metadata for Watch Radar

HEAD_CSS = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Watch Radar: Budget &amp; AliExpress Enthusiast Guide (2026)</title>
  <meta name="description" content="Curated budget watch tracker under 80 EUR for average and smaller wrists. Real lug-to-lug specs, Seiko NH35 vs VH31 comparisons, and Choice Day prices.">
  <link rel="icon" type="image/svg+xml" href="favicon.svg">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>

  <style>
    :root {
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

      /* Atelier Champagne Gold accents */
      --gold-primary: #eed49f;
      --gold-hover: #f5e0b8;
      --gold-dim: #c6a052;
      --gold-bg: rgba(238, 212, 159, 0.08);
      --gold-border: rgba(238, 212, 159, 0.25);

      /* Super-LumiNova Glow colors */
      --lume-bgw9: #00e5ff;
      --lume-c3: #39ff14;

      --font-display: 'Bricolage Grotesque', system-ui, -apple-system, sans-serif;
      --font-body: 'Inter', system-ui, -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;

      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
      --radius-xl: 20px;
      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.25);
      --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.35);
      --transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--ctp-base);
      color: var(--ctp-text);
      font-family: var(--font-body);
      line-height: 1.55;
      -webkit-font-smoothing: antialiased;
      padding-bottom: 5rem;
      transition: background-color 0.4s ease, color 0.4s ease;
      background-image: 
        radial-gradient(circle at 50% 0%, rgba(238, 212, 159, 0.03) 0%, transparent 75%),
        repeating-radial-gradient(circle at 100% 100%, transparent 0, rgba(255, 255, 255, 0.007) 1px, transparent 2px);
    }

    /* Super-LumiNova Darkroom Mode */
    body.lume-mode {
      background-color: #07070a;
      color: #94a3b8;
      background-image: 
        radial-gradient(circle at 50% 10%, rgba(0, 229, 255, 0.04) 0%, transparent 60%),
        radial-gradient(circle at 80% 80%, rgba(57, 255, 20, 0.03) 0%, transparent 50%);
    }

    body.lume-mode .watch-card {
      background: #0d0e14;
      border-color: rgba(0, 229, 255, 0.2);
      box-shadow: 0 0 25px -5px rgba(0, 229, 255, 0.12);
    }

    body.lume-mode .lume-target {
      color: var(--lume-bgw9) !important;
      text-shadow: 0 0 10px rgba(0, 229, 255, 0.8), 0 0 20px rgba(0, 229, 255, 0.4);
    }

    body.lume-mode .lume-target-c3 {
      color: var(--lume-c3) !important;
      text-shadow: 0 0 10px rgba(57, 255, 20, 0.8), 0 0 20px rgba(57, 255, 20, 0.4);
    }

    body.lume-mode .watch-thumb-img {
      filter: brightness(0.92) contrast(1.15) drop-shadow(0 0 12px rgba(0, 229, 255, 0.3));
    }

    .container {
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 1.25rem;
    }

    /* Top Ecosystem Cross-Nav Bar */
    .radar-ecosystem-bar {
      background-color: var(--ctp-crust);
      border-bottom: 1px solid var(--ctp-surface0);
      font-family: var(--font-mono);
      font-size: 0.75rem;
      padding: 0.45rem 1rem;
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(8px);
    }

    .ecosystem-container {
      max-width: 1280px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }

    .ecosystem-brand {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--ctp-subtext0);
      white-space: nowrap;
    }

    .pulse-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background-color: var(--gold-primary);
      box-shadow: 0 0 8px var(--gold-primary);
      display: inline-block;
    }

    .ecosystem-links {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      overflow-x: auto;
      padding-bottom: 2px;
    }

    .ecosystem-link {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.25rem 0.65rem;
      border-radius: var(--radius-sm);
      color: var(--ctp-subtext1);
      text-decoration: none;
      border: 1px solid transparent;
      transition: var(--transition);
      white-space: nowrap;
    }

    .ecosystem-link:hover {
      color: #fff;
      background-color: var(--ctp-surface0);
      border-color: var(--ctp-surface1);
    }

    .ecosystem-link.active {
      color: var(--gold-primary);
      background-color: var(--gold-bg);
      border-color: var(--gold-border);
      font-weight: 600;
    }

    /* Tactile physics */
    .btn-tactile {
      transition: all 0.15s ease;
      user-select: none;
      cursor: pointer;
    }

    .btn-tactile:hover {
      transform: translateY(-2px);
    }

    .btn-tactile:active {
      transform: scale(0.97);
    }

    /* Cards */
    .atelier-card {
      background-color: var(--ctp-mantle);
      border: 1px solid var(--ctp-surface0);
      border-radius: var(--radius-lg);
      padding: 1.25rem;
      transition: var(--transition);
    }

    .atelier-card:hover {
      border-color: var(--gold-border);
      transform: translateY(-2px);
      box-shadow: 0 10px 24px -10px rgba(0, 0, 0, 0.6);
    }

    /* Grid */
    .watch-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
      gap: 1.5rem;
      margin-top: 1.5rem;
    }

    @media (max-width: 640px) {
      .watch-grid {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
"""
