(function () {
  const slides = Array.from(document.querySelectorAll('.slide'));
  const deck = document.querySelector('.deck');
  const progress = document.querySelector('.progress');
  const number = document.querySelector('.slide-number');
  const overview = document.createElement('div');
  const speakerPanel = document.createElement('div');
  let current = 0;

  if (!slides.length) return;

  function getPreviewIndex() {
    const params = new URLSearchParams(window.location.search);
    const value = Number(params.get('preview'));
    return Number.isFinite(value) && value > 0 ? value - 1 : null;
  }

  function render() {
    slides.forEach((slide, idx) => {
      slide.classList.toggle('is-active', idx === current);
    });

    if (progress) {
      progress.style.width = `${((current + 1) / slides.length) * 100}%`;
    }

    if (number) {
      number.textContent = `${String(current + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')}`;
    }

    const activeNotes = slides[current].querySelector('.notes');
    speakerPanel.innerHTML = activeNotes ? activeNotes.innerHTML : '<p>本页暂无演讲备注。</p>';
    window.location.hash = `/${current + 1}`;
  }

  function go(idx) {
    current = Math.max(0, Math.min(slides.length - 1, idx));
    render();
  }

  function next() {
    go(current + 1);
  }

  function prev() {
    go(current - 1);
  }

  function toggleOverview() {
    overview.classList.toggle('is-open');
  }

  function toggleSpeakerPanel() {
    speakerPanel.classList.toggle('is-open');
  }

  function cycleTheme() {
    const host = document.body;
    const themes = (host.dataset.themes || '').split(',').map((item) => item.trim()).filter(Boolean);
    const base = host.dataset.themeBase || './assets/themes/';
    const link = document.getElementById('theme-link');
    if (!themes.length || !link) return;

    const currentHref = link.getAttribute('href') || '';
    const currentName = currentHref.split('/').pop().replace('.css', '');
    const nextIndex = (themes.indexOf(currentName) + 1) % themes.length;
    link.setAttribute('href', `${base}${themes[nextIndex]}.css`);
  }

  function initOverview() {
    overview.className = 'overview';
    slides.forEach((slide, idx) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.innerHTML = `<span class="pill">${idx + 1}</span><h3>${slide.dataset.title || `Slide ${idx + 1}`}</h3>`;
      button.addEventListener('click', () => {
        go(idx);
        overview.classList.remove('is-open');
      });
      overview.appendChild(button);
    });
    document.body.appendChild(overview);
  }

  function initSpeakerPanel() {
    speakerPanel.className = 'speaker-panel';
    document.body.appendChild(speakerPanel);
  }

  document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowRight' || event.key === ' ' || event.key === 'PageDown') next();
    if (event.key === 'ArrowLeft' || event.key === 'PageUp') prev();
    if (event.key === 'Home') go(0);
    if (event.key === 'End') go(slides.length - 1);
    if (event.key.toLowerCase() === 'o') toggleOverview();
    if (event.key.toLowerCase() === 's') toggleSpeakerPanel();
    if (event.key.toLowerCase() === 't') cycleTheme();
    if (event.key.toLowerCase() === 'f' && deck && deck.requestFullscreen) deck.requestFullscreen();
    if (event.key === 'Escape') {
      overview.classList.remove('is-open');
      speakerPanel.classList.remove('is-open');
    }
  });

  const previewIndex = getPreviewIndex();
  if (previewIndex !== null) {
    document.body.classList.add('preview-mode');
    go(previewIndex);
    return;
  }

  const hashMatch = window.location.hash.match(/#\/(\d+)/);
  if (hashMatch) current = Math.max(0, Math.min(slides.length - 1, Number(hashMatch[1]) - 1));

  initOverview();
  initSpeakerPanel();
  render();
})();
