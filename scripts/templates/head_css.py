# scripts/templates/head_css.py
# Styling, horological finishing textures, and head metadata for Watch Radar

HEAD_CSS = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Watch Radar: Budget &amp; AliExpress Enthusiast Guide (2026)</title>
  <meta name="description" content="Curated budget horology guide under 80 EUR for average and smaller wrists. Real micrometer lug-to-lug specs, Seiko NH35 vs VH31 sweeping quartz comparisons, and Choice Day prices.">
  <link rel="icon" type="image/svg+xml" href="favicon.svg">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

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

    html, body {
      max-width: 100vw;
      overflow-x: hidden;
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
        radial-gradient(circle at 50% 0%, rgba(238, 212, 159, 0.04) 0%, transparent 75%),
        repeating-linear-gradient(90deg, rgba(255, 255, 255, 0.008) 0px, rgba(255, 255, 255, 0.008) 1px, transparent 1px, transparent 24px);
    }

    /* Côtes de Genève (Geneva Waves) Texture */
    .cotes-de-geneve {
      background-image: repeating-linear-gradient(
        90deg,
        rgba(255, 255, 255, 0.015) 0px,
        rgba(255, 255, 255, 0.015) 14px,
        rgba(0, 0, 0, 0.04) 14px,
        rgba(0, 0, 0, 0.04) 28px
      );
    }

    /* Chemin de Fer (Railway Minute Track) Divider */
    .chemin-de-fer {
      height: 10px;
      width: 100%;
      margin: 1.75rem 0;
      background: 
        linear-gradient(to bottom, var(--gold-border), var(--gold-border) 1px, transparent 1px, transparent 8px, var(--gold-border) 8px),
        repeating-linear-gradient(to right, var(--gold-border) 0, var(--gold-border) 1px, transparent 1px, transparent 8px);
      opacity: 0.65;
    }

    /* Coin-Edge Milled Knurling */
    .coin-edge-top {
      border-top: 2px dashed var(--gold-border);
      position: relative;
    }

    /* Super-LumiNova Darkroom Mode */
    body.lume-mode {
      background-color: #07070a;
      color: #94a3b8;
      background-image: 
        radial-gradient(circle at 50% 10%, rgba(0, 229, 255, 0.05) 0%, transparent 60%),
        radial-gradient(circle at 80% 80%, rgba(57, 255, 20, 0.04) 0%, transparent 50%);
    }

    body.lume-mode .watch-card {
      background: #0d0e14;
      border-color: rgba(0, 229, 255, 0.25);
      box-shadow: 0 0 25px -5px rgba(0, 229, 255, 0.15);
    }

    body.lume-mode .lume-target {
      color: var(--lume-bgw9) !important;
      text-shadow: 0 0 10px rgba(0, 229, 255, 0.8), 0 0 22px rgba(0, 229, 255, 0.45);
    }

    body.lume-mode .lume-target-c3 {
      color: var(--lume-c3) !important;
      text-shadow: 0 0 10px rgba(57, 255, 20, 0.8), 0 0 22px rgba(57, 255, 20, 0.45);
    }

    body.lume-mode .watch-thumb-img {
      filter: brightness(0.95) contrast(1.15) drop-shadow(0 0 14px rgba(0, 229, 255, 0.35));
    }

    /* 365nm UV Torch Charge Strobe Animation */
    @keyframes uvTorchSweep {
      0% {
        transform: translateX(-100%) skewX(-20deg);
        opacity: 0;
      }
      20% {
        opacity: 0.9;
      }
      60% {
        opacity: 1;
      }
      100% {
        transform: translateX(200%) skewX(-20deg);
        opacity: 0;
      }
    }

    .uv-strobe-overlay {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 9999;
      background: linear-gradient(
        90deg,
        transparent 0%,
        rgba(138, 43, 226, 0.28) 25%,
        rgba(0, 229, 255, 0.65) 50%,
        rgba(147, 112, 219, 0.35) 75%,
        transparent 100%
      );
      filter: blur(16px);
      animation: uvTorchSweep 0.85s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
    }

    /* Hyper-excited Phosphorescence with realistic exponential decay */
    @keyframes phosphorescentDecay {
      0% {
        filter: drop-shadow(0 0 30px #00e5ff) brightness(1.4);
      }
      30% {
        filter: drop-shadow(0 0 20px #00e5ff) brightness(1.2);
      }
      100% {
        filter: drop-shadow(0 0 10px rgba(0, 229, 255, 0.6)) brightness(0.95);
      }
    }

    body.lume-mode .watch-thumb-img {
      animation: phosphorescentDecay 2.5s ease-out forwards;
    }

    /* Sunburst Metallic Dial Sheen on Card Hover */
    .watch-card-media {
      position: relative;
      overflow: hidden;
      background: #11111b;
      aspect-ratio: 16/10;
      border-bottom: 1px solid var(--ctp-surface0);
    }

    .watch-card-media::after {
      content: "";
      position: absolute;
      inset: 0;
      pointer-events: none;
      background: radial-gradient(
        circle at var(--sheen-x, 50%) var(--sheen-y, 50%),
        rgba(255, 255, 255, 0.16) 0%,
        rgba(238, 212, 159, 0.08) 25%,
        transparent 65%
      );
      opacity: 0;
      transition: opacity 0.3s ease;
    }

    .watch-card:hover .watch-card-media::after {
      opacity: 1;
    }

    .container {
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 1.25rem;
      width: 100%;
      box-sizing: border-box;
    }

    /* Top Ecosystem Cross-Nav Bar */
    .radar-ecosystem-bar {
      background-color: var(--ctp-crust);
      border-bottom: 1px solid var(--ctp-surface0);
      font-family: var(--font-mono);
      font-size: 0.75rem;
      padding: 0.4rem 1rem;
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(8px);
      width: 100%;
      box-sizing: border-box;
    }

    .ecosystem-container {
      max-width: 1280px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      width: 100%;
    }

    .ecosystem-brand {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--ctp-subtext0);
      white-space: nowrap;
      flex-shrink: 0;
    }

    .pulse-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background-color: var(--gold-primary);
      box-shadow: 0 0 8px var(--gold-primary);
      display: inline-block;
      flex-shrink: 0;
    }

    .ecosystem-links {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      overflow-x: auto;
      padding-bottom: 2px;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
    }
    .ecosystem-links::-webkit-scrollbar {
      display: none;
    }

    .ecosystem-link {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.4rem 0.65rem;
      min-height: 44px;
      border-radius: var(--radius-sm);
      color: var(--ctp-subtext1);
      text-decoration: none;
      border: 1px solid transparent;
      transition: var(--transition);
      white-space: nowrap;
      box-sizing: border-box;
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

    /* Tactile physics with Fitts's Law touch target standards */
    .btn-tactile {
      transition: all 0.15s ease;
      user-select: none;
      cursor: pointer;
      min-height: 44px;
      box-sizing: border-box;
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
      box-sizing: border-box;
    }

    .atelier-card:hover {
      border-color: var(--gold-border);
      transform: translateY(-2px);
      box-shadow: 0 10px 24px -10px rgba(0, 0, 0, 0.6);
    }

    /* Grid */
    .watch-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 1.5rem;
      margin-top: 1.5rem;
    }

    /* Escapement Simulator Buttons */
    .escapement-btn {
      min-height: 44px;
      padding: 0.5rem 0.85rem;
      border-radius: var(--radius-sm);
      background: var(--ctp-surface0);
      border: 1px solid var(--ctp-surface1);
      color: var(--ctp-text);
      font-family: var(--font-mono);
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 0.15rem;
      cursor: pointer;
      box-sizing: border-box;
      flex: 1 1 160px;
    }

    .escapement-btn.active {
      background: var(--gold-bg);
      border-color: var(--gold-border);
      color: var(--gold-primary);
    }

    /* Pricing Tabs */
    .price-tab-btn {
      min-height: 44px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 0.45rem 0.85rem;
      box-sizing: border-box;
    }

    /* Vernier Caliper Hatch Marks */
    .vernier-scale {
      background-image: repeating-linear-gradient(
        90deg,
        var(--ctp-overlay0) 0px,
        var(--ctp-overlay0) 1px,
        transparent 1px,
        transparent 10%
      );
      height: 6px;
      width: 100%;
      margin-top: 4px;
      opacity: 0.45;
    }

    /* Responsive Helpers */
    @media (max-width: 640px) {
      .sm-hidden {
        display: none !important;
      }
      .watch-grid {
        grid-template-columns: 1fr;
      }
      .container {
        padding: 0 0.85rem;
      }
      .atelier-card {
        padding: 1rem;
      }
    }
  </style>
</head>
"""
