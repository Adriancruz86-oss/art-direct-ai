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

    if (typeof window.gtag === 'function') {
      window.gtag('event', name, payload);
    }

    if (typeof window.plausible === 'function') {
      window.plausible(name, { props: payload });
    }
  }

  const signupForm = document.getElementById('guide-signup');
  if (signupForm) {
    signupForm.addEventListener('submit', () => {
      track('free_guide_signup', {
        funnel_stage: 'lead_magnet',
        asset: '5 Mistakes Guide',
        provider: 'buttondown'
      });

      // Buttondown handles confirmation/validation in a new tab. The guide
      // opens immediately here so the promised freebie is not delayed.
      window.setTimeout(() => {
        window.location.href = 'free-guide.html';
      }, 250);
    });
  }

  document.querySelectorAll('a[href="#full-guide"]').forEach((link) => {
    link.addEventListener('click', () => {
      track('full_guide_interest', { funnel_stage: 'product_interest' });
    });
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

    document.querySelectorAll('[data-open-essay]').forEach((button) => {
      button.addEventListener('click', openEssay);
    });

    essayReader.querySelector('[data-close-essay]').addEventListener('click', () => essayReader.close());
    essayReader.addEventListener('click', (event) => {
      if (event.target === essayReader) essayReader.close();
    });
    essayReader.addEventListener('close', () => document.body.classList.remove('reader-open'));
  }

  window.ArtDirectAI = {
    track,
    attribution: () => {
      try { return JSON.parse(localStorage.getItem(TRACKING_KEY) || '{}'); }
      catch { return {}; }
    }
  };
})();
