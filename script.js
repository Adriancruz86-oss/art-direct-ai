(() => {
  const TRACKING_KEY = 'artDirectAiAttribution';
  const params = new URLSearchParams(window.location.search);

  // Keep the first campaign/referrer that brought a visitor in so later
  // downloads and purchases can be attributed to the original post.
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

    // Temporary per-browser counters are useful for testing. The same event
    // names are also sent to GA4/Plausible automatically once either is added.
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

  const guide = document.getElementById('download-guide');
  if (guide) {
    guide.addEventListener('click', () => {
      track('free_guide_open', {
        funnel_stage: 'lead_magnet',
        asset: '5 Mistakes Guide'
      });
    });
  }

  document.querySelectorAll('a[href="#full-guide"]').forEach((link) => {
    link.addEventListener('click', () => {
      track('full_guide_interest', { funnel_stage: 'product_interest' });
    });
  });

  // Future checkout buttons can opt into tracking without another JS rewrite:
  // add data-track="checkout_click" to the element.
  document.querySelectorAll('[data-track]').forEach((element) => {
    element.addEventListener('click', () => {
      track(element.dataset.track, { funnel_stage: element.dataset.stage || '' });
    });
  });

  window.ArtDirectAI = {
    track,
    attribution: () => {
      try { return JSON.parse(localStorage.getItem(TRACKING_KEY) || '{}'); }
      catch { return {}; }
    }
  };
})();
