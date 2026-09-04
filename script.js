(() => {
  const download = document.getElementById('download-guide');
  if (!download) return;

  download.addEventListener('click', () => {
    // Local count is useful while testing. Real analytics can be added later
    // without changing the page structure.
    const key = 'artDirectAiGuideClicks';
    const count = Number(localStorage.getItem(key) || 0) + 1;
    localStorage.setItem(key, String(count));

    // Ready for common analytics providers if/when one is connected.
    if (typeof window.gtag === 'function') {
      window.gtag('event', 'free_guide_download', {
        event_category: 'lead_magnet',
        event_label: '5 Mistakes PDF'
      });
    }

    if (typeof window.plausible === 'function') {
      window.plausible('Free Guide Download');
    }
  });
})();
