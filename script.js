(() => {
  const TRACKING_KEY = 'artDirectAiAttribution';
  const params = new URLSearchParams(window.location.search);

  const existing = (() => {
    try { return JSON.parse(localStorage.getItem(TRACKING_KEY) || '{}'); }
    catch { return {}; }
  })();

  if (!existing.firstSeen) {
    const attribution = {
      firstSeen: new Date().toISOString(),
      landingPage: window.location.pathname,
      referrer: document.referrer || 'direct',
      utmSource: params.get('utm_source') || '',
      utmMedium: params.get('utm_medium') || '',
      utmCampaign: params.get('utm_campaign') || '',
      utmContent: params.get('utm_content') || ''
    };
    localStorage.setItem(TRACKING_KEY, JSON.stringify(attribution));
  }

  function track(name, details = {}) {
    const attribution = (() => {
      try { return JSON.parse(localStorage.getItem(TRACKING_KEY) || '{}'); }
      catch { return {}; }
    })();

    const key = `artDirectAi:${name}`;
    localStorage.setItem(key, String(Number(localStorage.getItem(key) || 0) + 1));
    const payload = { ...details, ...attribution };

    if (typeof window.gtag === 'function') window.gtag('event', name, payload);
    if (typeof window.plausible === 'function') window.plausible(name, { props: payload });
  }

  const signupForm = document.getElementById('guide-signup');
  if (signupForm) {
    signupForm.addEventListener('submit', () => {
      track('free_guide_signup', {
        funnel_stage: 'lead_magnet',
        asset: '5 Mistakes Guide',
        provider: 'buttondown'
      });
      window.setTimeout(() => { window.location.href = 'free-guide.html'; }, 250);
    });
  }

  document.querySelectorAll('a[href="#full-guide"]').forEach((link) => {
    link.addEventListener('click', () => track('full_guide_interest', { funnel_stage: 'product_interest' }));
  });

  document.querySelectorAll('[data-track]').forEach((element) => {
    element.addEventListener('click', () => {
      track(element.dataset.track, { funnel_stage: element.dataset.stage || '' });
    });
  });

  const essayReader = document.getElementById('essay-reader');
  if (essayReader) {
    const openEssay = () => {
      essayReader.scrollTop = 0;
      essayReader.showModal();
      document.body.classList.add('reader-open');
      track('essay_reader_open', { funnel_stage: 'editorial_interest' });
    };
    document.querySelectorAll('[data-open-essay]').forEach((button) => button.addEventListener('click', openEssay));
    essayReader.querySelector('[data-close-essay]').addEventListener('click', () => essayReader.close());
    essayReader.addEventListener('click', (event) => { if (event.target === essayReader) essayReader.close(); });
    essayReader.addEventListener('close', () => document.body.classList.remove('reader-open'));
  }

  // Public freebie for families. Keep it separate from the creator lead magnet:
  // no Gumroad gate and no author-site detour.
  const fullGuide = document.getElementById('full-guide');
  if (fullGuide && !document.getElementById('kids-ai-free-guide')) {
    const section = document.createElement('section');
    section.id = 'kids-ai-free-guide';
    section.className = 'free-guide';
    section.innerHTML = `
      <div class="section-shell free-grid">
        <div>
          <p class="kicker">FREE FOR KIDS + GROWN-UPS</p>
          <h2>5 Ways Your Kid Can Actually Use AI</h2>
          <p><strong>No homework. No cheating. Just creating.</strong></p>
          <p>A colorful 21-page activity guide that puts the kid in charge. Invent ridiculous machines, art-direct pictures, catch AI mistakes, create weird characters, and make something personal for somebody else.</p>
          <div class="guide-points">
            <span>✓ Five hands-on creative challenges</span>
            <span>✓ Jordan &amp; Evelyn throughout</span>
            <span>✓ Fact-checking without a lecture</span>
            <span>✓ Human ideas stay in charge</span>
          </div>
        </div>
        <div class="download-box guide-download-card">
          <p class="download-label">FREE • 21-PAGE PDF</p>
          <h3>Give them a blank page, not an answer key.</h3>
          <p>No email. No Gumroad. Download it directly from Art Direct AI and start making something.</p>
          <a class="button primary full" href="downloads/5_Ways_Your_Kid_Can_Actually_Use_AI_FREE.pdf" download data-track="kids_ai_pdf_download" data-stage="lead_magnet">Download the free activity guide</a>
          <a class="text-link" href="kids-ai-guide.html" data-track="kids_ai_web_guide_click" data-stage="lead_magnet" style="display:inline-block;margin-top:14px">Preview the activities online →</a>
          <p class="privacy-note">Free PDF. No signup required.</p>
        </div>
      </div>`;
    fullGuide.parentNode.insertBefore(section, fullGuide);

    section.querySelectorAll('[data-track]').forEach((element) => {
      element.addEventListener('click', () => {
        track(element.dataset.track, {
          funnel_stage: element.dataset.stage || 'lead_magnet',
          asset: '5 Ways Your Kid Can Actually Use AI'
        });
      });
    });
  }

  window.ArtDirectAI = {
    track,
    attribution: () => {
      try { return JSON.parse(localStorage.getItem(TRACKING_KEY) || '{}'); }
      catch { return {}; }
    }
  };
})();
