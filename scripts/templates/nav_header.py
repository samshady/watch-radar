# scripts/templates/nav_header.py
# Top ecosystem navigation, header, caliper simulator, and filter controls

NAV_HEADER_HTML = """
  <!-- Top Ecosystem Cross-Nav Bar -->
  <div class="radar-ecosystem-bar">
    <div class="ecosystem-container">
      <div class="ecosystem-brand">
        <span class="pulse-dot"></span>
        <strong style="color: var(--gold-primary);">RADAR ECOSYSTEM</strong>
        <span style="color: var(--ctp-overlay0);" class="hidden sm:inline">|</span>
        <span style="color: var(--ctp-subtext0);" class="hidden sm:inline">Curated enthusiast guides for budget gems</span>
      </div>
      <div class="ecosystem-links">
        <a href="https://samshady.github.io/watch-radar/" class="ecosystem-link active" title="Current Site: Watch Radar">
          <i class="fa-solid fa-stopwatch" style="color: var(--gold-primary);"></i>
          <span>Watch Radar</span>
        </a>
        <a href="https://samshady.github.io/iem-radar/" class="ecosystem-link" title="Explore IEM Radar">
          <i class="fa-solid fa-headphones" style="color: var(--ctp-sapphire);"></i>
          <span>IEM Radar</span>
        </a>
        <a href="https://samshady.github.io/retro-handhelds-radar/" class="ecosystem-link" title="Explore Retro Handhelds Radar">
          <i class="fa-solid fa-gamepad" style="color: var(--ctp-peach);"></i>
          <span>Retro Handhelds</span>
        </a>
      </div>
    </div>
  </div>

  <header style="background: linear-gradient(180deg, var(--ctp-mantle) 0%, var(--ctp-base) 100%); border-bottom: 1px solid var(--ctp-surface0); padding: 2.5rem 0 2rem;">
    <div class="container">
      <div style="display: flex; flex-direction: column; md:flex-row; justify-content: space-between; gap: 1.5rem; align-items: flex-start;">
        <div>
          <div style="display: inline-flex; align-items: center; gap: 0.5rem; background: var(--gold-bg); border: 1px solid var(--gold-border); padding: 0.25rem 0.75rem; border-radius: 9999px; margin-bottom: 0.75rem;">
            <i class="fa-solid fa-compass-drafting" style="color: var(--gold-primary); font-size: 0.8rem;"></i>
            <span style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 600; color: var(--gold-primary); letter-spacing: 0.05em; text-transform: uppercase;">Horological Atelier Edition</span>
          </div>
          <h1 style="font-family: var(--font-display); font-size: clamp(2rem, 5vw, 2.75rem); font-weight: 800; color: #fff; letter-spacing: -0.03em; line-height: 1.15; margin-bottom: 0.5rem;">
            Watch Radar <span style="font-weight: 400; color: var(--gold-primary); font-size: 0.7em;">2026</span>
          </h1>
          <p style="color: var(--ctp-subtext1); font-size: 1.05rem; max-width: 720px; line-height: 1.6;">
            Curated budget horology guide strictly under &euro;80. Real micrometer lug-to-lug specs, Seiko NH35 vs VH31 sweeping quartz comparisons, and ergonomic small-wrist verdicts.
          </p>
        </div>

        <!-- Quick actions -->
        <div style="display: flex; flex-wrap: wrap; gap: 0.6rem; align-items: center; margin-top: 0.5rem;">
          <button id="lume-toggle-btn" class="btn-tactile" style="display: inline-flex; align-items: center; gap: 0.5rem; background: var(--ctp-surface0); color: var(--ctp-text); border: 1px solid var(--ctp-surface1); padding: 0.6rem 1rem; border-radius: var(--radius-md); font-family: var(--font-mono); font-size: 0.825rem; font-weight: 600;">
            <i class="fa-solid fa-moon" style="color: var(--lume-bgw9);"></i>
            <span id="lume-btn-text">Lume Darkroom: OFF</span>
          </button>
          <a href="#caliper-lab" class="btn-tactile" style="display: inline-flex; align-items: center; gap: 0.5rem; background: var(--gold-bg); color: var(--gold-primary); border: 1px solid var(--gold-border); padding: 0.6rem 1rem; border-radius: var(--radius-md); font-family: var(--font-mono); font-size: 0.825rem; font-weight: 600; text-decoration: none;">
            <i class="fa-solid fa-ruler-horizontal"></i>
            <span>Caliper Lab</span>
          </a>
          <a href="#care-lab" class="btn-tactile" style="display: inline-flex; align-items: center; gap: 0.5rem; background: var(--ctp-surface0); color: var(--ctp-text); border: 1px solid var(--ctp-surface1); padding: 0.6rem 1rem; border-radius: var(--radius-md); font-family: var(--font-mono); font-size: 0.825rem; font-weight: 600; text-decoration: none;">
            <i class="fa-solid fa-screwdriver-wrench" style="color: var(--ctp-teal);"></i>
            <span>Care &amp; Toolkit</span>
          </a>
        </div>
      </div>
    </div>
  </header>

  <main class="container" style="margin-top: 2rem;">
    <!-- Digital Caliper L2L Simulator Section -->
    <section id="caliper-lab" class="atelier-card" style="margin-bottom: 2rem; border-color: var(--gold-border); background: linear-gradient(135deg, rgba(238, 212, 159, 0.05) 0%, var(--ctp-mantle) 100%);">
      <div style="display: flex; flex-direction: column; md:flex-row; justify-content: space-between; gap: 1.5rem; margin-bottom: 1.25rem;">
        <div>
          <div style="display: flex; align-items: center; gap: 0.5rem; font-family: var(--font-mono); font-size: 0.75rem; color: var(--gold-primary); text-transform: uppercase; letter-spacing: 0.05em; font-weight: 700;">
            <i class="fa-solid fa-ruler-combined"></i>
            <span>Digital Caliper Simulator: True Ergonomics</span>
          </div>
          <h2 style="font-family: var(--font-display); font-size: 1.5rem; font-weight: 700; color: #fff; margin-top: 0.25rem;">
            Lug-To-Lug vs Flat Wrist Span
          </h2>
          <p style="color: var(--ctp-subtext0); font-size: 0.9rem; margin-top: 0.25rem; max-width: 650px;">
            Case diameter is a vanity metric. What decides whether a watch looks tailored or comical on a 15 to 17 cm wrist is the lug-to-lug span compared to your flat bone width.
          </p>
        </div>

        <div style="background: var(--ctp-surface0); padding: 0.85rem 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--ctp-surface1); display: flex; align-items: center; gap: 1.5rem;">
          <div>
            <div style="font-size: 0.7rem; font-family: var(--font-mono); color: var(--ctp-overlay1); text-transform: uppercase;">Selected Wrist</div>
            <div id="wrist-circumference-display" style="font-family: var(--font-display); font-size: 1.5rem; font-weight: 700; color: var(--gold-primary);">16.5 cm / 6.5"</div>
          </div>
          <div style="height: 36px; width: 1px; background: var(--ctp-surface2);"></div>
          <div>
            <div style="font-size: 0.7rem; font-family: var(--font-mono); color: var(--ctp-overlay1); text-transform: uppercase;">Flat Top Span</div>
            <div id="flat-span-display" style="font-family: var(--font-mono); font-size: 1.5rem; font-weight: 700; color: var(--ctp-green);">47.0 mm</div>
          </div>
        </div>
      </div>

      <!-- Slider Control -->
      <div style="background: var(--ctp-crust); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--ctp-surface0);">
        <div style="display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-subtext0); margin-bottom: 0.5rem;">
          <span>14.5 cm (5.7" slender)</span>
          <span style="color: var(--gold-primary); font-weight: 600;">Drag slider to match your wrist</span>
          <span>19.0 cm (7.5" broad)</span>
        </div>
        <input type="range" id="wrist-slider" min="14.5" max="19.0" step="0.25" value="16.5" style="width: 100%; accent-color: var(--gold-primary); cursor: pointer; height: 8px;">
        
        <div style="margin-top: 1rem; display: flex; flex-wrap: wrap; gap: 0.75rem; font-size: 0.8rem; font-family: var(--font-mono);">
          <span style="display: inline-flex; align-items: center; gap: 0.4rem; color: var(--ctp-green); background: rgba(166, 227, 161, 0.1); padding: 0.3rem 0.6rem; border-radius: 4px;">
            <i class="fa-solid fa-circle-check"></i> &lt; 45.0 mm: Tailored Zero Overhang
          </span>
          <span style="display: inline-flex; align-items: center; gap: 0.4rem; color: var(--ctp-yellow); background: rgba(249, 226, 175, 0.1); padding: 0.3rem 0.6rem; border-radius: 4px;">
            <i class="fa-solid fa-circle-exclamation"></i> 45.0 to 47.5 mm: Borderline Flush
          </span>
          <span style="display: inline-flex; align-items: center; gap: 0.4rem; color: var(--ctp-red); background: rgba(243, 139, 168, 0.1); padding: 0.3rem 0.6rem; border-radius: 4px;">
            <i class="fa-solid fa-triangle-exclamation"></i> &gt; 47.5 mm: Overhang Alert for Small Wrists
          </span>
        </div>
      </div>
    </section>

    <!-- Filter & Search Controls -->
    <section class="atelier-card" style="margin-bottom: 2rem;">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; align-items: end;">
        <!-- Search -->
        <div>
          <label for="search-input" style="display: block; font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-subtext0); margin-bottom: 0.35rem; text-transform: uppercase;">Search Collection</label>
          <div style="position: relative;">
            <i class="fa-solid fa-magnifying-glass" style="position: absolute; left: 0.85rem; top: 50%; transform: translateY(-50%); color: var(--ctp-overlay0);"></i>
            <input type="text" id="search-input" placeholder="Search brand, engine, glass, style..." style="width: 100%; background: var(--ctp-crust); border: 1px solid var(--ctp-surface1); border-radius: var(--radius-md); padding: 0.65rem 0.85rem 0.65rem 2.25rem; color: var(--ctp-text); font-family: var(--font-body); font-size: 0.9rem;">
          </div>
        </div>

        <!-- Archetype -->
        <div>
          <label for="archetype-filter" style="display: block; font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-subtext0); margin-bottom: 0.35rem; text-transform: uppercase;">Archetype / Style</label>
          <select id="archetype-filter" style="width: 100%; background: var(--ctp-crust); border: 1px solid var(--ctp-surface1); border-radius: var(--radius-md); padding: 0.65rem 0.85rem; color: var(--ctp-text); font-family: var(--font-body); font-size: 0.9rem;">
            <option value="all">All Archetypes</option>
            <option value="Diver">Diver / Tool Watch</option>
            <option value="Dress">Dress / Clean Dial</option>
            <option value="Field">Field / Flieger</option>
            <option value="GADA">Everyday / GADA</option>
            <option value="Chrono">Chronograph</option>
            <option value="Digital">Digital / Modern Retro</option>
          </select>
        </div>

        <!-- Movement -->
        <div>
          <label for="movement-filter" style="display: block; font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-subtext0); margin-bottom: 0.35rem; text-transform: uppercase;">Movement / Caliber</label>
          <select id="movement-filter" style="width: 100%; background: var(--ctp-crust); border: 1px solid var(--ctp-surface1); border-radius: var(--radius-md); padding: 0.65rem 0.85rem; color: var(--ctp-text); font-family: var(--font-body); font-size: 0.9rem;">
            <option value="all">All Calibers</option>
            <option value="NH35">Seiko NH35 Automatic (21,600 bph)</option>
            <option value="VH31">Seiko VH31 Sweeping Quartz (4 bps)</option>
            <option value="VK63">Seiko VK63 Meca-Quartz Chrono</option>
            <option value="Casio">Casio Quartz Module</option>
            <option value="ST19">Mechanical Manual-Wind</option>
          </select>
        </div>

        <!-- Max L2L filter -->
        <div>
          <div style="display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-subtext0); margin-bottom: 0.35rem; text-transform: uppercase;">
            <span>Max Lug-To-Lug</span>
            <span id="l2l-slider-display" style="color: var(--gold-primary); font-weight: 700;">48.0 mm</span>
          </div>
          <input type="range" id="l2l-filter-slider" min="39.0" max="49.0" step="0.5" value="48.5" style="width: 100%; accent-color: var(--gold-primary); cursor: pointer; height: 8px;">
        </div>
      </div>

      <!-- Price Tiers Switch & Result Count -->
      <div style="margin-top: 1.25rem; padding-top: 1rem; border-top: 1px solid var(--ctp-surface0); display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 1rem;">
        <div style="display: flex; align-items: center; gap: 0.5rem; flex-wrap: wrap;">
          <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-overlay1); text-transform: uppercase; margin-right: 0.25rem;">Pricing Benchmark:</span>
          <button type="button" class="price-tab-btn active btn-tactile" data-mode="choice" style="background: var(--gold-bg); color: var(--gold-primary); border: 1px solid var(--gold-border); padding: 0.35rem 0.75rem; border-radius: var(--radius-sm); font-family: var(--font-mono); font-size: 0.75rem; font-weight: 600;">
            AliExpress Choice (Free Shipping)
          </button>
          <button type="button" class="price-tab-btn btn-tactile" data-mode="singles" style="background: var(--ctp-surface0); color: var(--ctp-subtext0); border: 1px solid var(--ctp-surface1); padding: 0.35rem 0.75rem; border-radius: var(--radius-sm); font-family: var(--font-mono); font-size: 0.75rem; font-weight: 600;">
            11.11 / Choice Day Peak
          </button>
          <button type="button" class="price-tab-btn btn-tactile" data-mode="street" style="background: var(--ctp-surface0); color: var(--ctp-subtext0); border: 1px solid var(--ctp-surface1); padding: 0.35rem 0.75rem; border-radius: var(--radius-sm); font-family: var(--font-mono); font-size: 0.75rem; font-weight: 600;">
            Standard Retail
          </button>
        </div>

        <div style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--ctp-subtext1);">
          Showing <span id="visible-count" style="font-weight: 700; color: #fff;">20</span> of <span id="total-count">20</span> horological picks
        </div>
      </div>
    </section>

    <!-- Watch Grid -->
    <div id="watch-grid" class="watch-grid"></div>
"""
