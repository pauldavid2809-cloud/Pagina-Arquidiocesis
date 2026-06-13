/* ═══════════════════════════════════════════════════════════════════════════
   Arquidiócesis de Maracaibo — main.js  (v2 · 2026)
   Vanilla JS — sin dependencias externas
   ═══════════════════════════════════════════════════════════════════════════ */

/* ── 1. Navbar — scroll state ──────────────────────────────────────────── */
const navbar = document.getElementById('navbar');
if (navbar) {
  const onScroll = () => {
    navbar.classList.toggle('scrolled', window.scrollY > 60);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

/* ── 2. Hamburger menu ─────────────────────────────────────────────────── */
const menuToggle = document.getElementById('menuToggle');
const navLinks   = document.getElementById('navLinks');
const navOverlay = document.getElementById('navOverlay');

const closeMenu = () => {
  if (!menuToggle) return;
  menuToggle.setAttribute('aria-expanded', 'false');
  navLinks?.classList.remove('active');
  navOverlay?.classList.remove('active');
  document.body.style.overflow = '';
};

const openMenu = () => {
  menuToggle.setAttribute('aria-expanded', 'true');
  navLinks?.classList.add('active');
  navOverlay?.classList.add('active');
  document.body.style.overflow = 'hidden';
};

menuToggle?.addEventListener('click', () => {
  const isOpen = menuToggle.getAttribute('aria-expanded') === 'true';
  isOpen ? closeMenu() : openMenu();
});

navOverlay?.addEventListener('click', closeMenu);

// Cerrar con Escape
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeMenu();
});

/* ── 3. Dropdown "Instituciones" (desktop hover / mobile tap) ──────────── */
document.querySelectorAll('.dropdown').forEach(dd => {
  const btn = dd.querySelector('.dropbtn');
  if (!btn) return;

  // Mobile: toggle con click
  btn.addEventListener('click', e => {
    const isMobile = window.innerWidth < 1100;
    if (!isMobile) return;
    e.preventDefault();
    const isOpen = dd.classList.contains('open');
    // Cerrar todos los demás
    document.querySelectorAll('.dropdown.open').forEach(d => d.classList.remove('open'));
    if (!isOpen) dd.classList.add('open');
    btn.setAttribute('aria-expanded', String(!isOpen));
  });
});

// Cerrar dropdowns al clickar fuera
document.addEventListener('click', e => {
  if (!e.target.closest('.dropdown')) {
    document.querySelectorAll('.dropdown.open').forEach(d => {
      d.classList.remove('open');
      d.querySelector('.dropbtn')?.setAttribute('aria-expanded', 'false');
    });
  }
});

/* ── 4. Fade-in con IntersectionObserver ───────────────────────────────── */
const fadeObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      fadeObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.fade-in').forEach(el => fadeObserver.observe(el));

/* ── 5. Contador animado para estadísticas ─────────────────────────────── */
function animateCounter(el, target, duration = 1400) {
  const prefix = el.dataset.prefix;
  // Si tiene prefijo fijo (ej: "+2M"), no animar
  if (prefix) return;

  let start = null;
  const step = (timestamp) => {
    if (!start) start = timestamp;
    const progress = Math.min((timestamp - start) / duration, 1);
    // Ease out cubic
    const eased = 1 - Math.pow(1 - progress, 3);
    el.textContent = Math.floor(eased * target).toLocaleString('es-VE');
    if (progress < 1) requestAnimationFrame(step);
    else el.textContent = target.toLocaleString('es-VE');
  };
  requestAnimationFrame(step);
}

const statObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const target = parseInt(el.dataset.count, 10);
      if (!isNaN(target)) animateCounter(el, target);
      statObserver.unobserve(el);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('.stat-number[data-count]').forEach(el => statObserver.observe(el));

/* ── 6. Hero scroll button ─────────────────────────────────────────────── */
// Ya está inline en el HTML con onclick. No se necesita nada aquí.

/* ── 7. Active nav link según URL actual ───────────────────────────────── */
const currentPage = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-item, .dropbtn').forEach(link => {
  const href = link.getAttribute('href') || '';
  if (href && currentPage === href.split('/').pop()) {
    link.classList.add('active');
  }
});

/* ── 8. Filtros del Directorio (directorio.html) ──────────────────────── */
const searchInput = document.getElementById('searchInput');
const zonaSelect  = document.getElementById('zonaSelect');
const resultsCount = document.getElementById('resultsCount');

if (searchInput || zonaSelect) {
  const filterCards = () => {
    const query = searchInput?.value.toLowerCase().trim() || '';
    const zona  = zonaSelect?.value || '';
    const allCards = document.querySelectorAll('[data-parroquia]');
    let visible = 0;

    allCards.forEach(card => {
      const name  = (card.dataset.parroquia || '').toLowerCase();
      const zCard = card.dataset.zona || '';
      const matchText = !query || name.includes(query);
      const matchZona = !zona  || zCard === zona;
      const show = matchText && matchZona;
      card.style.display = show ? '' : 'none';
      if (show) visible++;
    });

    if (resultsCount) resultsCount.textContent = `${visible} resultado${visible !== 1 ? 's' : ''}`;

    // Estado vacío
    const emptyState = document.getElementById('emptyState');
    if (emptyState) emptyState.style.display = visible === 0 ? 'flex' : 'none';
  };

  searchInput?.addEventListener('input', filterCards);
  zonaSelect?.addEventListener('change', filterCards);

  // Botón limpiar
  document.getElementById('clearFilters')?.addEventListener('click', () => {
    if (searchInput) searchInput.value = '';
    if (zonaSelect) zonaSelect.value = '';
    filterCards();
  });
}

/* ── 9. Tabs del Directorio ────────────────────────────────────────────── */
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const target = btn.dataset.tab;
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-pane').forEach(p => p.hidden = true);
    btn.classList.add('active');
    const pane = document.getElementById(target);
    if (pane) pane.hidden = false;
  });
});

/* ── 10. Pills de categoría en Noticias ────────────────────────────────── */
document.querySelectorAll('.pill[data-filter]').forEach(pill => {
  pill.addEventListener('click', () => {
    document.querySelectorAll('.pill[data-filter]').forEach(p => p.classList.remove('active'));
    pill.classList.add('active');
    const filter = pill.dataset.filter;
    document.querySelectorAll('[data-category]').forEach(card => {
      const show = !filter || filter === 'all' || card.dataset.category === filter;
      card.style.display = show ? '' : 'none';
    });
  });
});
