# scripts/templates/care_panels.py
# Aesthetic, modular Care & Workbench panels and clean atelier footer for Watch Radar

CARE_PANELS_HTML = """
    <!-- HOROLOGIST WORKBENCH & LONGEVITY PANELS -->
    <div class="chemin-de-fer"></div>

    <section id="care-lab" style="margin-top: 3.5rem;">
      <div style="margin-bottom: 2rem;">
        <div style="display: flex; align-items: center; gap: 0.5rem; font-family: var(--font-mono); font-size: 0.75rem; color: var(--gold-primary); text-transform: uppercase; letter-spacing: 0.06em; font-weight: 700;">
          <i class="fa-solid fa-wrench"></i>
          <span>Horologist Workbench &amp; Atelier Manual</span>
        </div>
        <h2 style="font-family: var(--font-display); font-size: clamp(1.5rem, 3.5vw, 2.15rem); font-weight: 700; color: #fff; margin-top: 0.25rem;">
          Care, Storage &amp; Bench Toolkit
        </h2>
        <p style="color: var(--ctp-subtext0); font-size: 0.95rem; margin-top: 0.25rem; max-width: 720px; line-height: 1.55;">
          Field rules for maintaining budget automatic and sweeping quartz calibers, sizing solid links for small wrists without scratching flanks, and essential bench tools.
        </p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
        
        <!-- PANEL 1: ATELIER RÉGULATION -->
        <article class="atelier-card" style="display: flex; flex-direction: column; justify-content: space-between; border-color: rgba(238, 212, 159, 0.2);">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.85rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--ctp-surface0);">
              <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--gold-primary); text-transform: uppercase; font-weight: 700; display: inline-flex; align-items: center; gap: 0.4rem;">
                <i class="fa-solid fa-gear"></i> Atelier Régulation
              </span>
              <span style="font-size: 0.7rem; font-family: var(--font-mono); color: var(--ctp-overlay1); background: var(--ctp-crust); padding: 0.15rem 0.45rem; border-radius: 4px;">Caliber Protocol</span>
            </div>
            <h3 style="font-family: var(--font-display); font-size: 1.25rem; color: #fff; margin-bottom: 0.85rem;">
              Movement &amp; Gear Meshing
            </h3>

            <!-- Distinct Dial Widget: Date Change Danger Zone -->
            <div style="background: var(--ctp-crust); padding: 0.85rem; border-radius: var(--radius-md); border-left: 3px solid var(--ctp-red); margin-bottom: 0.75rem;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-red); font-weight: 700; text-transform: uppercase; display: flex; align-items: center; gap: 0.35rem;">
                  <i class="fa-solid fa-triangle-exclamation"></i> Danger Zone (21:00 to 03:00)
                </span>
              </div>
              <div style="font-size: 0.825rem; color: var(--ctp-subtext1); line-height: 1.45;">
                In Seiko NH35 and mechanical movements, the plastic calendar driving wheel engages the date ring between 9 PM and 3 AM. Quicksetting during this window shears gears. Always advance hands past 4 AM before setting the calendar.
              </div>
            </div>

            <!-- Magnetism & Water Seal -->
            <div style="display: flex; flex-direction: column; gap: 0.6rem;">
              <div style="background: rgba(249, 226, 175, 0.05); padding: 0.75rem; border-radius: var(--radius-sm); border: 1px solid rgba(249, 226, 175, 0.15);">
                <div style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; color: var(--ctp-yellow); margin-bottom: 0.2rem;">
                  <i class="fa-solid fa-magnet"></i> Magnetism Spike (+45s/day)
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  Sudden large time gain signals magnetized balance coils sticking together. Rest next to phone compass to test; clear with a blue coil demagnetizer in 3 seconds.
                </div>
              </div>

              <div style="background: rgba(137, 180, 250, 0.05); padding: 0.75rem; border-radius: var(--radius-sm); border: 1px solid rgba(137, 180, 250, 0.15);">
                <div style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; color: var(--ctp-blue); margin-bottom: 0.2rem;">
                  <i class="fa-solid fa-droplet"></i> Gasket Care &amp; Threaded Crown
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  Ensure screw crowns catch threads cleanly without cross-threading. Coat caseback O-rings with Silicon 7000 grease annually for true 200m diver seal.
                </div>
              </div>
            </div>
          </div>

          <div style="margin-top: 1.25rem; padding-top: 0.85rem; border-top: 1px solid var(--ctp-surface0); font-family: var(--font-mono); font-size: 0.75rem; color: var(--gold-primary); display: flex; justify-content: space-between;">
            <span>Initial Manual Wind:</span>
            <span style="font-weight: 700;">15 to 20 gentle turns</span>
          </div>
        </article>

        <!-- PANEL 2: ÉCRIN & STORAGE -->
        <article class="atelier-card" style="display: flex; flex-direction: column; justify-content: space-between; border-color: rgba(166, 227, 161, 0.2);">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.85rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--ctp-surface0);">
              <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-green); text-transform: uppercase; font-weight: 700; display: inline-flex; align-items: center; gap: 0.4rem;">
                <i class="fa-solid fa-box-archive"></i> Écrin &amp; Preservation
              </span>
              <span style="font-size: 0.7rem; font-family: var(--font-mono); color: var(--ctp-overlay1); background: var(--ctp-crust); padding: 0.15rem 0.45rem; border-radius: 4px;">Small-Wrist Storage</span>
            </div>
            <h3 style="font-family: var(--font-display); font-size: 1.25rem; color: #fff; margin-bottom: 0.85rem;">
              Cushion Geometry &amp; Rolls
            </h3>

            <div style="background: var(--ctp-crust); padding: 0.85rem; border-radius: var(--radius-md); border-left: 3px solid var(--ctp-green); margin-bottom: 0.75rem;">
              <div style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-green); font-weight: 700; text-transform: uppercase; margin-bottom: 0.25rem;">
                <i class="fa-solid fa-compress"></i> The 16 cm Cushion Problem
              </div>
              <div style="font-size: 0.825rem; color: var(--ctp-subtext1); line-height: 1.45;">
                Standard watch boxes come with stiff 19 cm pillows. Forcing bracelets sized for 15 to 16.5 cm wrists over them bends clasp hinges and strains spring bars. Choose compressible memory foam cushions or M-shaped flexible inserts.
              </div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 0.6rem;">
              <div style="background: rgba(238, 212, 159, 0.05); padding: 0.75rem; border-radius: var(--radius-sm); border: 1px solid rgba(238, 212, 159, 0.15);">
                <div style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; color: var(--gold-primary); margin-bottom: 0.2rem;">
                  <i class="fa-solid fa-shield-halved"></i> Hexagonal Slide Rails
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  Travel rolls with individual grooved partitions stop steel crowns from rubbing against adjoining case flanks during commute or luggage transit.
                </div>
              </div>

              <div style="background: rgba(180, 190, 254, 0.05); padding: 0.75rem; border-radius: var(--radius-sm); border: 1px solid rgba(180, 190, 254, 0.15);">
                <div style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; color: var(--ctp-lavender); margin-bottom: 0.2rem;">
                  <i class="fa-solid fa-cloud"></i> Silica Protection
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  Place a reusable food-grade silica gel sachet inside your box drawer. Never store luxury or vintage timepieces in high-humidity bathrooms.
                </div>
              </div>
            </div>
          </div>

          <div style="margin-top: 1.25rem; padding-top: 0.85rem; border-top: 1px solid var(--ctp-surface0); font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-green); display: flex; justify-content: space-between;">
            <span>Recommended Carrier:</span>
            <span style="font-weight: 700;">3-slot individual rail roll</span>
          </div>
        </article>

        <!-- PANEL 3: HABILLAGE & ERGONOMIE -->
        <article class="atelier-card" style="display: flex; flex-direction: column; justify-content: space-between; border-color: rgba(116, 199, 236, 0.2);">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.85rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--ctp-surface0);">
              <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-sapphire); text-transform: uppercase; font-weight: 700; display: inline-flex; align-items: center; gap: 0.4rem;">
                <i class="fa-solid fa-link"></i> Habillage &amp; Ergonomie
              </span>
              <span style="font-size: 0.7rem; font-family: var(--font-mono); color: var(--ctp-overlay1); background: var(--ctp-crust); padding: 0.15rem 0.45rem; border-radius: 4px;">Strap Architecture</span>
            </div>
            <h3 style="font-family: var(--font-display); font-size: 1.25rem; color: #fff; margin-bottom: 0.85rem;">
              Strap Taper &amp; Female Endlinks
            </h3>

            <div style="background: var(--ctp-crust); padding: 0.85rem; border-radius: var(--radius-md); border-left: 3px solid var(--ctp-sapphire); margin-bottom: 0.75rem;">
              <div style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-sapphire); font-weight: 700; text-transform: uppercase; margin-bottom: 0.25rem;">
                <i class="fa-solid fa-bezier-curve"></i> Male vs Female Endlink Geometry
              </div>
              <div style="font-size: 0.825rem; color: var(--ctp-subtext1); line-height: 1.45;">
                Male endlinks have center pins protruding past the lugs, adding 3 to 5 mm of rigid span. Female endlinks let bracelet links pivot straight downward at 90 degrees, allowing a 47 mm case to wear like a tailored 43 mm piece on small wrists.
              </div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 0.6rem;">
              <div style="background: rgba(116, 199, 236, 0.05); padding: 0.75rem; border-radius: var(--radius-sm); border: 1px solid rgba(116, 199, 236, 0.15);">
                <div style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; color: var(--ctp-sapphire); margin-bottom: 0.2rem;">
                  <i class="fa-solid fa-water"></i> FKM Fluororubber vs Silicone
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  Cheap silicone picks up lint and sticks to skin. High-density FKM fluororubber drapes softly, resists seawater and UV, and wipes spotless instantly.
                </div>
              </div>

              <div style="background: rgba(203, 166, 247, 0.05); padding: 0.75rem; border-radius: var(--radius-sm); border: 1px solid rgba(203, 166, 247, 0.15);">
                <div style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; color: var(--ctp-mauve); margin-bottom: 0.2rem;">
                  <i class="fa-solid fa-ruler"></i> The 19 mm Lug Trap
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  Vintage homages like Escapement Time 35mm use authentic 19 mm lugs. Jamming 20 mm leather pinches flanks; always order true 19 mm straps.
                </div>
              </div>
            </div>
          </div>

          <div style="margin-top: 1.25rem; padding-top: 0.85rem; border-top: 1px solid var(--ctp-surface0); font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-sapphire); display: flex; justify-content: space-between;">
            <span>Proportions Rule:</span>
            <span style="font-weight: 700;">20 mm tapering to 16 mm clasp</span>
          </div>
        </article>

        <!-- PANEL 4: L'ÉTABLI -->
        <article class="atelier-card" style="display: flex; flex-direction: column; justify-content: space-between; border-color: rgba(235, 160, 172, 0.2);">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.85rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--ctp-surface0);">
              <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-maroon); text-transform: uppercase; font-weight: 700; display: inline-flex; align-items: center; gap: 0.4rem;">
                <i class="fa-solid fa-toolbox"></i> L'Établi (Bench Tools)
              </span>
              <span style="font-size: 0.7rem; font-family: var(--font-mono); color: var(--ctp-overlay1); background: var(--ctp-crust); padding: 0.15rem 0.45rem; border-radius: 4px;">Mod &amp; Sizing Kit</span>
            </div>
            <h3 style="font-family: var(--font-display); font-size: 1.25rem; color: #fff; margin-bottom: 0.85rem;">
              Tools &amp; Scratch Prevention
            </h3>

            <div style="background: var(--ctp-crust); padding: 0.85rem; border-radius: var(--radius-md); border-left: 3px solid var(--ctp-maroon); margin-bottom: 0.75rem;">
              <div style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-maroon); font-weight: 700; text-transform: uppercase; margin-bottom: 0.25rem;">
                <i class="fa-solid fa-screwdriver"></i> Hollow-Ground Screwdrivers (1.2mm)
              </div>
              <div style="font-size: 0.825rem; color: var(--ctp-subtext1); line-height: 1.45;">
                Standard wedge screwdrivers cam out of screw link slots and gouge polished bracelet flanks. True watchmaker hollow-ground screwdrivers have parallel flat edges that seat fully in the slot for zero slips.
              </div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 0.6rem;">
              <div style="background: rgba(235, 160, 172, 0.05); padding: 0.75rem; border-radius: var(--radius-sm); border: 1px solid rgba(235, 160, 172, 0.15);">
                <div style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; color: var(--ctp-maroon); margin-bottom: 0.2rem;">
                  <i class="fa-solid fa-hammer"></i> Slotted Block &amp; Brass Mallet
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  Cheap blue plastic twist pin pushers bend instantly on tight collar pins. Use a slotted plastic block, steel punch, and gentle taps from a brass watchmaker mallet.
                </div>
              </div>

              <div style="background: rgba(137, 220, 235, 0.05); padding: 0.75rem; border-radius: var(--radius-sm); border: 1px solid rgba(137, 220, 235, 0.15);">
                <div style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; color: var(--ctp-sky); margin-bottom: 0.2rem;">
                  <i class="fa-solid fa-gem"></i> Diamond Selector II Verification
                </div>
                <div style="font-size: 0.8rem; color: var(--ctp-subtext1); line-height: 1.4;">
                  A ten-euro thermal conductivity probe instantly verifies whether an AliExpress seller shipped genuine corundum synthetic sapphire or cheap mineral glass.
                </div>
              </div>
            </div>
          </div>

          <div style="margin-top: 1.25rem; padding-top: 0.85rem; border-top: 1px solid var(--ctp-surface0); font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-maroon); display: flex; justify-content: space-between;">
            <span>Essential Bench Consumable:</span>
            <span style="font-weight: 700;">Kapton tape for masking lugs</span>
          </div>
        </article>

      </div>
    </section>
  </main>

  <div class="chemin-de-fer"></div>

  <!-- CLEAN ATELIER FOOTER -->
  <footer style="border-top: 1px solid var(--ctp-surface0); padding: 3rem 0; background: var(--ctp-crust);">
    <div class="container" style="display: flex; flex-direction: column; md:flex-row; justify-content: space-between; align-items: center; gap: 1.5rem; text-align: center; md:text-align: left;">
      <div>
        <div style="display: flex; align-items: center; justify-content: center; md:justify-content: flex-start; gap: 0.5rem; margin-bottom: 0.5rem;">
          <i class="fa-solid fa-stopwatch" style="color: var(--gold-primary);"></i>
          <span style="font-family: var(--font-display); font-weight: 700; color: #fff; font-size: 1.1rem;">Watch Radar</span>
          <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--gold-primary); background: var(--gold-bg); border: 1px solid var(--gold-border); padding: 0.15rem 0.45rem; border-radius: 4px;">Atelier Edition</span>
        </div>
        <p style="color: var(--ctp-subtext0); font-size: 0.85rem; max-width: 600px; line-height: 1.5;">
          Curated guide for budget mechanical and sweeping quartz timepieces. Real micrometer measurements, small-wrist ergonomics, and unbiased value assessments.
        </p>
      </div>

      <div style="display: flex; flex-direction: column; align-items: center; md:align-items: flex-end; gap: 0.5rem;">
        <div style="display: flex; gap: 0.75rem; font-family: var(--font-mono); font-size: 0.8rem; flex-wrap: wrap; justify-content: center;">
          <a href="https://samshady.github.io/watch-radar/" style="color: var(--gold-primary); text-decoration: none;">Watch Radar</a>
          <span style="color: var(--ctp-surface2);">&bull;</span>
          <a href="https://samshady.github.io/iem-radar/" style="color: var(--ctp-subtext1); text-decoration: none;">IEM Radar</a>
          <span style="color: var(--ctp-surface2);">&bull;</span>
          <a href="https://samshady.github.io/retro-handhelds-radar/" style="color: var(--ctp-subtext1); text-decoration: none;">Retro Handhelds</a>
        </div>
        <div style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--ctp-overlay1);">
          Curated in the Radar Atelier. 2026.
        </div>
      </div>
    </div>
  </footer>
"""
