# scripts/templates/nav_header.py
# Top ecosystem navigation, header, escapement beat simulator, caliper lab, and filter controls

NAV_HEADER_HTML = """
  <!-- Top Ecosystem Cross-Nav Bar -->
  <div class="radar-ecosystem-bar">
    <div class="ecosystem-container">
      <div class="ecosystem-brand">
        <span class="pulse-dot"></span>
        <strong style="color: var(--gold-primary); letter-spacing: 0.05em;">RADAR ECOSYSTEM</strong>
        <span style="color: var(--ctp-overlay0);" class="sm-hidden">|</span>
        <span style="color: var(--ctp-subtext0);" class="sm-hidden">Curated enthusiast guides for budget gems</span>
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

  <header style="background: linear-gradient(180deg, var(--ctp-mantle) 0%, var(--ctp-base) 100%); border-bottom: 1px solid var(--ctp-surface0); padding: 2.25rem 0 1.75rem;" class="cotes-de-geneve">
    <div class="container">
      <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 1.25rem; align-items: flex-start;">
        <div>
          <div style="display: inline-flex; align-items: center; gap: 0.5rem; background: var(--gold-bg); border: 1px solid var(--gold-border); padding: 0.3rem 0.75rem; border-radius: 9999px; margin-bottom: 0.75rem;">
            <i class="fa-solid fa-compass-drafting" style="color: var(--gold-primary); font-size: 0.8rem;"></i>
            <span style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 600; color: var(--gold-primary); letter-spacing: 0.06em; text-transform: uppercase;">Horological Atelier Edition</span>
          </div>
          <h1 style="font-family: var(--font-display); font-size: clamp(2rem, 5vw, 2.75rem); font-weight: 800; color: #fff; letter-spacing: -0.03em; line-height: 1.15; margin-bottom: 0.5rem;">
            Watch Radar <span style="font-weight: 400; color: var(--gold-primary); font-size: 0.7em;">2026</span>
          </h1>
          <p style="color: var(--ctp-subtext1); font-size: 1.05rem; max-width: 720px; line-height: 1.6;">
            Curated budget horology guide strictly under &euro;80. Real micrometer lug-to-lug specs, Seiko NH35 vs VH31 sweeping quartz comparisons, and ergonomic small-wrist verdicts.
          </p>
        </div>

        <!-- Quick actions with strict >=44px mobile touch targets -->
        <div style="display: flex; flex-wrap: wrap; gap: 0.6rem; align-items: center; width: 100%;">
          <a href="#escapement-lab" class="btn-tactile" style="display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; background: var(--ctp-surface0); color: var(--gold-primary); border: 1px solid var(--gold-border); padding: 0.6rem 1rem; border-radius: var(--radius-md); font-family: var(--font-mono); font-size: 0.825rem; font-weight: 600; text-decoration: none; min-height: 44px; box-sizing: border-box;">
            <i class="fa-solid fa-gear"></i>
            <span>Beat Rate Lab</span>
          </a>
          <a href="#caliper-lab" class="btn-tactile" style="display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; background: var(--gold-bg); color: var(--gold-primary); border: 1px solid var(--gold-border); padding: 0.6rem 1rem; border-radius: var(--radius-md); font-family: var(--font-mono); font-size: 0.825rem; font-weight: 600; text-decoration: none; min-height: 44px; box-sizing: border-box;">
            <i class="fa-solid fa-ruler-horizontal"></i>
            <span>Caliper Lab</span>
          </a>
          <a href="#care-lab" class="btn-tactile" style="display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; background: var(--ctp-surface0); color: var(--ctp-text); border: 1px solid var(--ctp-surface1); padding: 0.6rem 1rem; border-radius: var(--radius-md); font-family: var(--font-mono); font-size: 0.825rem; font-weight: 600; text-decoration: none; min-height: 44px; box-sizing: border-box;">
            <i class="fa-solid fa-screwdriver-wrench" style="color: var(--ctp-teal);"></i>
            <span>Care &amp; Workbench</span>
          </a>
        </div>
      </div>
    </div>
  </header>

  <main class="container" style="margin-top: 2rem;">

    <!-- ESCAPEMENT & BEAT RATE SIMULATOR (UNIQUE WATCH ANIMATION) -->
    <section id="escapement-lab" class="atelier-card" style="margin-bottom: 2rem; border-color: var(--gold-border); background: linear-gradient(135deg, rgba(238, 212, 159, 0.05) 0%, var(--ctp-mantle) 100%);">
      <div style="display: flex; flex-direction: column; lg:flex-row; justify-content: space-between; gap: 2rem; align-items: center;">
        <div style="flex: 1; width: 100%;">
          <div style="display: flex; align-items: center; gap: 0.5rem; font-family: var(--font-mono); font-size: 0.75rem; color: var(--gold-primary); text-transform: uppercase; letter-spacing: 0.06em; font-weight: 700;">
            <i class="fa-solid fa-gear fa-spin" style="animation-duration: 8s;"></i>
            <span>Escapement &amp; Beat Rate Laboratory</span>
          </div>
          <h2 style="font-family: var(--font-display); font-size: clamp(1.35rem, 3vw, 1.75rem); font-weight: 700; color: #fff; margin-top: 0.25rem;">
            Mechanical Sweep vs Quartz Cadence
          </h2>
          <p style="color: var(--ctp-subtext0); font-size: 0.9rem; margin-top: 0.35rem; line-height: 1.55; max-width: 640px;">
            The soul of a timepiece lives in its balance spring oscillation. Tap calibers below to see the second hand cadence change live on the railway dial.
          </p>

          <!-- Caliber Selector Pills -->
          <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1.25rem;" id="escapement-selector">
            <button type="button" class="escapement-btn active btn-tactile" data-bph="21600" data-hz="3" data-bps="6" data-name="Seiko NH35 Automatic" data-desc="Seiko NH35/NH36 mechanical automatic. 21,600 vibrations per hour (3 Hz). 6 visual steps each second with robust balance wheel oscillation.">
              <span style="font-weight: 700; color: #fff; font-size: 0.85rem;">Seiko NH35</span>
              <span style="font-size: 0.7rem; color: var(--gold-primary);">21,600 bph / 6 bps</span>
            </button>
            <button type="button" class="escapement-btn btn-tactile" data-bph="28800" data-hz="4" data-bps="8" data-name="PT5000 / ETA 2824 Clone" data-desc="PT5000 high-beat automatic. 28,800 vibrations per hour (4 Hz). 8 visual steps each second producing a silky luxury sweep.">
              <span style="font-weight: 700; color: #fff; font-size: 0.85rem;">PT5000 Hi-Beat</span>
              <span style="font-size: 0.7rem; color: var(--ctp-subtext0);">28,800 bph / 8 bps</span>
            </button>
            <button type="button" class="escapement-btn btn-tactile" data-bph="14400" data-hz="2" data-bps="4" data-name="Seiko VH31 Sweeping Quartz" data-desc="Seiko VH31 sweeping quartz. 14,400 vibrations per hour. 4 micro-ticks each second creating the illusion of a vintage mechanical engine with quartz precision.">
              <span style="font-weight: 700; color: #fff; font-size: 0.85rem;">Seiko VH31</span>
              <span style="font-size: 0.7rem; color: var(--ctp-subtext0);">14,400 bph / 4 bps</span>
            </button>
            <button type="button" class="escapement-btn btn-tactile" data-bph="3600" data-hz="1" data-bps="1" data-name="Casio Quartz Module" data-desc="Casio quartz module. 3,600 vibrations per hour (1 Hz). Single deadbeat stepping second for extreme shock tolerance and 10-year battery endurance.">
              <span style="font-weight: 700; color: #fff; font-size: 0.85rem;">Casio 1 Hz</span>
              <span style="font-size: 0.7rem; color: var(--ctp-subtext0);">3,600 bph / 1 bps</span>
            </button>
          </div>

          <div id="escapement-info" style="margin-top: 1rem; padding: 0.75rem 1rem; background: var(--ctp-crust); border-radius: var(--radius-md); border-left: 3px solid var(--gold-primary); font-family: var(--font-body); font-size: 0.85rem; color: var(--ctp-subtext1); line-height: 1.45;">
            Seiko NH35/NH36 mechanical automatic. 21,600 vibrations per hour (3 Hz). 6 visual steps each second with robust balance wheel oscillation.
          </div>
        </div>

        <!-- Live Animated Escapement Railway Dial -->
        <div style="flex-shrink: 0; width: 210px; height: 210px; position: relative; display: flex; align-items: center; justify-content: center; background: radial-gradient(circle, var(--ctp-crust) 60%, var(--ctp-mantle) 100%); border-radius: 50%; border: 3px solid var(--gold-primary); box-shadow: 0 0 24px rgba(0,0,0,0.6), inset 0 0 16px rgba(238, 212, 159, 0.12);">
          <!-- Chemin de fer railway minute ring -->
          <svg viewBox="0 0 200 200" style="position: absolute; width: 100%; height: 100%; pointer-events: none;">
            <circle cx="100" cy="100" r="92" fill="none" stroke="var(--gold-border)" stroke-width="1.5" />
            <circle cx="100" cy="100" r="82" fill="none" stroke="var(--gold-border)" stroke-width="1.5" />
            <circle cx="100" cy="100" r="87" stroke="var(--ctp-surface2)" stroke-width="8" stroke-dasharray="1.5 7.6" fill="none"/>
            <!-- 12, 3, 6, 9 markers -->
            <line x1="100" y1="8" x2="100" y2="18" stroke="var(--gold-primary)" stroke-width="2.5" />
            <line x1="192" y1="100" x2="182" y2="100" stroke="var(--gold-primary)" stroke-width="2.5" />
            <line x1="100" y1="192" x2="100" y2="182" stroke="var(--gold-primary)" stroke-width="2.5" />
            <line x1="8" y1="100" x2="18" y2="100" stroke="var(--gold-primary)" stroke-width="2.5" />
          </svg>

          <!-- Escapement Balance Wheel Hairspring (Rotates with beat frequency) -->
          <div id="balance-wheel-anim" style="position: absolute; width: 110px; height: 110px; border-radius: 50%; border: 2px dashed rgba(238, 212, 159, 0.35); pointer-events: none; opacity: 0.7;"></div>

          <!-- Center Sweeping Hand -->
          <div id="escapement-hand-pivot" style="position: absolute; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; transform: rotate(0deg); pointer-events: none;">
            <div id="escapement-hand" style="position: absolute; bottom: 50%; left: calc(50% - 1.5px); width: 3px; height: 80px; background: #f38ba8; transform-origin: bottom center; border-radius: 2px; box-shadow: 0 0 8px rgba(243, 139, 168, 0.7);">
              <div style="position: absolute; top: -5px; left: -3.5px; width: 10px; height: 10px; border-radius: 50%; background: #f38ba8;"></div>
            </div>
          </div>

          <!-- Center Ruby Jewel Cap -->
          <div style="position: relative; width: 16px; height: 16px; border-radius: 50%; background: #f38ba8; border: 2px solid #fff; box-shadow: 0 0 10px rgba(243, 139, 168, 0.8); z-index: 2;"></div>
          
          <!-- Cadence Badge -->
          <div id="cadence-readout" style="position: absolute; bottom: 18px; font-family: var(--font-mono); font-size: 0.7rem; font-weight: 700; color: var(--gold-primary); background: rgba(17, 17, 27, 0.9); padding: 0.2rem 0.55rem; border-radius: 4px; border: 1px solid var(--gold-border); letter-spacing: 0.05em; z-index: 3;">
            6 TICKS / SEC
          </div>
        </div>
      </div>
    </section>

    <div class="chemin-de-fer"></div>

    <!-- Digital Caliper L2L Simulator Section -->
    <section id="caliper-lab" class="atelier-card" style="margin-bottom: 2rem; border-color: var(--gold-border); background: linear-gradient(135deg, rgba(238, 212, 159, 0.04) 0%, var(--ctp-mantle) 100%);">
      <div style="display: flex; flex-direction: column; lg:flex-row; justify-content: space-between; gap: 1.5rem; margin-bottom: 1.25rem;">
        <div>
          <div style="display: flex; align-items: center; gap: 0.5rem; font-family: var(--font-mono); font-size: 0.75rem; color: var(--gold-primary); text-transform: uppercase; letter-spacing: 0.06em; font-weight: 700;">
            <i class="fa-solid fa-ruler-combined"></i>
            <span>Vernier Caliper Simulator: Anatomical Fit</span>
          </div>
          <h2 style="font-family: var(--font-display); font-size: clamp(1.35rem, 3vw, 1.65rem); font-weight: 700; color: #fff; margin-top: 0.25rem;">
            Lug-To-Lug vs Flat Wrist Span
          </h2>
          <p style="color: var(--ctp-subtext0); font-size: 0.9rem; margin-top: 0.25rem; max-width: 650px; line-height: 1.5;">
            Case diameter is a vanity metric. What decides whether a watch sits flush or overhangs on a 15 to 17 cm wrist is the lug-to-lug span compared to your flat bone width.
          </p>
        </div>

        <!-- Metric Display Card: Mobile Responsive -->
        <div style="background: var(--ctp-surface0); padding: 0.85rem 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--ctp-surface1); display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; align-items: center; min-width: 260px;">
          <div>
            <div style="font-size: 0.7rem; font-family: var(--font-mono); color: var(--ctp-overlay1); text-transform: uppercase;">Selected Wrist</div>
            <div id="wrist-circumference-display" style="font-family: var(--font-display); font-size: 1.35rem; font-weight: 700; color: var(--gold-primary);">16.5 cm / 6.5"</div>
          </div>
          <div style="border-left: 1px solid var(--ctp-surface2); padding-left: 1rem;">
            <div style="font-size: 0.7rem; font-family: var(--font-mono); color: var(--ctp-overlay1); text-transform: uppercase;">Flat Top Span</div>
            <div id="flat-span-display" style="font-family: var(--font-mono); font-size: 1.35rem; font-weight: 700; color: var(--ctp-green);">47.0 mm</div>
          </div>
        </div>
      </div>

      <!-- Slider Control with Vernier Graduations -->
      <div style="background: var(--ctp-crust); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--ctp-surface0);">
        <div style="display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-subtext0); margin-bottom: 0.5rem;">
          <span>14.5 cm (5.7" slender)</span>
          <span style="color: var(--gold-primary); font-weight: 600;">Drag slider to measure your wrist</span>
          <span>19.0 cm (7.5" broad)</span>
        </div>
        <input type="range" id="wrist-slider" min="14.5" max="19.0" step="0.25" value="16.5" style="width: 100%; accent-color: var(--gold-primary); cursor: pointer; height: 10px;">
        <div class="vernier-scale"></div>
        
        <div style="margin-top: 1rem; display: flex; flex-wrap: wrap; gap: 0.6rem; font-size: 0.8rem; font-family: var(--font-mono);">
          <span style="display: inline-flex; align-items: center; gap: 0.4rem; color: var(--ctp-green); background: rgba(166, 227, 161, 0.1); padding: 0.35rem 0.65rem; border-radius: 4px;">
            <i class="fa-solid fa-circle-check"></i> &lt; 45.0 mm: Tailored Zero Overhang
          </span>
          <span style="display: inline-flex; align-items: center; gap: 0.4rem; color: var(--ctp-yellow); background: rgba(249, 226, 175, 0.1); padding: 0.35rem 0.65rem; border-radius: 4px;">
            <i class="fa-solid fa-circle-exclamation"></i> 45.0 to 47.5 mm: Borderline Flush
          </span>
          <span style="display: inline-flex; align-items: center; gap: 0.4rem; color: var(--ctp-red); background: rgba(243, 139, 168, 0.1); padding: 0.35rem 0.65rem; border-radius: 4px;">
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
            <input type="text" id="search-input" placeholder="Search brand, engine, glass, style..." style="width: 100%; min-height: 44px; background: var(--ctp-crust); border: 1px solid var(--ctp-surface1); border-radius: var(--radius-md); padding: 0.65rem 0.85rem 0.65rem 2.25rem; color: var(--ctp-text); font-family: var(--font-body); font-size: 0.9rem; box-sizing: border-box;">
          </div>
        </div>

        <!-- Archetype -->
        <div>
          <label for="archetype-filter" style="display: block; font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-subtext0); margin-bottom: 0.35rem; text-transform: uppercase;">Archetype / Style</label>
          <select id="archetype-filter" style="width: 100%; min-height: 44px; background: var(--ctp-crust); border: 1px solid var(--ctp-surface1); border-radius: var(--radius-md); padding: 0.65rem 0.85rem; color: var(--ctp-text); font-family: var(--font-body); font-size: 0.9rem; box-sizing: border-box;">
            <option value="all">All Archetypes</option>
            <option value="Diver">Diver / Tool Watch</option>
            <option value="Dress">Dress / Clean Dial</option>
            <option value="Aviation">Aviation / Pilot</option>
            <option value="Field">Field / Explorer</option>
            <option value="GADA">Everyday / GADA</option>
            <option value="Chrono">Chronograph</option>
            <option value="Digital">Digital / Modern Retro</option>
          </select>
        </div>

        <!-- Movement -->
        <div>
          <label for="movement-filter" style="display: block; font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-subtext0); margin-bottom: 0.35rem; text-transform: uppercase;">Movement / Caliber</label>
          <select id="movement-filter" style="width: 100%; min-height: 44px; background: var(--ctp-crust); border: 1px solid var(--ctp-surface1); border-radius: var(--radius-md); padding: 0.65rem 0.85rem; color: var(--ctp-text); font-family: var(--font-body); font-size: 0.9rem; box-sizing: border-box;">
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
            <span id="l2l-slider-display" style="color: var(--gold-primary); font-weight: 700;">49.5 mm</span>
          </div>
          <input type="range" id="l2l-filter-slider" min="38.0" max="50.0" step="0.5" value="49.5" style="width: 100%; accent-color: var(--gold-primary); cursor: pointer; height: 10px;">
          <div class="vernier-scale"></div>
        </div>
      </div>

      <!-- Price Tiers Switch, Lume Darkroom Switch & Result Count -->
      <div style="margin-top: 1.25rem; padding-top: 1rem; border-top: 1px solid var(--ctp-surface0); display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 1rem;">
        <div style="display: flex; align-items: center; gap: 0.5rem; flex-wrap: wrap;">
          <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-overlay1); text-transform: uppercase; margin-right: 0.25rem;">Pricing Benchmark:</span>
          <button type="button" class="price-tab-btn active btn-tactile" data-mode="choice" style="background: var(--gold-bg); color: var(--gold-primary); border: 1px solid var(--gold-border); border-radius: var(--radius-sm); font-family: var(--font-mono); font-size: 0.75rem; font-weight: 600;">
            AliExpress Choice (Free Shipping)
          </button>
          <button type="button" class="price-tab-btn btn-tactile" data-mode="singles" style="background: var(--ctp-surface0); color: var(--ctp-subtext0); border: 1px solid var(--ctp-surface1); border-radius: var(--radius-sm); font-family: var(--font-mono); font-size: 0.75rem; font-weight: 600;">
            11.11 / Choice Day Peak
          </button>
          <button type="button" class="price-tab-btn btn-tactile" data-mode="street" style="background: var(--ctp-surface0); color: var(--ctp-subtext0); border: 1px solid var(--ctp-surface1); border-radius: var(--radius-sm); font-family: var(--font-mono); font-size: 0.75rem; font-weight: 600;">
            Standard Retail
          </button>
        </div>

        <div style="display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap;">
          <!-- Prominent Filter-Bar Lume Darkroom Toggle Button -->
          <button id="lume-toggle-btn" class="btn-tactile lume-filter-btn" type="button" aria-label="Toggle Lume Darkroom Mode" style="display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; background: var(--ctp-surface0); color: var(--ctp-text); border: 1px solid var(--ctp-surface1); padding: 0.55rem 0.95rem; border-radius: var(--radius-sm); font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700;">
            <i class="fa-solid fa-moon" style="color: var(--lume-bgw9);"></i>
            <span id="lume-btn-text">Lume Darkroom: OFF</span>
          </button>

          <div style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--ctp-subtext1);">
            Showing <span id="visible-count" style="font-weight: 700; color: #fff;">25</span> of <span id="total-count">25</span> horological picks
          </div>
        </div>
      </div>
    </section>

    <!-- Watch Grid -->
    <div id="watch-grid" class="watch-grid"></div>

    <!-- Floating Action Dock: Quick Lume Darkroom & Back to Top -->
    <aside class="floating-dock" id="floating-dock" aria-label="Quick Navigation and View Controls">
      <button id="dock-lume-btn" class="dock-action-btn dock-lume-btn btn-tactile" type="button" aria-label="Toggle Lume Darkroom Mode" title="Toggle Lume Darkroom Mode">
        <i class="fa-solid fa-moon" style="color: var(--lume-bgw9);"></i>
        <span id="dock-lume-text">Lume Mode</span>
      </button>
      <button id="back-to-top-btn" class="dock-action-btn btn-tactile" type="button" aria-label="Scroll back to top" title="Scroll back to top">
        <i class="fa-solid fa-arrow-up" style="color: var(--gold-primary);"></i>
        <span>Top</span>
      </button>
    </aside>
"""
