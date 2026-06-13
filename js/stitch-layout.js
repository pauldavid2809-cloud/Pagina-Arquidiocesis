(function () {
  'use strict';

  // Scroll navbar padding & shadow
  window.addEventListener('scroll', function () {
    var nav = document.querySelector('nav');
    if (!nav) return;
    if (window.scrollY > 50) {
      nav.classList.add('py-3', 'shadow-md');
      nav.classList.remove('py-4', 'shadow-sm');
    } else {
      nav.classList.add('py-4', 'shadow-sm');
      nav.classList.remove('py-3', 'shadow-md');
    }
  }, { passive: true });

  // Mobile drawer
  (function initMobileDrawer() {
    var mobileMenuBtn = document.getElementById('mobileMenuBtn');
    var closeDrawerBtn = document.getElementById('closeDrawerBtn');
    var mobileDrawer = document.getElementById('mobileDrawer');
    var mobileDrawerContent = document.getElementById('mobileDrawerContent');

    if (!mobileMenuBtn || !closeDrawerBtn || !mobileDrawer || !mobileDrawerContent) return;

    function openDrawer() {
      mobileDrawer.classList.remove('opacity-0', 'pointer-events-none');
      mobileDrawerContent.classList.remove('translate-x-full');
      document.body.style.overflow = 'hidden';
    }

    function closeDrawer() {
      mobileDrawer.classList.add('opacity-0', 'pointer-events-none');
      mobileDrawerContent.classList.add('translate-x-full');
      document.body.style.overflow = '';
    }

    mobileMenuBtn.addEventListener('click', openDrawer);
    closeDrawerBtn.addEventListener('click', closeDrawer);
    mobileDrawer.addEventListener('click', function (e) {
      if (e.target === mobileDrawer) closeDrawer();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeDrawer();
    });
    mobileDrawer.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', closeDrawer);
    });
  })();

  // Active nav link
  (function initActiveNav() {
    var currentPage = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('nav a[href]').forEach(function (link) {
      var href = link.getAttribute('href');
      if (!href || href.startsWith('http') || href.startsWith('#')) return;
      if (href === currentPage) {
        link.classList.add('text-primary', 'font-bold');
        link.classList.remove('text-on-surface-variant');
      }
    });
  })();
})();
