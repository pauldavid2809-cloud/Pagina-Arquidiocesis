import os
import re

dir_path = r"."

# ─── 1. REESCRIBIR styles.css COMPLETO ───────────────────────────────────────
new_css = """/* ═══════════════════════════════════════════════════════════════════════════
   Arquidiócesis de Maracaibo — Design System v2
   Paleta: Azur #003366 · Gualda #FFCC00 · Grana #B23A48 · Hueso #FAF8F4
   ═══════════════════════════════════════════════════════════════════════════ */

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600;700&family=Poppins:wght@700;800&display=swap');

:root {
  /* Colores */
  --primary:       #003366;
  --primary-dark:  #002244;
  --primary-light: #0a4a8f;
  --secondary:     #FFCC00;
  --secondary-dark:#e6b800;
  --danger:        #B23A48;
  --success:       #25D366;

  /* Neutros */
  --bg:            #FAF8F4;
  --bg-white:      #FFFFFF;
  --bg-dark:       #0d1b2a;
  --text:          #1a1a2e;
  --text-light:    #5a6478;
  --text-muted:    #9aa0ad;
  --border:        #e8e6e0;
  --border-light:  #f0eee9;

  /* Tipografía */
  --font-display:  'Cormorant Garamond', Georgia, serif;
  --font-body:     'Inter', system-ui, sans-serif;
  --font-accent:   'Poppins', sans-serif;

  /* Espaciado */
  --space-xs:  0.25rem;
  --space-sm:  0.5rem;
  --space-md:  1rem;
  --space-lg:  2rem;
  --space-xl:  4rem;
  --space-2xl: 8rem;

  /* Otros */
  --radius-sm:  6px;
  --radius-md:  12px;
  --radius-lg:  20px;
  --radius-xl:  32px;
  --shadow-sm:  0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
  --shadow-md:  0 4px 16px rgba(0,51,102,0.08), 0 2px 6px rgba(0,0,0,0.04);
  --shadow-lg:  0 12px 40px rgba(0,51,102,0.12), 0 4px 12px rgba(0,0,0,0.06);
  --shadow-xl:  0 24px 64px rgba(0,51,102,0.16);
  --transition: all 0.28s cubic-bezier(0.4, 0, 0.2, 1);
}

/* ─── Reset ──────────────────────────────────────────────────────────────── */
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; -webkit-font-smoothing: antialiased; }
body { font-family: var(--font-body); background: var(--bg); color: var(--text); line-height: 1.6; overflow-x: hidden; }
a { text-decoration: none; color: inherit; transition: var(--transition); }
ul { list-style: none; }
img { max-width: 100%; display: block; }

/* ─── Tipografía ─────────────────────────────────────────────────────────── */
h1, h2, h3, h4, h5 { font-family: var(--font-display); color: var(--primary); line-height: 1.15; font-weight: 600; }
h2 { font-size: clamp(2rem, 4vw, 3.2rem); }
h3 { font-size: clamp(1.4rem, 2.5vw, 2rem); }
h4 { font-size: clamp(1.1rem, 2vw, 1.4rem); }
p  { color: var(--text-light); line-height: 1.75; }

/* ─── Utilidades ─────────────────────────────────────────────────────────── */
.container   { width: 90%; max-width: 1200px; margin: 0 auto; }
.text-center { text-align: center; }
.mb-4        { margin-bottom: 2rem; }
.mt-2        { margin-top: 2rem; }
.py-4        { padding: 5rem 0; }
.bg-light    { background: var(--bg); }

/* ─── Botones ────────────────────────────────────────────────────────────── */
.btn {
  display: inline-flex; align-items: center; gap: 0.4rem;
  padding: 0.75rem 1.75rem; border-radius: 50px;
  font-family: var(--font-body); font-weight: 600; font-size: 0.9rem;
  border: 2px solid transparent; cursor: pointer;
  transition: var(--transition); white-space: nowrap;
}
.btn-primary {
  background: var(--secondary); color: var(--primary);
  box-shadow: 0 4px 14px rgba(255,204,0,0.35);
}
.btn-primary:hover {
  background: var(--secondary-dark);
  box-shadow: 0 6px 20px rgba(255,204,0,0.5);
  transform: translateY(-2px);
}
.btn-outline {
  background: transparent; color: white;
  border-color: rgba(255,255,255,0.5);
}
.btn-outline:hover { background: rgba(255,255,255,0.12); border-color: white; }
.btn-info {
  background: rgba(255,255,255,0.15); color: white;
  border-color: rgba(255,255,255,0.3); backdrop-filter: blur(8px);
}
.btn-info:hover { background: rgba(255,255,255,0.25); }
.btn-danger { background: var(--danger); color: white; }
.btn-danger:hover { background: #9e2f3c; transform: translateY(-2px); }

/* ─── Navbar ─────────────────────────────────────────────────────────────── */
.navbar {
  position: fixed; top: 0; width: 100%; z-index: 1000;
  padding: 0;
  background: transparent;
  transition: var(--transition);
}
.navbar.scrolled {
  background: rgba(255,255,255,0.97);
  backdrop-filter: blur(20px);
  box-shadow: 0 1px 0 var(--border), var(--shadow-sm);
}
.nav-container {
  display: flex; justify-content: space-between; align-items: center;
  width: 92%; max-width: 1400px; margin: 0 auto;
  padding: 1rem 0;
  transition: var(--transition);
}
.navbar.scrolled .nav-container { padding: 0.65rem 0; }

/* Logo */
.logo { display: flex; align-items: center; gap: 0.75rem; }
.logo img {
  height: 44px; width: 44px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
  transition: var(--transition);
}
.logo:hover img { transform: scale(1.05); }
.logo-text { display: flex; flex-direction: column; line-height: 1.1; }
.logo-text h1 {
  font-family: var(--font-accent);
  font-size: 0.95rem; font-weight: 800;
  color: var(--primary);
  letter-spacing: -0.01em;
  text-transform: uppercase;
}
.navbar:not(.scrolled) .logo-text h1 { color: white; }
.logo-text p {
  font-family: var(--font-accent);
  font-size: 0.72rem; font-weight: 700;
  color: var(--primary-light);
  letter-spacing: 0.05em;
  text-transform: uppercase;
}
.navbar:not(.scrolled) .logo-text p { color: rgba(255,255,255,0.75); }

/* Nav links */
.nav-links {
  display: flex; gap: 0.2rem; align-items: center;
}
.nav-links > a {
  font-weight: 500; font-size: 0.84rem;
  color: var(--text); padding: 0.45rem 0.75rem;
  border-radius: var(--radius-sm);
}
.navbar:not(.scrolled) .nav-links > a { color: rgba(255,255,255,0.88); }
.nav-links > a:hover { color: var(--primary); background: rgba(0,51,102,0.06); }
.navbar:not(.scrolled) .nav-links > a:hover { color: white; background: rgba(255,255,255,0.12); }

/* Dropdown */
.dropdown { position: relative; }
.dropbtn {
  background: none; border: none; cursor: pointer;
  font-family: var(--font-body); font-weight: 500; font-size: 0.84rem;
  color: var(--text); padding: 0.45rem 0.75rem; border-radius: var(--radius-sm);
  transition: var(--transition); display: flex; align-items: center; gap: 0.3rem;
}
.navbar:not(.scrolled) .dropbtn { color: rgba(255,255,255,0.88); }
.dropdown:hover .dropbtn,
.dropbtn:hover { color: var(--primary); background: rgba(0,51,102,0.06); }
.navbar:not(.scrolled) .dropdown:hover .dropbtn { color: white; background: rgba(255,255,255,0.12); }

.dropdown-content {
  display: none; position: absolute;
  top: calc(100% + 0.5rem); left: 50%; transform: translateX(-50%);
  background: var(--bg-white); min-width: 210px;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  border: 1px solid var(--border-light);
  padding: 0.4rem; z-index: 1001;
  animation: fadeDown 0.18s ease;
}
@keyframes fadeDown { from { opacity:0; transform: translateX(-50%) translateY(-8px); } to { opacity:1; transform: translateX(-50%) translateY(0); } }
.dropdown:hover .dropdown-content { display: block; }
.dropdown-content a {
  display: block; padding: 0.6rem 0.9rem;
  font-size: 0.84rem; font-weight: 500; color: var(--text);
  border-radius: var(--radius-sm); transition: var(--transition);
}
.dropdown-content a:hover { background: var(--bg); color: var(--primary); padding-left: 1.1rem; }

/* Botón donaciones */
.nav-links .btn-primary {
  font-size: 0.84rem; padding: 0.5rem 1.2rem;
  margin-left: 0.5rem;
}

/* Toggle móvil */
.menu-toggle {
  display: none; flex-direction: column; gap: 5px;
  background: transparent; border: none; cursor: pointer; padding: 0.3rem;
}
.menu-toggle span {
  width: 24px; height: 2.5px;
  background: var(--primary); border-radius: 2px;
  transition: var(--transition);
}
.navbar:not(.scrolled) .menu-toggle span { background: white; }

/* ─── Hero ───────────────────────────────────────────────────────────────── */
.hero {
  min-height: 100vh; position: relative;
  display: flex; align-items: center; justify-content: center;
  text-align: center; color: white;
  background: url('../img/inicio_bg.webp') no-repeat center center / cover;
}
.hero-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(
    170deg,
    rgba(0, 20, 51, 0.72) 0%,
    rgba(0, 40, 90, 0.60) 50%,
    rgba(0, 20, 51, 0.80) 100%
  );
}
/* Patrón decorativo sutil */
.hero-overlay::after {
  content: '';
  position: absolute; inset: 0;
  background-image: radial-gradient(circle at 20% 80%, rgba(255,204,0,0.08) 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, rgba(255,204,0,0.06) 0%, transparent 45%);
}
.hero-content {
  position: relative; z-index: 2;
  max-width: 820px; padding: 0 2rem;
}
.hero-eyebrow {
  display: inline-block;
  font-family: var(--font-body); font-size: 0.78rem; font-weight: 600;
  letter-spacing: 0.18em; text-transform: uppercase;
  color: var(--secondary); margin-bottom: 1.25rem;
  opacity: 0.9;
}
.hero-content h2 {
  font-family: var(--font-display);
  font-size: clamp(2.4rem, 5.5vw, 4rem);
  font-weight: 600; font-style: italic;
  color: white; line-height: 1.1;
  margin-bottom: 1.25rem;
  text-shadow: 0 2px 20px rgba(0,0,0,0.3);
}
.hero-content p {
  font-size: clamp(1rem, 2vw, 1.2rem);
  color: rgba(255,255,255,0.82);
  line-height: 1.7; margin-bottom: 2.5rem;
  font-weight: 300;
}
.hero-actions { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }

/* Scroll indicator */
.hero-scroll {
  position: absolute; bottom: 2rem; left: 50%; transform: translateX(-50%);
  display: flex; flex-direction: column; align-items: center; gap: 0.4rem;
  color: rgba(255,255,255,0.5); font-size: 0.7rem; letter-spacing: 0.12em;
  text-transform: uppercase; animation: bounce 2s infinite;
}
@keyframes bounce { 0%,100%{transform:translateX(-50%) translateY(0)} 50%{transform:translateX(-50%) translateY(6px)} }
.hero-scroll svg { width: 20px; opacity: 0.5; }

/* ─── Sección header ─────────────────────────────────────────────────────── */
.section-header { margin-bottom: 3rem; }
.section-label {
  display: inline-block; font-size: 0.72rem; font-weight: 700;
  letter-spacing: 0.14em; text-transform: uppercase; color: var(--danger);
  margin-bottom: 0.75rem;
}
.section-title {
  font-family: var(--font-display); font-size: clamp(1.8rem, 3.5vw, 2.6rem);
  color: var(--primary); margin-bottom: 0.75rem; font-weight: 600;
}
.section-subtitle { color: var(--text-light); font-size: 1.05rem; max-width: 560px; margin: 0 auto; }

/* Línea decorativa */
.section-title::after {
  content: '';
  display: block; width: 48px; height: 3px;
  background: var(--secondary); margin: 0.9rem auto 0;
  border-radius: 2px;
}
.text-center .section-title::after { margin-left: auto; margin-right: auto; }

/* ─── Grid de ejes ───────────────────────────────────────────────────────── */
.grid { display: grid; gap: 1.25rem; }
.axes-grid { grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); }

/* ─── Cards ──────────────────────────────────────────────────────────────── */
.glass-card {
  background: var(--bg-white);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 2rem 1.5rem;
  text-align: center;
  transition: var(--transition);
  box-shadow: var(--shadow-sm);
  position: relative; overflow: hidden;
}
.glass-card::before {
  content: ''; position: absolute;
  top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, var(--primary), var(--primary-light));
  opacity: 0; transition: var(--transition);
}
.glass-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-lg);
  border-color: transparent;
}
.glass-card:hover::before { opacity: 1; }
.glass-card.highlight {
  border: 2px solid var(--secondary);
  background: linear-gradient(135deg, #fffef5, #fff);
}
.glass-card.highlight::before { background: var(--secondary); opacity: 1; }
.glass-card.danger-card::before { background: var(--danger); opacity: 1; }

.card-img-circle {
  width: 72px; height: 72px; border-radius: 50%;
  object-fit: cover; margin: 0 auto 1.25rem;
  border: 3px solid var(--border-light);
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  background: var(--bg);
}
.glass-card h4 {
  font-family: var(--font-display); font-size: 1.2rem;
  color: var(--primary); margin-bottom: 0.5rem; font-weight: 600;
}
.glass-card p { font-size: 0.88rem; color: var(--text-light); line-height: 1.6; }

/* ─── Feature sections ───────────────────────────────────────────────────── */
.feature-section {
  display: flex; align-items: center;
  gap: 4rem; padding: 2rem 0;
}
.feature-section.reverse { flex-direction: row-reverse; }
.feature-text { flex: 1; }
.feature-text h2 {
  font-family: var(--font-display);
  font-size: clamp(1.8rem, 3vw, 2.5rem);
  margin-bottom: 1.25rem; font-weight: 600;
}
.feature-text p { font-size: 1rem; line-height: 1.8; margin-bottom: 1.25rem; }
.feature-image {
  flex: 1; border-radius: var(--radius-lg);
  overflow: hidden; box-shadow: var(--shadow-lg);
  position: relative;
}
.feature-image img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease; }
.feature-image:hover img { transform: scale(1.03); }
.feature-list { margin-top: 1.25rem; }
.feature-list li { margin-bottom: 0.6rem; font-weight: 600; color: var(--primary); }

/* ─── Page header (páginas internas) ────────────────────────────────────── */
.page-header {
  background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 60%, var(--primary-light) 100%);
  padding: 8rem 0 4rem; text-align: center; position: relative; overflow: hidden;
}
.page-header::before {
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(ellipse at 70% 50%, rgba(255,204,0,0.08) 0%, transparent 60%);
}
.page-header .container { position: relative; z-index: 1; }
.page-header h2 { color: white; font-family: var(--font-display); font-style: italic; }
.page-header p  { color: rgba(255,255,255,0.7); font-size: 1.05rem; margin-top: 0.5rem; }

/* ─── Footer ─────────────────────────────────────────────────────────────── */
.footer {
  background: var(--bg-dark);
  color: rgba(255,255,255,0.75);
  padding: 4rem 0 0;
}
.footer-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 3rem; margin-bottom: 3rem;
}
.footer h4 {
  font-family: var(--font-body); font-size: 0.78rem;
  font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase;
  color: var(--secondary); margin-bottom: 1.25rem;
}
.footer-info p { font-size: 0.88rem; line-height: 1.7; max-width: 280px; }
.footer-links ul li { margin-bottom: 0.6rem; }
.footer-links ul li a { font-size: 0.88rem; color: rgba(255,255,255,0.6); transition: var(--transition); }
.footer-links ul li a:hover { color: white; padding-left: 4px; }
.footer-social a { font-size: 0.88rem; color: rgba(255,255,255,0.6); }
.footer-social a:hover { color: var(--secondary); }
.footer-bottom {
  border-top: 1px solid rgba(255,255,255,0.08);
  padding: 1.5rem 0; text-align: center;
  font-size: 0.82rem; color: rgba(255,255,255,0.35);
  grid-column: 1 / -1; margin-top: 0;
}

/* ─── Animaciones ────────────────────────────────────────────────────────── */
.animate-fade-in-up {
  opacity: 0; transform: translateY(28px);
  animation: fadeInUp 0.7s cubic-bezier(0.4,0,0.2,1) forwards;
}
.delay-1 { animation-delay: 0.15s; }
.delay-2 { animation-delay: 0.3s; }
@keyframes fadeInUp { to { opacity:1; transform:translateY(0); } }

/* ─── Otros ──────────────────────────────────────────────────────────────── */
.pastoral-tags { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1.5rem; }
.pastoral-tags span {
  background: rgba(0,51,102,0.08); color: var(--primary);
  padding: 0.3rem 0.9rem; border-radius: 50px;
  font-size: 0.82rem; font-weight: 600; border: 1px solid rgba(0,51,102,0.12);
}
.warning-section { background: linear-gradient(135deg, var(--danger), #8b0000); color: white; }
.safe-env { border: 3px solid rgba(255,255,255,0.2); }

/* ─── Responsive ─────────────────────────────────────────────────────────── */
@media (max-width: 1100px) {
  .nav-links {
    position: fixed; top: 0; left: -100%; width: 80%; max-width: 320px;
    height: 100vh; background: var(--bg-white);
    flex-direction: column; justify-content: flex-start;
    align-items: flex-start; padding: 5rem 2rem 2rem;
    gap: 0.1rem; box-shadow: var(--shadow-xl);
    transition: left 0.3s ease;
  }
  .nav-links.active { left: 0; }
  .nav-links > a { width: 100%; padding: 0.75rem 1rem; font-size: 1rem; color: var(--text) !important; }
  .nav-links > a:hover { background: var(--bg); color: var(--primary) !important; }
  .nav-links .btn-primary { margin-left: 0; margin-top: 1rem; width: 100%; justify-content: center; }
  .dropdown-content { position: static; transform: none; box-shadow: none; border: none; background: var(--bg); animation: none; padding-left: 1rem; }
  .dropdown:hover .dropdown-content { display: block; }
  .dropbtn { width: 100%; justify-content: space-between; color: var(--text) !important; font-size: 1rem; padding: 0.75rem 1rem; }
  .menu-toggle { display: flex; }
  .feature-section, .feature-section.reverse { flex-direction: column; gap: 2rem; }
  .footer-grid { grid-template-columns: 1fr 1fr; }
  .hero-content h2 { font-size: 2.2rem; }
}
@media (max-width: 600px) {
  .axes-grid { grid-template-columns: repeat(2, 1fr); gap: 0.75rem; }
  .glass-card { padding: 1.25rem 1rem; }
  .hero-actions { flex-direction: column; align-items: center; }
  .footer-grid { grid-template-columns: 1fr; gap: 2rem; }
  .page-header { padding: 7rem 0 3rem; }
}
"""

css_path = os.path.join(dir_path, 'css', 'styles.css')
os.makedirs(os.path.join(dir_path, 'css'), exist_ok=True)
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(new_css)
print(f"  [✓] css/styles.css reescrito ({len(new_css)} chars)")

# ─── 2. MEJORAR EL HERO DEL index.html ───────────────────────────────────────
index_path = os.path.join(dir_path, 'index.html')
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        idx = f.read()

    # Reemplazar contenido del hero
    old_hero_content = '''        <h2 class="animate-fade-in-up">Encuentro, Transparencia y Servicio Pastoral</h2>
            <p class="animate-fade-in-up delay-1">Bienvenidos al portal web oficial de la Arquidiócesis de Maracaibo, una iglesia en salida para más de 2 millones de fieles zulianos.</p>
            <div class="hero-actions animate-fade-in-up delay-2">
                <a href="directorio.html" class="btn btn-primary">Buscar mi Parroquia</a>
                <a href="ambientes.html" class="btn btn-info">Ambientes Seguros</a>
            </div>'''

    new_hero_content = '''        <span class="hero-eyebrow animate-fade-in-up">Iglesia Particular de Maracaibo</span>
            <h2 class="animate-fade-in-up delay-1">Encuentro, Transparencia<br>y Servicio Pastoral</h2>
            <p class="animate-fade-in-up delay-2">Portal oficial de la Arquidiócesis de Maracaibo, una Iglesia en salida al encuentro de más de 2 millones de fieles zulianos.</p>
            <div class="hero-actions animate-fade-in-up delay-2">
                <a href="directorio.html" class="btn btn-primary">Buscar mi Parroquia</a>
                <a href="ambientes.html" class="btn btn-info">Ambientes Seguros</a>
            </div>
        <div class="hero-scroll">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
            Explorar
        </div>'''

    idx = idx.replace(old_hero_content, new_hero_content)

    # Mejorar sección header de ejes
    idx = idx.replace(
        '<h3 class="section-title">Ejes Pastorales y Administrativos</h3>\n            <p class="section-subtitle">Navegue por las distintas áreas de servicio que ofrecemos a nuestra comunidad</p>',
        '<span class="section-label">Nuestra Iglesia</span>\n            <h3 class="section-title">Ejes Pastorales y Administrativos</h3>\n            <p class="section-subtitle">Navegue por las distintas áreas de servicio que ofrecemos a nuestra comunidad</p>'
    )

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(idx)
    print(f"  [✓] index.html mejorado")
else:
    print(f"  [!] index.html no encontrado")

# ─── 3. ACTUALIZAR GOOGLE FONTS EN TODOS LOS HTML ────────────────────────────
old_fonts = 'https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap'
new_fonts = 'https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600;700&family=Poppins:wght@700;800&display=swap'

# También manejar versión con Poppins ya incluido
old_fonts_b = 'https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Poppins:wght@700&display=swap'

html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]
fonts_updated = 0
for filename in html_files:
    fp = os.path.join(dir_path, filename)
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    changed = False
    if old_fonts in c:
        c = c.replace(old_fonts, new_fonts)
        changed = True
    if old_fonts_b in c:
        c = c.replace(old_fonts_b, new_fonts)
        changed = True
    if changed:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        fonts_updated += 1

print(f"  [✓] Fuentes actualizadas en {fonts_updated} archivos HTML")

# ─── 4. MEJORAR LOGO EN TODOS LOS HTML ───────────────────────────────────────
# Patrón flexible para capturar la div del logo-text en cualquier variante
logo_pattern = re.compile(
    r'<div class="logo-text">.*?</div>',
    re.DOTALL
)
new_logo_div = (
    '<div class="logo-text">'
    '<h1>Arquidiócesis</h1>'
    '<p>de Maracaibo</p>'
    '</div>'
)

logos_updated = 0
for filename in html_files:
    fp = os.path.join(dir_path, filename)
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    new_c, n = logo_pattern.subn(new_logo_div, c)
    if n > 0:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_c)
        logos_updated += 1

print(f"  [✓] Logo normalizado en {logos_updated} archivos HTML")

print("""
╔══════════════════════════════════════════════════════╗
║  ✅  Diseño actualizado correctamente                ║
║                                                      ║
║  Cambios aplicados:                                  ║
║  • css/styles.css — sistema de diseño completo       ║
║  • Nuevas fuentes: Cormorant Garamond + Inter        ║
║    + Poppins (serif elegante + sans limpio)          ║
║  • Navbar transparente que se vuelve blanca          ║
║    al hacer scroll                                   ║
║  • Hero con eyebrow label + scroll indicator         ║
║  • Cards con hover más refinado                      ║
║  • Page headers con gradiente mejorado               ║
║  • Footer oscuro tipo editorial                      ║
║  • Logo normalizado en todos los HTML                ║
╚══════════════════════════════════════════════════════╝
""")
