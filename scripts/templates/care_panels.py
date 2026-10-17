# scripts/templates/care_panels.py
# Aesthetic, modular Care & Toolkit panels and clean footer for Watch Radar

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
          Bite-sized field rules for maintaining budget calibers, sizing bracelets for small wrists without scratching links, and essential bench tools.
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
              <span style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ctp-overlay1);">Module 01</span>
            </div>
            <h3 style="font-family: var(--font-display); font-size: 1.2rem; color: #fff; margin-bottom: 1rem;">
              Movement Protocol
            </h3>

            <!-- Mini Widgets -->
            <div style="display: flex; flex-direction: column; gap: 0.75rem;">
              <div style="background: var(--ctp-crust); padding: 0.75rem; border-radius: var(--radius-md); border: 1px solid rgba(243, 139, 168, 0.2);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-red); font-weight: 700; text-transform: uppercase; display: flex; align-items: center; gap: 0.3rem;">
                    <i class="fa-solid fa-triangle-exclamation"></i> Danger Zone
                  </span>
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-red); background: rgba(243, 139, 168, 0.1); padding: 0.15rem 0.4rem; border-radius: 4px;">21:00 to 03:00</span>
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  Intermediate date gears are meshed. Never quickset date during these hours. Advance hands past midnight first.
                </div>
              </div>

              <div style="background: var(--ctp-crust); padding: 0.75rem; border-radius: var(--radius-md); border: 1px solid rgba(249, 226, 175, 0.2);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-yellow); font-weight: 700; text-transform: uppercase; display: flex; align-items: center; gap: 0.3rem;">
                    <i class="fa-solid fa-magnet"></i> Magnetism
                  </span>
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-yellow); background: rgba(249, 226, 175, 0.1); padding: 0.15rem 0.4rem; border-radius: 4px;">+45s/day Spike</span>
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  Sudden massive gain signals magnetized hairspring. Test with phone compass app; clear with blue coil demagnetizer.
                </div>
              </div>

              <div style="background: var(--ctp-crust); padding: 0.75rem; border-radius: var(--radius-md); border: 1px solid rgba(137, 180, 250, 0.2);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-blue); font-weight: 700; text-transform: uppercase; display: flex; align-items: center; gap: 0.3rem;">
                    <i class="fa-solid fa-droplet"></i> Water Seal
                  </span>
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-blue); background: rgba(137, 180, 250, 0.1); padding: 0.15rem 0.4rem; border-radius: 4px;">100m+ Screw Crown</span>
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  30m is splash only. For confident lap swimming, choose 100m or 200m ratings with threaded crown.
                </div>
              </div>
            </div>
          </div>
          <div style="margin-top: 1.25rem; padding-top: 0.85rem; border-top: 1px solid var(--ctp-surface0); font-family: var(--font-mono); font-size: 0.75rem; color: var(--gold-primary); display: flex; justify-content: space-between;">
            <span>Initial Wind:</span>
            <span style="font-weight: 700;">15 to 20 gentle turns</span>
          </div>
        </article>

        <!-- PANEL 2: STORAGE & ROLLS -->
        <article class="atelier-card" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
              <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-green); text-transform: uppercase; font-weight: 700; display: inline-flex; align-items: center; gap: 0.4rem;">
                <i class="fa-solid fa-box-archive"></i> Storage
              </span>
              <span style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ctp-overlay1);">Module 02</span>
            </div>
            <h3 style="font-family: var(--font-display); font-size: 1.2rem; color: #fff; margin-bottom: 1rem;">
              Small-Wrist Storage
            </h3>

            <!-- Mini Widgets -->
            <div style="display: flex; flex-direction: column; gap: 0.75rem;">
              <div style="background: var(--ctp-crust); padding: 0.75rem; border-radius: var(--radius-md); border: 1px solid rgba(166, 227, 161, 0.2);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-green); font-weight: 700; text-transform: uppercase; display: flex; align-items: center; gap: 0.3rem;">
                    <i class="fa-solid fa-compress"></i> Cushion Fit
                  </span>
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-green); background: rgba(166, 227, 161, 0.1); padding: 0.15rem 0.4rem; border-radius: 4px;">&le; 15.5 cm Pillows</span>
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  Standard 19cm cushions stretch bracelets sized for 16cm wrists. Pick compressible M-cushions.
                </div>
              </div>

              <div style="background: var(--ctp-crust); padding: 0.75rem; border-radius: var(--radius-md); border: 1px solid rgba(238, 212, 159, 0.2);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--gold-primary); font-weight: 700; text-transform: uppercase; display: flex; align-items: center; gap: 0.3rem;">
                    <i class="fa-solid fa-shield-halved"></i> Slide Rails
                  </span>
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--gold-primary); background: var(--gold-bg); padding: 0.15rem 0.4rem; border-radius: 4px;">Flank Protection</span>
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  Hexagonal travel rolls with grooved partitions stop steel crowns from rubbing adjoining watch flanks.
                </div>
              </div>

              <div style="background: var(--ctp-crust); padding: 0.75rem; border-radius: var(--radius-md); border: 1px solid rgba(180, 190, 254, 0.2);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-lavender); font-weight: 700; text-transform: uppercase; display: flex; align-items: center; gap: 0.3rem;">
                    <i class="fa-solid fa-cloud"></i> Humidity
                  </span>
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-lavender); background: rgba(180, 190, 254, 0.1); padding: 0.15rem 0.4rem; border-radius: 4px;">Silica Gel Pack</span>
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  Add one dry silica sachet per box slot. Keep timepieces out of humid bathroom environments.
                </div>
              </div>
            </div>
          </div>
          <div style="margin-top: 1.25rem; padding-top: 0.85rem; border-top: 1px solid var(--ctp-surface0); font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-green); display: flex; justify-content: space-between;">
            <span>Ideal Format:</span>
            <span style="font-weight: 700;">3-slot hexagonal travel roll</span>
          </div>
        </article>

        <!-- PANEL 3: STRAP SWAPPING -->
        <article class="atelier-card" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
              <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-sapphire); text-transform: uppercase; font-weight: 700; display: inline-flex; align-items: center; gap: 0.4rem;">
                <i class="fa-solid fa-link"></i> Customization
              </span>
              <span style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ctp-overlay1);">Module 03</span>
            </div>
            <h3 style="font-family: var(--font-display); font-size: 1.2rem; color: #fff; margin-bottom: 1rem;">
              Strap Masterclass
            </h3>

            <!-- Mini Widgets -->
            <div style="display: flex; flex-direction: column; gap: 0.75rem;">
              <div style="background: var(--ctp-crust); padding: 0.75rem; border-radius: var(--radius-md); border: 1px solid rgba(116, 199, 236, 0.2);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-sapphire); font-weight: 700; text-transform: uppercase; display: flex; align-items: center; gap: 0.3rem;">
                    <i class="fa-solid fa-water"></i> FKM Waffle
                  </span>
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-sapphire); background: rgba(116, 199, 236, 0.1); padding: 0.15rem 0.4rem; border-radius: 4px;">Zero Lint</span>
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  Fluoroelastomer rubber curves smoothly over small wrists without silicone lint accumulation.
                </div>
              </div>

              <div style="background: var(--ctp-crust); padding: 0.75rem; border-radius: var(--radius-md); border: 1px solid rgba(203, 166, 247, 0.2);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-mauve); font-weight: 700; text-transform: uppercase; display: flex; align-items: center; gap: 0.3rem;">
                    <i class="fa-solid fa-parachute-box"></i> Parachute
                  </span>
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-mauve); background: rgba(203, 166, 247, 0.1); padding: 0.15rem 0.4rem; border-radius: 4px;">Infinite Micro-Fit</span>
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  Marine Nationale elastic webbing has zero punched holes. Sits flush without stiff buckle gaps.
                </div>
              </div>

              <div style="background: var(--ctp-crust); padding: 0.75rem; border-radius: var(--radius-md); border: 1px solid rgba(249, 226, 175, 0.2);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-yellow); font-weight: 700; text-transform: uppercase; display: flex; align-items: center; gap: 0.3rem;">
                    <i class="fa-solid fa-circle-exclamation"></i> Odd Lug Width
                  </span>
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-yellow); background: rgba(249, 226, 175, 0.1); padding: 0.15rem 0.4rem; border-radius: 4px;">19mm Check</span>
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  Escapement Time 35mm uses 19mm lugs. Forcing 20mm leather scuffs edges; order true 19mm straps.
                </div>
              </div>
            </div>
          </div>
          <div style="margin-top: 1.25rem; padding-top: 0.85rem; border-top: 1px solid var(--ctp-surface0); font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-sapphire); display: flex; justify-content: space-between;">
            <span>Hardware Tip:</span>
            <span style="font-weight: 700;">Use quick-release spring bars</span>
          </div>
        </article>

        <!-- PANEL 4: TOOLKIT & SIZING -->
        <article class="atelier-card" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
              <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-maroon); text-transform: uppercase; font-weight: 700; display: inline-flex; align-items: center; gap: 0.4rem;">
                <i class="fa-solid fa-toolbox"></i> Workbench
              </span>
              <span style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ctp-overlay1);">Module 04</span>
            </div>
            <h3 style="font-family: var(--font-display); font-size: 1.2rem; color: #fff; margin-bottom: 1rem;">
              Mod &amp; Sizing Kit
            </h3>

            <!-- Mini Widgets -->
            <div style="display: flex; flex-direction: column; gap: 0.75rem;">
              <div style="background: var(--ctp-crust); padding: 0.75rem; border-radius: var(--radius-md); border: 1px solid rgba(235, 160, 172, 0.2);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-maroon); font-weight: 700; text-transform: uppercase; display: flex; align-items: center; gap: 0.3rem;">
                    <i class="fa-solid fa-hammer"></i> Pin Removal
                  </span>
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-maroon); background: rgba(235, 160, 172, 0.1); padding: 0.15rem 0.4rem; border-radius: 4px;">Brass Mallet</span>
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  Use a slotted block and brass mallet along stamped link arrows. Twist pushers bend easily.
                </div>
              </div>

              <div style="background: var(--ctp-crust); padding: 0.75rem; border-radius: var(--radius-md); border: 1px solid rgba(238, 212, 159, 0.2);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--gold-primary); font-weight: 700; text-transform: uppercase; display: flex; align-items: center; gap: 0.3rem;">
                    <i class="fa-solid fa-screwdriver"></i> Screwed Links
                  </span>
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--gold-primary); background: var(--gold-bg); padding: 0.15rem 0.4rem; border-radius: 4px;">1.2mm Hollow-Ground</span>
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  Parallel ground blades grip full slot walls. Standard wedge tips cam out and scratch link flanks.
                </div>
              </div>

              <div style="background: var(--ctp-crust); padding: 0.75rem; border-radius: var(--radius-md); border: 1px solid rgba(137, 220, 235, 0.2);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-sky); font-weight: 700; text-transform: uppercase; display: flex; align-items: center; gap: 0.3rem;">
                    <i class="fa-solid fa-gem"></i> Sapphire Check
                  </span>
                  <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--ctp-sky); background: rgba(137, 220, 235, 0.1); padding: 0.15rem 0.4rem; border-radius: 4px;">Diamond Selector II</span>
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  Thermal conductivity probe confirms genuine corundum sapphire crystal versus mineral glass in 2 seconds.
                </div>
              </div>
            </div>
          </div>
          <div style="margin-top: 1.25rem; padding-top: 0.85rem; border-top: 1px solid var(--ctp-surface0); font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-maroon); display: flex; justify-content: space-between;">
            <span>Gasket Care:</span>
            <span style="font-weight: 700;">Silicon 7000 grease</span>
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
