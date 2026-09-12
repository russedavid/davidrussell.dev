(() => {
  const toggle = document.getElementById('theme-toggle');
  const root = document.documentElement;
  const update = () => {
    const dark = root.dataset.theme === 'dark';
    toggle?.setAttribute('aria-label', dark ? 'Use light theme' : 'Use dark theme');
    toggle?.setAttribute('aria-pressed', String(dark));
    const label = toggle?.querySelector('[data-theme-label]');
    if (label) label.textContent = dark ? 'Light' : 'Dark';
  };
  toggle?.addEventListener('click', () => {
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('theme', root.dataset.theme); } catch {}
    update();
  });
  update();
})();
