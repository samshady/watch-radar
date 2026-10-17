# scripts/templates/care_panels.py
# 4 Care & Toolkit panels and clean footer for Watch Radar

CARE_PANELS_HTML = """
    <!-- CARE LAB & TOOLKIT PANELS -->
    <section id="care-lab" style="margin-top: 4rem;">
      <div style="margin-bottom: 2rem;">
        <div style="display: flex; align-items: center; gap: 0.5rem; font-family: var(--font-mono); font-size: 0.75rem; color: var(--gold-primary); text-transform: uppercase; letter-spacing: 0.05em; font-weight: 700;">
          <i class="fa-solid fa-wrench"></i>
          <span>Horologist Workbench &amp; Longevity</span>
        </div>
        <h2 style="font-family: var(--font-display); font-size: 2rem; font-weight: 700; color: #fff; margin-top: 0.25rem;">
          Care, Storage &amp; Toolkit Manual
        </h2>
        <p style="color: var(--ctp-subtext0); font-size: 0.95rem; margin-top: 0.25rem; max-width: 720px;">
          Tested guidance for maintaining budget automatics, sizing bracelets for small wrists without scratching links, and protecting movements from everyday hazards.
        </p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
        <!-- PANEL 1: MOVEMENT CARE -->
        <article class="atelier-card" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
              <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-peach); text-transform: uppercase; font-weight: 700; display: inline-flex; align-items: center; gap: 0.4rem;">
                <i class="fa-solid fa-gear"></i> Caliber Safety
              </span>
              <span style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ctp-overlay1);">Part I</span>
            </div>
            <h3 style="font-family: var(--font-display); font-size: 1.2rem; color: #fff; margin-bottom: 0.75rem;">
              Movement Care &amp; Safety Protocol
            </h3>
            <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.75rem; font-size: 0.85rem; color: var(--ctp-subtext1);">
              <li style="display: flex; gap: 0.6rem; align-items: flex-start;">
                <i class="fa-solid fa-triangle-exclamation" style="color: var(--ctp-red); margin-top: 0.2rem; shrink-0;"></i>
                <div>
                  <strong style="color: #fff;">The Date Change Danger Zone:</strong> Never quickset the date between 21:00 (9 PM) and 03:00 (3 AM) on Seiko NH35 or PT5000 calibers. The date-change gears are actively engaged. Manually advance hands past midnight first.
                </div>
              </li>
              <li style="display: flex; gap: 0.6rem; align-items: flex-start;">
                <i class="fa-solid fa-magnet" style="color: var(--ctp-yellow); margin-top: 0.2rem; shrink-0;"></i>
                <div>
                  <strong style="color: #fff;">Demagnetization in 5 Seconds:</strong> If an automatic suddenly runs 45 seconds fast per day, laptop speakers or iPad smart covers magnetized the hairspring. Test with a compass app, then clear it with an eight euro blue coil demagnetizer.
                </div>
              </li>
              <li style="display: flex; gap: 0.6rem; align-items: flex-start;">
                <i class="fa-solid fa-droplet" style="color: var(--ctp-blue); margin-top: 0.2rem; shrink-0;"></i>
                <div>
                  <strong style="color: #fff;">Water Resistance Reality:</strong> 50m means light surface swimming only. For swimming confidence, choose 100m or 200m watches with a screw-down crown like the Steeldive SD1970.
                </div>
              </li>
            </ul>
          </div>
          <div style="margin-top: 1.25rem; padding-top: 1rem; border-top: 1px solid var(--ctp-surface0); font-family: var(--font-mono); font-size: 0.75rem; color: var(--gold-primary);">
            Rule of thumb: Hand-wind 15 turns to start, never shake violently.
          </div>
        </article>

        <!-- PANEL 2: STORAGE & TRAVEL ROLLS -->
        <article class="atelier-card" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
              <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-green); text-transform: uppercase; font-weight: 700; display: inline-flex; align-items: center; gap: 0.4rem;">
                <i class="fa-solid fa-box-archive"></i> Storage
              </span>
              <span style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ctp-overlay1);">Part II</span>
            </div>
            <h3 style="font-family: var(--font-display); font-size: 1.2rem; color: #fff; margin-bottom: 0.75rem;">
              Small-Wrist Watch Boxes &amp; Rolls
            </h3>
            <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.75rem; font-size: 0.85rem; color: var(--ctp-subtext1);">
              <li style="display: flex; gap: 0.6rem; align-items: flex-start;">
                <i class="fa-solid fa-compress" style="color: var(--ctp-green); margin-top: 0.2rem; shrink-0;"></i>
                <div>
                  <strong style="color: #fff;">The Stiff Cushion Trap:</strong> Standard Chinese watch box pillows measure 18 to 20 cm in circumference. Forcing a bracelet sized for a 16 cm wrist over them stretches clasp springs.
                </div>
              </li>
              <li style="display: flex; gap: 0.6rem; align-items: flex-start;">
                <i class="fa-solid fa-gem" style="color: var(--gold-primary); margin-top: 0.2rem; shrink-0;"></i>
                <div>
                  <strong style="color: #fff;">Slide-Rail M-Cushions:</strong> Look for travel rolls with hexagonal snap rails or M-shaped compressible pillows that compress down to 14.5 cm without strain.
                </div>
              </li>
              <li style="display: flex; gap: 0.6rem; align-items: flex-start;">
                <i class="fa-solid fa-cloud" style="color: var(--ctp-lavender); margin-top: 0.2rem; shrink-0;"></i>
                <div>
                  <strong style="color: #fff;">Moisture Protection:</strong> Keep one dry silica gel packet inside your 3-watch roll. Avoid storing mechanical watches in high-humidity bathrooms.
                </div>
              </li>
            </ul>
          </div>
          <div style="margin-top: 1.25rem; padding-top: 1rem; border-top: 1px solid var(--ctp-surface0); font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-green);">
            Recommended: Hexagonal 3-slot travel roll with slide-in dividers.
          </div>
        </article>

        <!-- PANEL 3: STRAP SWAPPING -->
        <article class="atelier-card" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
              <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-sapphire); text-transform: uppercase; font-weight: 700; display: inline-flex; align-items: center; gap: 0.4rem;">
                <i class="fa-solid fa-link"></i> Customization
              </span>
              <span style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ctp-overlay1);">Part III</span>
            </div>
            <h3 style="font-family: var(--font-display); font-size: 1.2rem; color: #fff; margin-bottom: 0.75rem;">
              Strap Swapping Masterclass
            </h3>
            <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.75rem; font-size: 0.85rem; color: var(--ctp-subtext1);">
              <li style="display: flex; gap: 0.6rem; align-items: flex-start;">
                <i class="fa-solid fa-circle-check" style="color: var(--ctp-sapphire); margin-top: 0.2rem; shrink-0;"></i>
                <div>
                  <strong style="color: #fff;">FKM Waffle &amp; Tropic Rubber:</strong> Standard silicone collects pocket lint. Fluoroelastomer (FKM) rubber is lint-free, chemical resistant, and curves naturally around smaller wrists.
                </div>
              </li>
              <li style="display: flex; gap: 0.6rem; align-items: flex-start;">
                <i class="fa-solid fa-parachute-box" style="color: var(--ctp-mauve); margin-top: 0.2rem; shrink-0;"></i>
                <div>
                  <strong style="color: #fff;">Marine Nationale Parachute Webbing:</strong> Elastic French parachute straps have zero pin holes. They adjust by millimeter increments and sit flat without stiff buckle gaps.
                </div>
              </li>
              <li style="display: flex; gap: 0.6rem; align-items: flex-start;">
                <i class="fa-solid fa-triangle-exclamation" style="color: var(--ctp-yellow); margin-top: 0.2rem; shrink-0;"></i>
                <div>
                  <strong style="color: #fff;">Watch Lug Widths:</strong> 20mm is the universal sweet spot. Watch out for 19mm odd lug widths (like the Escapement Time 35mm) which require dedicated 19mm straps.
                </div>
              </li>
            </ul>
          </div>
          <div style="margin-top: 1.25rem; padding-top: 1rem; border-top: 1px solid var(--ctp-surface0); font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-sapphire);">
            Quick-release spring bars save your lugs from scratches.
          </div>
        </article>

        <!-- PANEL 4: TOOLKIT & SIZING -->
        <article class="atelier-card" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
              <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-maroon); text-transform: uppercase; font-weight: 700; display: inline-flex; align-items: center; gap: 0.4rem;">
                <i class="fa-solid fa-toolbox"></i> Workbench
              </span>
              <span style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ctp-overlay1);">Part IV</span>
            </div>
            <h3 style="font-family: var(--font-display); font-size: 1.2rem; color: #fff; margin-bottom: 0.75rem;">
              Essential Mod &amp; Sizing Kit
            </h3>
            <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.75rem; font-size: 0.85rem; color: var(--ctp-subtext1);">
              <li style="display: flex; gap: 0.6rem; align-items: flex-start;">
                <i class="fa-solid fa-hammer" style="color: var(--ctp-maroon); margin-top: 0.2rem; shrink-0;"></i>
                <div>
                  <strong style="color: #fff;">Pin Punch Block &amp; Brass Hammer:</strong> Do not use cheap plastic twist pushers on stubborn split pins. A slotted plastic holder and brass hammer give clean, controlled link removal.
                </div>
              </li>
              <li style="display: flex; gap: 0.6rem; align-items: flex-start;">
                <i class="fa-solid fa-screwdriver" style="color: var(--gold-primary); margin-top: 0.2rem; shrink-0;"></i>
                <div>
                  <strong style="color: #fff;">Hollow-Ground Screwdrivers:</strong> For San Martin or Pagani screwed links, use 1.2mm or 1.4mm hollow-ground blades. Wedge tips will cam out and mar screw slots.
                </div>
              </li>
              <li style="display: flex; gap: 0.6rem; align-items: flex-start;">
                <i class="fa-solid fa-gem" style="color: var(--ctp-sky); margin-top: 0.2rem; shrink-0;"></i>
                <div>
                  <strong style="color: #fff;">Diamond Selector II Tester:</strong> A ten euro thermal conductivity gem tester confirms genuine sapphire crystal versus mineral glass in two seconds.
                </div>
              </li>
            </ul>
          </div>
          <div style="margin-top: 1.25rem; padding-top: 1rem; border-top: 1px solid var(--ctp-surface0); font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-maroon);">
            Silicon 7000 grease keeps caseback O-rings pliable and waterproof.
          </div>
        </article>
      </div>
    </section>
  </main>

  <footer style="margin-top: 5rem; border-top: 1px solid var(--ctp-surface0); padding: 3rem 0; background: var(--ctp-crust);">
    <div class="container" style="display: flex; flex-direction: column; md:flex-row; justify-content: space-between; align-items: center; gap: 1.5rem; text-align: center; md:text-align: left;">
      <div>
        <div style="display: flex; align-items: center; justify-content: center; md:justify-content: flex-start; gap: 0.5rem; margin-bottom: 0.5rem;">
          <i class="fa-solid fa-stopwatch" style="color: var(--gold-primary);"></i>
          <span style="font-family: var(--font-display); font-weight: 700; color: #fff; font-size: 1.1rem;">Watch Radar</span>
          <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--gold-primary); background: var(--gold-bg); border: 1px solid var(--gold-border); padding: 0.15rem 0.45rem; border-radius: 4px;">Atelier Edition</span>
        </div>
        <p style="color: var(--ctp-subtext0); font-size: 0.85rem; max-width: 600px;">
          Curated guide for budget mechanical and sweeping quartz timepieces. Real dimensions, small-wrist ergonomics, and unbiased value assessments.
        </p>
      </div>

      <div style="display: flex; flex-direction: column; align-items: center; md:align-items: flex-end; gap: 0.5rem;">
        <div style="display: flex; gap: 0.75rem; font-family: var(--font-mono); font-size: 0.8rem;">
          <a href="https://samshady.github.io/watch-radar/" style="color: var(--gold-primary); text-decoration: none;">Watch Radar</a>
          <span style="color: var(--ctp-surface2);">&bull;</span>
          <a href="https://samshady.github.io/iem-radar/" style="color: var(--ctp-subtext1); text-decoration: none;">IEM Radar</a>
          <span style="color: var(--ctp-surface2);">&bull;</span>
          <a href="https://samshady.github.io/retro-handhelds-radar/" style="color: var(--ctp-subtext1); text-decoration: none;">Retro Handhelds</a>
        </div>
        <div style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-overlay1);">
          Handcrafted in the Radar Atelier. 2026.
        </div>
      </div>
    </div>
  </footer>
"""
