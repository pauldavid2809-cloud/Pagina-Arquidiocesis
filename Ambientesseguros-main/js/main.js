/**
 * Main Javascript for Ambientes Seguros - Arquidiócesis de Maracaibo
 */

document.addEventListener('DOMContentLoaded', () => {
    initNavbar();
    initMobileMenu();
    initStatsCounter();
    initContactForm();
    initAnimations();
    initHeroCanvas();
    initCardTilt();
});

/* ─── NAVBAR ─── */
function initNavbar() {
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        navbar.classList.toggle('scrolled', window.scrollY > 50);
    });
}

/* ─── MOBILE MENU ─── */
function initMobileMenu() {
    const navToggle = document.getElementById('navToggle');
    const navLinks  = document.getElementById('navLinks');
    if (!navToggle || !navLinks) return;

    navToggle.addEventListener('click', () => {
        navLinks.classList.toggle('mobile-active');
        navToggle.classList.toggle('active');
        const spans = navToggle.querySelectorAll('span');
        const isActive = navToggle.classList.contains('active');
        spans[0].style.transform = isActive ? 'rotate(45deg) translate(5px, 5px)' : 'none';
        spans[1].style.opacity   = isActive ? '0' : '1';
        spans[2].style.transform = isActive ? 'rotate(-45deg) translate(7px, -6px)' : 'none';
    });

    navLinks.querySelectorAll('.nav-item').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('mobile-active');
            navToggle.classList.remove('active');
            navToggle.querySelectorAll('span').forEach(s => {
                s.style.transform = 'none';
                s.style.opacity   = '1';
            });
        });
    });
}

/* ─── STATS COUNTER ─── */
function initStatsCounter() {
    const stats = document.querySelectorAll('.stat-number');
    if (!stats.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCount(entry.target, parseInt(entry.target.dataset.target));
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    stats.forEach(s => observer.observe(s));
}

function animateCount(el, target) {
    let start = null;
    const duration = 2000;
    const step = (timestamp) => {
        if (!start) start = timestamp;
        const progress = Math.min((timestamp - start) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.floor(eased * target);
        if (progress < 1) requestAnimationFrame(step);
        else el.textContent = target;
    };
    requestAnimationFrame(step);
}

/* ─── CONTACT FORM ─── */
function initContactForm() {
    const form    = document.getElementById('contact-form');
    const success = document.getElementById('form-success');
    if (!form) return;

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        let isValid = true;

        form.querySelectorAll('[required]').forEach(field => {
            if (field.type === 'checkbox') {
                const valid = field.checked;
                field.parentElement.style.color = valid ? 'inherit' : 'var(--danger-color)';
                if (!valid) isValid = false;
            } else {
                const valid = field.value.trim() !== '';
                field.style.borderColor = valid ? '#ddd' : 'var(--danger-color)';
                if (!valid) isValid = false;
            }
        });

        if (!isValid) return;

        const btn = form.querySelector('button[type="submit"]');
        btn.disabled = true;
        btn.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> Enviando...';

        setTimeout(() => {
            form.style.display = 'none';
            success.style.display = 'block';
            success.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }, 1500);
    });
}

/* ─── REVEAL ANIMATIONS ─── */
function initAnimations() {
    const targets = document.querySelectorAll(
        '.pillar-card, .stat-card, .course-card, .step-card, .law-card, .support-card, .checklist-card, .download-card, .conduct-item, .legal-card, .contact-card, .location-card, .section-header, .archbishop-content, .cta-container, .alert-box, .info-block'
    );

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, i) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.opacity    = '1';
                    entry.target.style.transform  = 'translateY(0) scale(1)';
                }, i * 60);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    targets.forEach(el => {
        el.style.opacity    = '0';
        el.style.transform  = 'translateY(28px) scale(0.97)';
        el.style.transition = 'opacity 0.65s cubic-bezier(0.22,1,0.36,1), transform 0.65s cubic-bezier(0.22,1,0.36,1)';
        observer.observe(el);
    });
}

/* ─── THREE.JS HERO CANVAS ─── */
function initHeroCanvas() {
    const canvas = document.getElementById('hero-canvas');
    if (!canvas || typeof THREE === 'undefined') return;

    const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    const scene  = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(60, canvas.clientWidth / canvas.clientHeight, 0.1, 1000);
    camera.position.z = 5;

    /* Particles */
    const COUNT = 120;
    const positions = new Float32Array(COUNT * 3);
    const velocities = [];

    for (let i = 0; i < COUNT; i++) {
        positions[i * 3]     = (Math.random() - 0.5) * 14;
        positions[i * 3 + 1] = (Math.random() - 0.5) * 8;
        positions[i * 3 + 2] = (Math.random() - 0.5) * 4;
        velocities.push({
            x: (Math.random() - 0.5) * 0.005,
            y: (Math.random() - 0.5) * 0.005,
        });
    }

    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.BufferAttribute(positions, 3));

    const mat = new THREE.PointsMaterial({
        color: 0xffffff,
        size: 0.06,
        transparent: true,
        opacity: 0.55,
        sizeAttenuation: true,
    });

    const points = new THREE.Points(geo, mat);
    scene.add(points);

    /* Connection lines */
    const lineMat = new THREE.LineBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.12 });
    const lineGeo = new THREE.BufferGeometry();
    const maxLines = COUNT * 3;
    const linePositions = new Float32Array(maxLines * 6);
    lineGeo.setAttribute('position', new THREE.BufferAttribute(linePositions, 3));
    const lines = new THREE.LineSegments(lineGeo, lineMat);
    scene.add(lines);

    function resizeCanvas() {
        const hero = canvas.parentElement;
        const w = hero.clientWidth, h = hero.clientHeight;
        renderer.setSize(w, h, false);
        camera.aspect = w / h;
        camera.updateProjectionMatrix();
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    /* Animate */
    function animate() {
        requestAnimationFrame(animate);

        const pos = geo.attributes.position.array;
        for (let i = 0; i < COUNT; i++) {
            pos[i * 3]     += velocities[i].x;
            pos[i * 3 + 1] += velocities[i].y;
            if (Math.abs(pos[i * 3])     > 7)  velocities[i].x *= -1;
            if (Math.abs(pos[i * 3 + 1]) > 4.5) velocities[i].y *= -1;
        }
        geo.attributes.position.needsUpdate = true;

        /* Update connection lines */
        let lineIdx = 0;
        const lp = lineGeo.attributes.position.array;
        const DIST = 2.8;

        for (let i = 0; i < COUNT && lineIdx < maxLines; i++) {
            for (let j = i + 1; j < COUNT && lineIdx < maxLines; j++) {
                const dx = pos[i*3]   - pos[j*3];
                const dy = pos[i*3+1] - pos[j*3+1];
                const dz = pos[i*3+2] - pos[j*3+2];
                const dist = Math.sqrt(dx*dx + dy*dy + dz*dz);
                if (dist < DIST) {
                    lp[lineIdx*6]   = pos[i*3];   lp[lineIdx*6+1] = pos[i*3+1]; lp[lineIdx*6+2] = pos[i*3+2];
                    lp[lineIdx*6+3] = pos[j*3];   lp[lineIdx*6+4] = pos[j*3+1]; lp[lineIdx*6+5] = pos[j*3+2];
                    lineIdx++;
                }
            }
        }
        lineGeo.setDrawRange(0, lineIdx * 2);
        lineGeo.attributes.position.needsUpdate = true;

        points.rotation.y += 0.0005;
        lines.rotation.y  += 0.0005;

        renderer.render(scene, camera);
    }
    animate();
}

/* ─── 3D CARD TILT ─── */
function initCardTilt() {
    const selector = [
        '.pillar-card',
        '.stat-card',
        '.course-card',
        '.step-card',
        '.law-card',
        '.support-card',
        '.checklist-card',
        '.download-card',
        '.conduct-item',
        '.legal-card',
        '.contact-card',
        '.location-card',
        '.info-block',
    ].join(', ');

    const cards = document.querySelectorAll(selector);

    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect   = card.getBoundingClientRect();
            const x      = e.clientX - rect.left;
            const y      = e.clientY - rect.top;
            const cx     = rect.width  / 2;
            const cy     = rect.height / 2;
            const tiltX  = ((y - cy) / cy) * -8;
            const tiltY  = ((x - cx) / cx) *  8;
            card.style.transform = `perspective(800px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) translateZ(6px)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(800px) rotateX(0) rotateY(0) translateZ(0)';
            card.style.transition = 'transform 0.5s cubic-bezier(0.22,1,0.36,1), box-shadow 0.3s ease';
        });

        card.addEventListener('mouseenter', () => {
            card.style.transition = 'box-shadow 0.3s ease';
        });
    });
}
