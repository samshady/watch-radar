# scripts/templates/card_js.py
# JavaScript logic, card generator, dynamic caliper wrist calculator, JOMW video links, and Lume mode

CARD_JS = """
  <script>
    const WATCH_DATA = __WATCH_DATA_PLACEHOLDER__;

    // DOM Elements
    const searchInput = document.getElementById('search-input');
    const archetypeFilter = document.getElementById('archetype-filter');
    const movementFilter = document.getElementById('movement-filter');
    const l2lSlider = document.getElementById('l2l-filter-slider');
    const l2lSliderDisplay = document.getElementById('l2l-slider-display');
    const wristSlider = document.getElementById('wrist-slider');
    const wristCircDisplay = document.getElementById('wrist-circumference-display');
    const flatSpanDisplay = document.getElementById('flat-span-display');
    const visibleCount = document.getElementById('visible-count');
    const totalCount = document.getElementById('total-count');
    const watchGrid = document.getElementById('watch-grid');
    const priceTabs = document.querySelectorAll('.price-tab-btn');
    const lumeToggleBtn = document.getElementById('lume-toggle-btn');
    const lumeBtnText = document.getElementById('lume-btn-text');

    let currentPriceMode = 'choice';
    let currentWristCirc = 16.5;
    let currentFlatSpan = 47.0;

    totalCount.textContent = WATCH_DATA.length;

    // Calculate anatomical flat top span in mm from circumference in cm
    function calculateFlatSpan(circumferenceCm) {
      return (circumferenceCm * 10 * 0.285).toFixed(1);
    }

    // Lume Darkroom Mode Toggle
    let lumeActive = false;
    lumeToggleBtn.addEventListener('click', () => {
      lumeActive = !lumeActive;
      document.body.classList.toggle('lume-mode', lumeActive);
      if (lumeActive) {
        lumeBtnText.textContent = 'Lume Darkroom: ON';
        lumeBtnText.style.color = 'var(--lume-bgw9)';
        if (typeof confetti === 'function') {
          confetti({
            particleCount: 35,
            spread: 50,
            origin: { y: 0.15 },
            colors: ['#00e5ff', '#39ff14', '#eed49f']
          });
        }
      } else {
        lumeBtnText.textContent = 'Lume Darkroom: OFF';
        lumeBtnText.style.color = '';
      }
    });

    // Wrist Caliper Slider Listener
    wristSlider.addEventListener('input', (e) => {
      currentWristCirc = parseFloat(e.target.value);
      currentFlatSpan = parseFloat(calculateFlatSpan(currentWristCirc));
      
      const inches = (currentWristCirc / 2.54).toFixed(1);
      wristCircDisplay.textContent = `${currentWristCirc.toFixed(1)} cm / ${inches}"`;
      flatSpanDisplay.textContent = `${currentFlatSpan.toFixed(1)} mm`;

      renderWatches();
    });

    // Filter controls
    l2lSlider.addEventListener('input', (e) => {
      const val = parseFloat(e.target.value).toFixed(1);
      l2lSliderDisplay.textContent = `${val} mm`;
      renderWatches();
    });

    searchInput.addEventListener('input', renderWatches);
    archetypeFilter.addEventListener('change', renderWatches);
    movementFilter.addEventListener('change', renderWatches);

    priceTabs.forEach(btn => {
      btn.addEventListener('click', () => {
        priceTabs.forEach(b => {
          b.classList.remove('active');
          b.style.background = 'var(--ctp-surface0)';
          b.style.color = 'var(--ctp-subtext0)';
          b.style.borderColor = 'var(--ctp-surface1)';
        });
        btn.classList.add('active');
        btn.style.background = 'var(--gold-bg)';
        btn.style.color = 'var(--gold-primary)';
        btn.style.borderColor = 'var(--gold-border)';
        currentPriceMode = btn.getAttribute('data-mode');
        renderWatches();
      });
    });

    function renderWatches() {
      const query = searchInput.value.toLowerCase().trim();
      const archetype = archetypeFilter.value;
      const movement = movementFilter.value;
      const maxL2L = parseFloat(l2lSlider.value);

      const filtered = WATCH_DATA.filter(w => {
        if (w.lug_to_lug_mm > maxL2L) return false;
        if (archetype !== 'all' && !w.archetype.includes(archetype)) return false;
        if (movement !== 'all' && !w.movement.includes(movement)) return false;
        if (query) {
          const haystack = `${w.brand} ${w.model} ${w.archetype} ${w.movement} ${w.crystal} ${w.wrist_notes}`.toLowerCase();
          if (!haystack.includes(query)) return false;
        }
        return true;
      });

      // Sort by JOMW Spec Score descending
      filtered.sort((a, b) => b.jomw_spec_score - a.jomw_spec_score);

      visibleCount.textContent = filtered.length;

      if (filtered.length === 0) {
        watchGrid.innerHTML = `
          <div style="grid-column: 1 / -1; padding: 3rem 1.5rem; text-align: center; background: var(--ctp-mantle); border-radius: var(--radius-lg); border: 1px dashed var(--ctp-surface2);">
            <div style="font-size: 2rem; color: var(--ctp-overlay1); margin-bottom: 0.5rem;"><i class="fa-solid fa-gauge"></i></div>
            <p style="font-family: var(--font-display); font-size: 1.25rem; color: var(--ctp-subtext1); margin-bottom: 0.5rem;">No watches match your filter criteria</p>
            <p style="font-size: 0.875rem; color: var(--ctp-overlay1);">Try raising the Lug-To-Lug slider or resetting search parameters.</p>
          </div>
        `;
        return;
      }

      watchGrid.innerHTML = filtered.map(w => {
        let displayPrice = w.choice_price_eur;
        let priceLabel = 'Ali Choice';
        if (currentPriceMode === 'singles') {
          displayPrice = w.singles_day_price_eur;
          priceLabel = '11.11 Lowest';
        } else if (currentPriceMode === 'street') {
          displayPrice = w.street_price_eur;
          priceLabel = 'Retail';
        }

        // Dynamic wrist fit evaluation
        let fitClass = 'color: var(--ctp-green); background: rgba(166, 227, 161, 0.1); border-color: rgba(166, 227, 161, 0.3);';
        let fitIcon = 'fa-solid fa-circle-check';
        let fitTitle = 'Tailored Zero Overhang';
        let fitDesc = 'Lug tips sit comfortably within your wrist silhouette.';

        const diff = w.lug_to_lug_mm - currentFlatSpan;
        if (diff > 1.5) {
          fitClass = 'color: var(--ctp-red); background: rgba(243, 139, 168, 0.1); border-color: rgba(243, 139, 168, 0.3);';
          fitIcon = 'fa-solid fa-triangle-exclamation';
          fitTitle = 'Overhang Alert';
          fitDesc = `L2L (${w.lug_to_lug_mm}mm) exceeds flat span (${currentFlatSpan}mm) by ${diff.toFixed(1)}mm.`;
        } else if (diff >= -1.5) {
          fitClass = 'color: var(--ctp-yellow); background: rgba(249, 226, 175, 0.1); border-color: rgba(249, 226, 175, 0.3);';
          fitIcon = 'fa-solid fa-circle-exclamation';
          fitTitle = 'Borderline Flush';
          fitDesc = 'Lug tips reach the outer bone edge. Wear on flexible strap.';
        }

        const prosHtml = w.pros.map(p => `<li style="display: flex; gap: 0.35rem; align-items: flex-start;"><i class="fa-solid fa-check" style="color: var(--ctp-green); margin-top: 0.2rem; font-size: 0.75rem;"></i><span>${p}</span></li>`).join('');
        const consHtml = w.cons.map(c => `<li style="display: flex; gap: 0.35rem; align-items: flex-start;"><i class="fa-solid fa-xmark" style="color: var(--ctp-red); margin-top: 0.2rem; font-size: 0.75rem;"></i><span>${c}</span></li>`).join('');

        const videoBtnHtml = w.jomw_video_url ? `
          <div style="display: flex; justify-content: flex-end; margin-top: 0.4rem;">
            <a href="${w.jomw_video_url}" target="_blank" rel="noopener noreferrer" class="btn-tactile" style="display: inline-flex; align-items: center; gap: 0.4rem; background: rgba(239, 68, 68, 0.12); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); font-family: var(--font-mono); font-size: 0.7rem; font-weight: 600; padding: 0.25rem 0.55rem; border-radius: 4px; text-decoration: none;" title="Watch Jody's Review on YouTube">
              <i class="fa-brands fa-youtube" style="color: #ef4444; font-size: 0.85rem;"></i>
              <span>JOMW Video Review</span>
            </a>
          </div>
        ` : '';

        return `
          <article class="atelier-card watch-card" style="display: flex; flex-direction: column; justify-content: space-between; position: relative;">
            <div>
              <!-- Image & Top Header -->
              <div style="position: relative; margin: -1.25rem -1.25rem 1rem -1.25rem; border-top-left-radius: var(--radius-lg); border-top-right-radius: var(--radius-lg); overflow: hidden; background: #11111b; aspect-ratio: 16/10; border-bottom: 1px solid var(--ctp-surface0);">
                <img src="${w.image}" alt="${w.brand} ${w.model}" class="watch-thumb-img" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;" onmouseover="this.style.transform='scale(1.04)'" onmouseout="this.style.transform='scale(1)'">
                
                <div style="position: absolute; top: 0.75rem; left: 0.75rem; display: flex; gap: 0.4rem; flex-wrap: wrap;">
                  <span style="background: rgba(17, 17, 27, 0.85); backdrop-filter: blur(4px); border: 1px solid var(--gold-border); color: var(--gold-primary); font-family: var(--font-mono); font-size: 0.7rem; font-weight: 700; padding: 0.2rem 0.5rem; border-radius: 4px; text-transform: uppercase;">
                    ${w.brand}
                  </span>
                  <span style="background: rgba(17, 17, 27, 0.85); backdrop-filter: blur(4px); border: 1px solid var(--ctp-surface1); color: var(--ctp-subtext1); font-family: var(--font-mono); font-size: 0.7rem; padding: 0.2rem 0.5rem; border-radius: 4px;">
                    ${w.archetype}
                  </span>
                </div>

                <div style="position: absolute; top: 0.75rem; right: 0.75rem; background: rgba(17, 17, 27, 0.9); backdrop-filter: blur(4px); border: 1px solid var(--gold-border); border-radius: 8px; padding: 0.25rem 0.55rem; text-align: center;">
                  <div style="font-size: 0.55rem; font-family: var(--font-mono); color: var(--gold-primary); text-transform: uppercase; font-weight: 700;">JOMW</div>
                  <div style="font-size: 0.95rem; font-family: var(--font-mono); font-weight: 800; color: #fff;">${w.jomw_spec_score}</div>
                </div>
              </div>

              <!-- Title & Model -->
              <div style="margin-bottom: 1rem;">
                <h3 style="font-family: var(--font-display); font-size: 1.25rem; font-weight: 700; color: #fff; line-height: 1.25;">
                  ${w.model}
                </h3>
              </div>

              <!-- Micrometer Specs Matrix -->
              <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.4rem; background: var(--ctp-crust); padding: 0.65rem; border-radius: var(--radius-md); border: 1px solid var(--ctp-surface0); margin-bottom: 0.85rem; text-align: center;">
                <div>
                  <div style="font-size: 0.65rem; font-family: var(--font-mono); color: var(--ctp-overlay1); text-transform: uppercase;">Diameter</div>
                  <div style="font-size: 0.85rem; font-family: var(--font-mono); font-weight: 700; color: var(--ctp-text);">${w.case_diameter_mm}mm</div>
                </div>
                <div style="background: rgba(238, 212, 159, 0.08); border-radius: 4px;">
                  <div style="font-size: 0.65rem; font-family: var(--font-mono); color: var(--gold-primary); text-transform: uppercase; font-weight: 700;">L2L</div>
                  <div style="font-size: 0.85rem; font-family: var(--font-mono); font-weight: 800; color: var(--gold-primary);">${w.lug_to_lug_mm}mm</div>
                </div>
                <div>
                  <div style="font-size: 0.65rem; font-family: var(--font-mono); color: var(--ctp-overlay1); text-transform: uppercase;">Thick</div>
                  <div style="font-size: 0.85rem; font-family: var(--font-mono); font-weight: 700; color: var(--ctp-text);">${w.thickness_mm}mm</div>
                </div>
                <div>
                  <div style="font-size: 0.65rem; font-family: var(--font-mono); color: var(--ctp-overlay1); text-transform: uppercase;">Lug</div>
                  <div style="font-size: 0.85rem; font-family: var(--font-mono); font-weight: 700; color: var(--ctp-text);">${w.lug_width_mm}mm</div>
                </div>
              </div>

              <!-- Dynamic Wrist Caliper Assessment -->
              <div style="padding: 0.65rem 0.85rem; border-radius: var(--radius-md); border: 1px solid; margin-bottom: 0.85rem; font-size: 0.75rem; font-family: var(--font-mono); ${fitClass}">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.2rem;">
                  <span style="font-weight: 700; display: inline-flex; align-items: center; gap: 0.35rem;">
                    <i class="${fitIcon}"></i> ${fitTitle}
                  </span>
                  <span style="opacity: 0.85;">${w.lug_to_lug_mm}mm vs ${currentFlatSpan}mm</span>
                </div>
                <div style="font-family: var(--font-body); opacity: 0.9; line-height: 1.35;">
                  ${fitDesc}
                </div>
              </div>

              <!-- Technical Specifications -->
              <div style="background: var(--ctp-surface0); padding: 0.75rem; border-radius: var(--radius-md); border: 1px solid var(--ctp-surface1); margin-bottom: 0.85rem; font-size: 0.75rem; font-family: var(--font-mono); display: flex; flex-direction: column; gap: 0.35rem;">
                <div style="display: flex; justify-content: space-between;">
                  <span style="color: var(--ctp-overlay1);">Caliber Engine:</span>
                  <span style="color: #fff; font-weight: 600;">${w.movement}</span>
                </div>
                <div style="display: flex; justify-content: space-between;">
                  <span style="color: var(--ctp-overlay1);">Crystal Glass:</span>
                  <span style="color: #fff;">${w.crystal}</span>
                </div>
                <div style="display: flex; justify-content: space-between;">
                  <span style="color: var(--ctp-overlay1);">Bezel Insert:</span>
                  <span style="color: #fff;">${w.bezel}</span>
                </div>
                <div style="display: flex; justify-content: space-between;">
                  <span style="color: var(--ctp-overlay1);">Water Resist:</span>
                  <span style="color: #fff;">${w.water_resistance_m}m ${w.water_resistance_m >= 100 ? '(Screw Crown)' : '(Push-Pull)'}</span>
                </div>
                <div style="display: flex; justify-content: space-between;">
                  <span style="color: var(--ctp-overlay1);">Lume Rating:</span>
                  <span class="lume-target" style="color: var(--lume-bgw9); font-weight: 600;">${w.lume}</span>
                </div>
              </div>

              <!-- Pros & Cons -->
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.6rem; font-size: 0.75rem; margin-bottom: 0.85rem;">
                <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.3rem;">${prosHtml}</ul>
                <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.3rem;">${consHtml}</ul>
              </div>

              <!-- JOMW Quote & Video Link -->
              <div style="background: var(--ctp-crust); padding: 0.75rem 0.85rem; border-radius: var(--radius-sm); border-left: 2px solid var(--gold-primary); margin-bottom: 1rem;">
                <div style="font-size: 0.75rem; color: var(--ctp-subtext1); font-style: italic; line-height: 1.4;">
                  "${w.jomw_quote}"
                </div>
                ${videoBtnHtml}
              </div>
            </div>

            <!-- Footer Price & Buy Links -->
            <div style="padding-top: 0.85rem; border-top: 1px solid var(--ctp-surface0);">
              <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 0.85rem;">
                <div>
                  <div style="font-size: 0.65rem; font-family: var(--font-mono); color: var(--ctp-overlay1); text-transform: uppercase;">${priceLabel}</div>
                  <div style="font-size: 1.4rem; font-family: var(--font-display); font-weight: 800; color: var(--gold-primary); line-height: 1;">
                    &euro;${displayPrice.toFixed(0)}
                  </div>
                </div>
                <div style="display: flex; gap: 0.35rem; font-family: var(--font-mono); font-size: 0.7rem;">
                  <span style="background: var(--ctp-surface0); padding: 0.2rem 0.4rem; border-radius: 4px; color: var(--ctp-subtext0);" title="Standard Retail">&euro;${w.street_price_eur.toFixed(0)}</span>
                  <span style="background: var(--gold-bg); border: 1px solid var(--gold-border); padding: 0.2rem 0.4rem; border-radius: 4px; color: var(--gold-primary);" title="AliExpress Choice">&euro;${w.choice_price_eur.toFixed(0)}</span>
                  <span style="background: rgba(250, 179, 135, 0.1); border: 1px solid rgba(250, 179, 135, 0.3); padding: 0.2rem 0.4rem; border-radius: 4px; color: var(--ctp-peach);" title="11.11 Lowest">&euro;${w.singles_day_price_eur.toFixed(0)}</span>
                </div>
              </div>

              <!-- Buy Action Buttons -->
              <div style="display: grid; grid-template-columns: 1.3fr 1fr; gap: 0.5rem;">
                <a href="${w.buy_url_aliexpress}" target="_blank" rel="noopener noreferrer" class="btn-tactile" style="display: flex; align-items: center; justify-content: center; gap: 0.4rem; background: var(--gold-primary); color: #11111b; font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; padding: 0.65rem 0.5rem; border-radius: var(--radius-sm); text-decoration: none; border: 1px solid var(--gold-hover);">
                  <i class="fa-solid fa-cart-shopping"></i>
                  <span>Ali Choice</span>
                </a>
                <a href="${w.buy_url_alt}" target="_blank" rel="noopener noreferrer" class="btn-tactile" style="display: flex; align-items: center; justify-content: center; gap: 0.4rem; background: var(--ctp-surface0); color: var(--ctp-text); font-family: var(--font-mono); font-size: 0.75rem; font-weight: 600; padding: 0.65rem 0.5rem; border-radius: var(--radius-sm); text-decoration: none; border: 1px solid var(--ctp-surface1);">
                  <i class="fa-solid fa-arrow-up-right-from-square"></i>
                  <span>Amazon/Alt</span>
                </a>
              </div>
            </div>
          </article>
        `;
      }).join('');
    }

    // Initial render
    renderWatches();
  </script>
</body>
</html>
"""
