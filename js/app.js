/* ═══════════════════════════════════════════════════════════════════════════
   Arquidiócesis de Maracaibo — app.js
   Unified Navigation & Interactivity System (2026 Edition)
   ═══════════════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', () => {
    // 1. Elements
    const navbar = document.getElementById('navbar');
    const toggle = document.getElementById('menuToggle');
    const navLinks = document.getElementById('navLinks');

    if (!navbar) return;

    // 2. Dynamic Mobile Drawer Backdrop Overlay
    let overlay = document.querySelector('.nav-overlay');
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.className = 'nav-overlay';
      document.body.appendChild(overlay);
    }

    // 3. Navbar scroll effect
    const hasFullHero = document.querySelector('.hero') !== null;
    
    function handleScroll() {
      if (window.scrollY > 60) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    }

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll(); // Initial call

    // 4. Hamburger & Drawer Navigation Toggle
    if (toggle && navLinks) {
      function openMenu() {
        navLinks.classList.add('active');
        overlay.classList.add('active');
        toggle.setAttribute('aria-expanded', 'true');
        document.body.style.overflow = 'hidden'; // Lock background scroll
      }

      function closeMenu() {
        navLinks.classList.remove('active');
        overlay.classList.remove('active');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = ''; // Restore background scroll
        // Collapse all mobile submenus
        const dropdowns = navLinks.querySelectorAll('.dropdown');
        dropdowns.forEach(d => d.classList.remove('mobile-open'));
      }

      toggle.addEventListener('click', (e) => {
        e.stopPropagation();
        const isOpen = navLinks.classList.contains('active');
        if (isOpen) {
          closeMenu();
        } else {
          openMenu();
        }
      });

      overlay.addEventListener('click', closeMenu);

      // Close menu on hitting ESC key
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
          closeMenu();
        }
      });

      // 5. Mobile Accordion logic for Dropdowns
      const dropdowns = navLinks.querySelectorAll('.dropdown');
      dropdowns.forEach(dropdown => {
        const btn = dropdown.querySelector('.dropbtn');
        if (btn) {
          btn.addEventListener('click', (e) => {
            if (window.innerWidth <= 1200) {
              e.preventDefault();
              e.stopPropagation();
              
              const isCurrentlyOpen = dropdown.classList.contains('mobile-open');
              
              // Collapse other open dropdowns
              dropdowns.forEach(other => {
                if (other !== dropdown) {
                  other.classList.remove('mobile-open');
                }
              });

              if (isCurrentlyOpen) {
                dropdown.classList.remove('mobile-open');
              } else {
                dropdown.classList.add('mobile-open');
              }
            }
          });
        }
      });

      // Close menu when clicking normal nav links
      navLinks.querySelectorAll('a:not(.dropbtn)').forEach(link => {
        link.addEventListener('click', () => {
          if (window.innerWidth <= 1200) {
            closeMenu();
          }
        });
      });
    }

    // 6. Active State Link Styling
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    if (navLinks) {
      navLinks.querySelectorAll('a[href]').forEach(link => {
        const href = link.getAttribute('href');
        if (href && href !== '#' && currentPage === href) {
          link.classList.add('nav-active');
          
          // Mark parent dropdown if link is sub-menu item
          const parentDropdown = link.closest('.dropdown');
          if (parentDropdown) {
            const btn = parentDropdown.querySelector('.dropbtn');
            if (btn) {
              btn.classList.add('nav-active');
            }
          }
        }
      });
    }

    // 7. Scroll Reveal Animations (Intersection Observer)
    const revealElements = document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right');
    
    if ('IntersectionObserver' in window && revealElements.length > 0) {
      const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target); // Trigger only once
          }
        });
      }, {
        threshold: 0.12,
        rootMargin: '0px 0px -40px 0px'
      });

      revealElements.forEach(el => revealObserver.observe(el));
    } else {
      // Fallback if IntersectionObserver is not supported
      revealElements.forEach(el => el.classList.add('visible'));
    }

    // 8. Statistics Counter Animation
    const counterElements = document.querySelectorAll('.stat-number');
    
    if ('IntersectionObserver' in window && counterElements.length > 0) {
      const counterObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const el = entry.target;
            const targetVal = parseInt(el.getAttribute('data-target') || '0', 10);
            animateCounter(el, targetVal);
            observer.unobserve(el);
          }
        });
      }, {
        threshold: 0.5
      });

      counterElements.forEach(el => counterObserver.observe(el));
    } else {
      // Fallback
      counterElements.forEach(el => {
        el.textContent = el.getAttribute('data-target') || el.textContent;
      });
    }

    function animateCounter(element, targetValue) {
      let currentVal = 0;
      const duration = 1500; // ms
      const startTime = performance.now();

      function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // Easing function (easeOutQuad)
        const ease = progress * (2 - progress);
        currentVal = Math.floor(ease * targetValue);
        
        element.textContent = currentVal.toLocaleString();

        if (progress < 1) {
          requestAnimationFrame(update);
        } else {
          element.textContent = targetValue.toLocaleString();
        }
      }

      requestAnimationFrame(update);
    }
  });
})();
