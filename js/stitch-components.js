/**
 * Stitch Sacred Modernism — Shared Layout Components
 * Injects consistent Navbar, Footer, and Mobile Menu across all pages.
 * 
 * Usage: 
 *   <script src="js/stitch-components.js"></script>
 *   <script>
 *     StitchLayout.init({ activePage: 'index' });
 *   </script>
 */
const StitchLayout = (() => {

  /* ── Navigation Data ─────────────────────────────────── */
  const NAV_LINKS = [
    { id: 'arquidiocesis', label: 'Arquidiócesis', href: 'arquidiocesis.html', icon: 'account_balance' },
    { id: 'arzobispo',     label: 'Arzobispo',     href: 'arzobispo.html',     icon: 'person' },
    { id: 'pastoral',      label: 'Pastoral',      href: 'pastoral.html',      icon: 'groups' },
    { id: 'noticias',      label: 'Noticias',      href: 'noticias.html',      icon: 'newspaper' },
    { id: 'directorio',    label: 'Directorio',    href: 'directorio.html',    icon: 'map' }
  ];

  const EXTRA_LINKS = [
    { id: 'seminario',        label: 'Seminario',        href: 'seminario.html',        icon: 'school' },
    { id: 'vida-consagrada',  label: 'Vida Consagrada',  href: 'vida-consagrada.html',  icon: 'auto_awesome' },
    { id: 'cancilleria',      label: 'Cancillería',      href: 'cancilleria.html',      icon: 'description' },
    { id: 'ambientes',        label: 'Ambientes Seguros', href: 'ambientes.html',        icon: 'verified_user' },
    { id: 'donaciones',       label: 'Donaciones',       href: 'donaciones.html',       icon: 'volunteer_activism' }
  ];

  /* ── Render Navbar ───────────────────────────────────── */
  function renderNavbar(activePage) {
    return `
    <header class="bg-surface/85 backdrop-blur-md sticky top-0 z-50 shadow-sm border-b border-outline-variant/10 transition-all duration-300" id="top-nav">
      <div class="flex justify-between items-center w-full px-margin-mobile md:px-gutter max-w-container-max mx-auto h-20 transition-all duration-300">
        <!-- Logo -->
        <a href="index.html" class="flex items-center gap-3 hover:opacity-90 transition-opacity shrink-0">
          <div class="w-11 h-11 shrink-0">
            <img alt="Arquidiócesis de Maracaibo" class="w-full h-full object-contain" 
                 src="img/logo-arquidiocesis.webp" 
                 onerror="this.onerror=null;this.src='https://lh3.googleusercontent.com/aida-public/AB6AXuBwA_WLOeM2SqpiNB8tqTn3YKrqPWYr_y8RGFGLuh89XZeUat7tXojr9Bcoz5zQHK3SvDEIvv0rNwEp9FIQQjF7eosV8uHZfxKpBz5D7m4Kl7M2AMbnXoGNdZLgycD6e7MPn_XxoIplHPL8IZ3GEVy7Wt03s8oyryyWvn3ItI1mhwxcEgb89RxGEny8RLhS4_fuuFX5tI5C5KtIuEgwiV_lPCxSBNSJjJAu8Q7YvoFT-HobMp4Tk4cOdePtiY8UODTXhw'">
          </div>
          <div class="flex flex-col">
            <span class="font-display text-[18px] font-bold text-crimson-deep leading-none tracking-tight">ARQUIDIÓCESIS</span>
            <span class="font-label text-[13px] font-bold tracking-[0.1em] text-slate-warm uppercase mt-0.5">de Maracaibo</span>
          </div>
        </a>

        <!-- Desktop Navigation -->
        <nav class="hidden lg:flex items-center gap-8">
          ${NAV_LINKS.map(l => `
            <a class="${activePage === l.id 
              ? 'text-crimson-deep border-b-2 border-gold-antique pb-1 font-bold' 
              : 'text-slate-warm hover:text-crimson-deep'} transition-colors duration-200 font-label text-[14px] tracking-wide" 
               href="${l.href}">${l.label}</a>
          `).join('')}
        </nav>

        <!-- Actions -->
        <div class="flex items-center gap-3">
          <a class="hidden md:inline-flex bg-crimson-deep text-white px-6 py-2.5 rounded-full font-label text-[13px] font-bold hover:bg-primary transition-all active:scale-95 duration-150 items-center gap-2" href="portal-sacerdotes.html">
            Portal Clero
          </a>
          <a class="hidden md:inline-flex items-center justify-center w-10 h-10 hover:bg-warm-ivory rounded-full transition-all" href="donaciones.html" title="Donaciones">
            <span class="material-symbols-outlined text-crimson-deep text-xl">volunteer_activism</span>
          </a>
          <button class="lg:hidden p-2 text-crimson-deep hover:bg-warm-ivory rounded-lg transition-colors" onclick="StitchLayout.toggleMobile()" aria-label="Abrir menú">
            <span class="material-symbols-outlined text-2xl">menu</span>
          </button>
        </div>
      </div>
    </header>`;
  }

  /* ── Render Mobile Menu ──────────────────────────────── */
  function renderMobileMenu(activePage) {
    const allLinks = [...NAV_LINKS, { divider: true }, ...EXTRA_LINKS];
    return `
    <div class="fixed inset-0 z-[60] pointer-events-none" id="mobile-overlay">
      <!-- Backdrop -->
      <div class="absolute inset-0 bg-black/0 transition-all duration-300" id="mobile-backdrop" onclick="StitchLayout.toggleMobile()"></div>
      <!-- Drawer -->
      <div class="fixed top-0 right-0 h-full w-[300px] bg-white shadow-2xl translate-x-full transition-transform duration-300 ease-out flex flex-col" id="mobile-drawer">
        <!-- Header -->
        <div class="flex justify-between items-center p-6 border-b border-outline-variant/10">
          <div class="flex flex-col">
            <span class="font-display text-[18px] font-bold text-crimson-deep leading-none">ARQUIDIÓCESIS</span>
            <span class="font-label text-[11px] tracking-[0.1em] text-slate-warm uppercase mt-1">de Maracaibo</span>
          </div>
          <button class="p-2 text-slate-warm hover:text-crimson-deep rounded-lg transition-colors" onclick="StitchLayout.toggleMobile()" aria-label="Cerrar menú">
            <span class="material-symbols-outlined text-2xl">close</span>
          </button>
        </div>
        <!-- Links -->
        <nav class="flex-1 overflow-y-auto p-6">
          <div class="flex flex-col gap-1">
            ${allLinks.map(l => {
              if (l.divider) return '<div class="h-px bg-outline-variant/20 my-3"></div>';
              const isActive = activePage === l.id;
              return `
              <a class="flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200 ${isActive 
                ? 'bg-primary-container text-white font-bold' 
                : 'text-slate-warm hover:bg-warm-ivory hover:text-crimson-deep'}" href="${l.href}">
                <span class="material-symbols-outlined text-[20px]">${l.icon}</span>
                <span class="font-label text-[14px]">${l.label}</span>
                ${isActive ? '<span class="ml-auto w-2 h-2 rounded-full bg-gold-antique"></span>' : ''}
              </a>`;
            }).join('')}
          </div>
        </nav>
        <!-- Footer -->
        <div class="p-6 border-t border-outline-variant/10 space-y-3">
          <a class="block w-full bg-crimson-deep text-white text-center py-3.5 rounded-xl font-label font-bold text-[14px] hover:bg-primary transition-colors" href="portal-sacerdotes.html">
            Portal del Clero
          </a>
          <a class="block w-full border-2 border-gold-antique text-gold-antique text-center py-3 rounded-xl font-label font-bold text-[14px] hover:bg-gold-antique hover:text-white transition-all" href="donaciones.html">
            Hacer Donación
          </a>
        </div>
      </div>
    </div>`;
  }

  /* ── Render Footer ───────────────────────────────────── */
  function renderFooter() {
    return `
    <footer class="bg-surface-container-highest border-t border-outline-variant/20 w-full pt-16 pb-8">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-gutter px-margin-mobile md:px-gutter max-w-container-max mx-auto">
        <!-- Branding -->
        <div class="md:col-span-1 space-y-4">
          <a href="index.html" class="block">
            <div class="font-display text-[26px] text-crimson-deep font-bold leading-tight">Arquidiócesis <br> de Maracaibo</div>
          </a>
          <p class="font-body text-[14px] text-slate-warm leading-relaxed">
            Av. 4 con calle 95, frente a la Plaza Bolívar. Maracaibo, Estado Zulia, Venezuela.
          </p>
          <div class="flex gap-3">
            <a class="w-10 h-10 rounded-full border border-outline-variant flex items-center justify-center text-slate-warm hover:bg-crimson-deep hover:border-crimson-deep hover:text-white transition-all" href="https://www.instagram.com/arquimcbo/" target="_blank" rel="noopener" aria-label="Instagram">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
            </a>
            <a class="w-10 h-10 rounded-full border border-outline-variant flex items-center justify-center text-slate-warm hover:bg-crimson-deep hover:border-crimson-deep hover:text-white transition-all" href="https://www.youtube.com/@arquidicosisdemaracaibo" target="_blank" rel="noopener" aria-label="YouTube">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
            </a>
          </div>
        </div>

        <!-- Resources -->
        <div class="md:col-span-1">
          <h4 class="font-label text-[12px] text-crimson-deep uppercase tracking-widest mb-5 font-bold">Recursos</h4>
          <ul class="space-y-3">
            <li><a class="font-label text-[13px] text-slate-warm hover:text-crimson-deep underline-offset-4 hover:underline transition-all" href="directorio.html">Directorio de Parroquias</a></li>
            <li><a class="font-label text-[13px] text-slate-warm hover:text-crimson-deep underline-offset-4 hover:underline transition-all" href="ambientes.html">Ambientes Seguros</a></li>
            <li><a class="font-label text-[13px] text-slate-warm hover:text-crimson-deep underline-offset-4 hover:underline transition-all" href="cancilleria.html">Cancillería</a></li>
            <li><a class="font-label text-[13px] text-slate-warm hover:text-crimson-deep underline-offset-4 hover:underline transition-all" href="donaciones.html">Donaciones</a></li>
            <li><a class="font-label text-[13px] text-slate-warm hover:text-crimson-deep underline-offset-4 hover:underline transition-all" href="noticias.html">Noticias</a></li>
          </ul>
        </div>

        <!-- Institutions -->
        <div class="md:col-span-1">
          <h4 class="font-label text-[12px] text-crimson-deep uppercase tracking-widest mb-5 font-bold">Instituciones</h4>
          <ul class="space-y-3">
            <li><a class="font-label text-[13px] text-slate-warm hover:text-crimson-deep underline-offset-4 hover:underline transition-all" href="seminario.html">Seminario Conciliar</a></li>
            <li><a class="font-label text-[13px] text-slate-warm hover:text-crimson-deep underline-offset-4 hover:underline transition-all" href="vida-consagrada.html">Vida Consagrada</a></li>
            <li><a class="font-label text-[13px] text-slate-warm hover:text-crimson-deep underline-offset-4 hover:underline transition-all" href="https://tribunaleclesiasticomaracaibo.org/" target="_blank" rel="noopener">Tribunal Eclesiástico</a></li>
            <li><a class="font-label text-[13px] text-slate-warm hover:text-crimson-deep underline-offset-4 hover:underline transition-all" href="pastoral.html">Vicaría de Pastoral</a></li>
            <li><a class="font-label text-[13px] text-slate-warm hover:text-crimson-deep underline-offset-4 hover:underline transition-all font-bold text-crimson-deep" href="portal-sacerdotes.html">Portal del Clero</a></li>
          </ul>
        </div>

        <!-- Contact -->
        <div class="md:col-span-1">
          <h4 class="font-label text-[12px] text-crimson-deep uppercase tracking-widest mb-5 font-bold">Contacto</h4>
          <div class="space-y-3 text-[14px] text-slate-warm font-body">
            <p>info@arquidiocesisdemaracaibo.org</p>
            <p>+58 261 722 83 24</p>
          </div>
          <div class="mt-5 bg-surface-container rounded-xl p-4 border border-outline-variant/10">
            <p class="font-bold text-crimson-deep text-[13px] mb-1">Despacho Curia</p>
            <p class="text-slate-warm text-[12px]">Lun a Vie: 8:30 AM – 1:00 PM</p>
          </div>
        </div>
      </div>
      <div class="max-w-container-max mx-auto px-margin-mobile md:px-gutter mt-10 pt-6 border-t border-outline-variant/15">
        <p class="font-body text-[13px] text-center text-slate-warm/60">
          © ${new Date().getFullYear()} Arquidiócesis de Maracaibo. Todos los derechos reservados. Sacred Modernism.
        </p>
      </div>
    </footer>`;
  }

  /* ── Mobile Menu Toggle ──────────────────────────────── */
  let mobileOpen = false;

  function toggleMobile() {
    mobileOpen = !mobileOpen;
    const overlay  = document.getElementById('mobile-overlay');
    const backdrop = document.getElementById('mobile-backdrop');
    const drawer   = document.getElementById('mobile-drawer');
    if (!overlay) return;

    if (mobileOpen) {
      overlay.classList.remove('pointer-events-none');
      backdrop.classList.replace('bg-black/0', 'bg-black/40');
      drawer.classList.remove('translate-x-full');
      document.body.style.overflow = 'hidden';
    } else {
      backdrop.classList.replace('bg-black/40', 'bg-black/0');
      drawer.classList.add('translate-x-full');
      setTimeout(() => {
        overlay.classList.add('pointer-events-none');
        document.body.style.overflow = '';
      }, 300);
    }
  }

  /* ── Scroll Effects ──────────────────────────────────── */
  function initScrollEffects() {
    const header = document.getElementById('top-nav');
    if (!header) return;

    let lastScrollY = 0;
    window.addEventListener('scroll', () => {
      const nav = header.querySelector('div');
      if (window.scrollY > 50) {
        header.classList.add('shadow-md');
        if (nav) nav.classList.replace('h-20', 'h-16');
      } else {
        header.classList.remove('shadow-md');
        if (nav) nav.classList.replace('h-16', 'h-20');
      }
      lastScrollY = window.scrollY;
    }, { passive: true });

    // Close mobile on escape
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileOpen) toggleMobile();
    });
  }

  /* ── Scroll Reveal Animation ─────────────────────────── */
  function initRevealAnimations() {
    if (!('IntersectionObserver' in window)) return;
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
  }

  /* ── Init ────────────────────────────────────────────── */
  function init(options = {}) {
    const activePage = options.activePage || '';

    // Inject navbar at the start of body
    const navPlaceholder = document.getElementById('stitch-navbar');
    if (navPlaceholder) {
      navPlaceholder.outerHTML = renderNavbar(activePage);
    } else {
      document.body.insertAdjacentHTML('afterbegin', renderNavbar(activePage));
    }

    // Inject mobile menu
    document.body.insertAdjacentHTML('beforeend', renderMobileMenu(activePage));

    // Inject footer
    const footerPlaceholder = document.getElementById('stitch-footer');
    if (footerPlaceholder) {
      footerPlaceholder.outerHTML = renderFooter();
    } else {
      // Find existing footer or append before last script
      const existingFooter = document.querySelector('footer');
      if (existingFooter) {
        existingFooter.outerHTML = renderFooter();
      } else {
        document.body.insertAdjacentHTML('beforeend', renderFooter());
      }
    }

    // Initialize interactions
    initScrollEffects();
    initRevealAnimations();
  }

  /* ── Public API ──────────────────────────────────────── */
  return { init, toggleMobile, initRevealAnimations };

})();
