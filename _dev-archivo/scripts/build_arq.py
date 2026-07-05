with open('priests_html.txt', 'r', encoding='utf-8') as f:
    priests_html = f.read()

html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arquidiócesis | Arquidiócesis de Maracaibo</title>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600;700&family=Poppins:wght@700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <!-- Navbar -->
    <header class="navbar" id="navbar">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <img src="img/logo-arquidiocesis.webp" alt="Escudo" onerror="this.src='https://placehold.co/44x44/003366/fff?text=A'">
                <div class="logo-text"><h1>Arquidiócesis</h1><p>de Maracaibo</p></div>
            </a>
            <button class="menu-toggle" id="menuToggle" aria-label="Abrir menú" aria-expanded="false">
                <span></span><span></span><span></span>
            </button>
            <nav class="nav-links" id="navLinks">
                <a href="arquidiocesis.html">Arquidiócesis</a>
                <a href="arzobispo.html">Arzobispo</a>
                <a href="pastoral.html">Pastoral</a>
                <a href="noticias.html">Noticias</a>
                <a href="directorio.html">Directorio Parroquial</a>
                <div class="dropdown">
                    <button class="dropbtn">Instituciones &#9662;</button>
                    <div class="dropdown-content">
                        <a href="seminario.html">Seminario</a>
                        <a href="vida-consagrada.html">Vida Consagrada</a>
                        <a href="cancilleria.html">Cancillería</a>
                        <a href="https://tribunaleclesiasticomaracaibo.org/" target="_blank">Tribunal Eclesiástico</a>
                    </div>
                </div>
                <a href="ambientes.html">Ambientes Seguros</a>
                <a href="donaciones.html" class="btn btn-primary">Donaciones</a>
            </nav>
        </div>
    </header>

    <section class="page-header">
        <div class="container animate-fade-in-up">
            <h2>Nuestra Arquidiócesis</h2>
            <p>Historia, curia y organización eclesial de la grey zuliana.</p>
        </div>
    </section>

    <main class="container py-4">

        <!-- Sección Iglesia Universal -->
        <section id="iglesia-universal" class="mb-4">
            <h3 class="section-title text-center mb-4">Iglesia Universal</h3>
            <div class="feature-section" style="align-items: center;">
                <div class="feature-text" style="text-align: left;">
                    <h4 style="color: var(--primary); margin-bottom: 1rem;">La Centralidad de Jesucristo</h4>
                    <p>La Iglesia Católica tiene como único centro y cabeza a Jesucristo, el Hijo de Dios. Todo nuestro actuar, organización y misión pastoral nacen del encuentro vivo con Él, buscando hacer presente el Reino de Dios en la sociedad.</p>
                    
                    <h4 style="color: var(--primary); margin-bottom: 1rem; margin-top: 1.5rem;">Una Iglesia Católica Universal</h4>
                    <p>Nuestra Arquidiócesis de Maracaibo no es una entidad aislada, sino una porción del Pueblo de Dios integrada plenamente a la Iglesia Católica Universal, unida en comunión de fe, sacramentos y disciplina.</p>
                    
                    <h4 style="color: var(--primary); margin-bottom: 1rem; margin-top: 1.5rem;">En Comunión con el Santo Padre</h4>
                    <p>Caminamos en estricta fidelidad y comunión con el Obispo de Roma, el Papa, Sucesor de San Pedro y Vicario de Jesucristo en la tierra. Él es el principio y fundamento perpetuo y visible de la unidad de la Iglesia.</p>
                    
                    <div style="margin-top: 2rem;">
                        <a href="https://www.vatican.va/" target="_blank" class="btn btn-primary" style="display: inline-block;">Sitio Web de la Santa Sede</a>
                    </div>
                </div>
                <div class="feature-image">
                    <img src="img/vaticano.jpg" alt="El Vaticano" onerror="this.src='https://placehold.co/600x400/003366/fff?text=Vaticano'">
                </div>
            </div>
        </section>

        <!-- Sección Historia -->
        <section id="historia" class="mb-4" style="margin-top: 4rem;">
            <h3 class="section-title text-center mb-4">Historia de la Arquidiócesis</h3>
            <div class="feature-section">
                <div class="feature-image">
                    <img src="img/catedral.jpg" alt="Catedral de Maracaibo" onerror="this.src='https://placehold.co/600x400/003366/fff?text=Catedral'">
                </div>
                <div class="feature-text">
                    <p>La historia de nuestra Iglesia local se remonta al 28 de julio de 1897, cuando el Papa León XIII erigió la antigua <strong>Diócesis del Zulia</strong>, separando su territorio de la Diócesis de Mérida. El 2 de enero de 1953, cambió su nombre a Diócesis de Maracaibo.</p>
                    <p>Gracias al profundo crecimiento en la fe y al dinamismo pastoral de la región occidental, el 30 de abril de 1966 el Papa San Pablo VI elevó la sede al rango de <strong>Arquidiócesis Metropolitana</strong>, siendo Monseñor Domingo Roa Pérez su primer Arzobispo.</p>
                    <p>Hoy en día, la Arquidiócesis congrega a cientos de miles de fieles y abarca una rica estructura parroquial, liderada por nuestro Arzobispo, impulsando la nueva evangelización y labor social en el estado Zulia.</p>
                </div>
            </div>
        </section>

        <!-- Sección Nuestra Patrona -->
        <section id="patrona" class="mb-4" style="margin-top: 4rem;">
            <h3 class="section-title text-center mb-4">Nuestra Patrona: Ntra. Sra. del Rosario de Chiquinquirá</h3>
            <div class="feature-section">
                <div class="feature-image">
                    <img src="img/la_chinita.jpg" alt="Nuestra Patrona" onerror="this.src='https://placehold.co/600x800/003366/fff?text=La+Chinita'">
                </div>
                <div class="feature-text">
                    <p>La venerada imagen de <strong>Nuestra Señora del Rosario de Chiquinquirá</strong>, cariñosamente llamada "La Chinita", es el corazón espiritual del Zulia y Patrona indiscutible de nuestra Arquidiócesis.</p>
                    <p>Cuenta la historia que en 1709, en las orillas del Lago de Maracaibo, una humilde mujer encontró una pequeña tabla que llevó a su casa. Días después, el 18 de noviembre, escuchó unos golpes que provenían del cuarto donde había colgado la tabla. Al asomarse, la vivienda se llenó de un gran resplandor: en la madera se había dibujado nítidamente la imagen de la Virgen de Chiquinquirá.</p>
                    <p>Desde aquel milagro de la renovación, hace más de tres siglos, la Basílica Santuario alberga la Reliquia, siendo centro de peregrinación continua y manifestación del profundo fervor mariano de todo el pueblo zuliano.</p>
                </div>
            </div>
        </section>

        <!-- Sección Territorio -->
        <section id="territorio" class="mb-4" style="margin-top: 4rem;">
            <h3 class="section-title text-center mb-4">Nuestro Territorio</h3>
            <div class="feature-section" style="flex-direction: row-reverse;">
                <div class="feature-image" style="background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                    <img src="img/mapa_arquidiocesis.webp" alt="Mapa de la Arquidiócesis" onerror="this.src='https://placehold.co/800x600/e6e6e6/999?text=Mapa+de+la+Arquidiocesis'">
                </div>
                <div class="feature-text">
                    <p>La Arquidiócesis de Maracaibo abarca un vasto y diverso territorio que incluye los municipios Maracaibo, San Francisco, Jesús Enrique Lossada, Mara, Almirante Padilla, y La Cañada de Urdaneta.</p>
                    <p>Nuestro <strong>pueblo fiel</strong> se caracteriza por una profunda devoción mariana, alegría inconfundible y un fuerte apego a sus tradiciones. Es un pueblo diverso que incluye zonas urbanas, rurales y asentamientos de nuestros hermanos de las etnias indígenas, especialmente la Wayúu y Añú, enriqueciendo nuestra pastoral con su cultura milenaria.</p>
                    <p>Caminamos juntos como una Iglesia sinodal, buscando llegar a todas las periferias y llevando la buena noticia del Evangelio a cada hogar zuliano.</p>
                </div>
            </div>
        </section>

        <!-- Sección Organización -->
        <section id="organizacion" style="margin-top: 4rem;">
            <h3 class="section-title text-center mb-4">Estructura y Organización</h3>
            
            <div class="grid axes-grid">
                <!-- Gobierno y Vicarios -->
                <div class="card glass-card" style="text-align: left; padding: 2rem; grid-column: 1 / -1;">
                    <h4 style="margin-bottom: 1.5rem; border-bottom: 2px solid var(--secondary); padding-bottom: 0.5rem; text-align: left;">Vicarios Episcopales</h4>
                    <ul class="feature-list" style="margin-top: 0; padding-left: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.25rem 1rem;">
                        <li style="list-style: none;"><strong>Vicario General:</strong><br><span style="color: var(--text-light); font-weight: normal;">Pbro. Jesús Enrique Hernández</span></li>
                        <li style="list-style: none;"><strong>Vic. Episcopal Maracaibo-Oeste:</strong><br><span style="color: var(--text-light); font-weight: normal;">Pbro. Jesús Sandoval</span></li>
                        <li style="color: #999; font-weight: normal; list-style: none; font-size: 0.85rem;"><em>(Añadir otros vicarios territoriales y funcionales según aplique)</em></li>
                    </ul>
                </div>

                <!-- Sacerdotes Incardinados -->
                <div class="card glass-card" style="text-align: left; padding: 2rem; grid-column: 1 / -1; margin-top: 2rem;">
                    <h4 style="margin-bottom: 1rem; border-bottom: 2px solid var(--secondary); padding-bottom: 0.5rem; text-align: left;">Sacerdotes Incardinados</h4>
                    <p style="font-size: 0.95rem; margin-bottom: 1rem;">Listado oficial de sacerdotes incardinados al servicio de la Arquidiócesis de Maracaibo.</p>
                    <ul class="feature-list" style="margin-top: 0; padding-left: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1rem;">
{priests_html}
                    </ul>
                </div>
            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container footer-grid">
            <div class="footer-info">
                <h4>Arquidiócesis de Maracaibo</h4>
                <p>Av. 4 con calle 95, frente a la Plaza Bolívar. Maracaibo, Estado Zulia.</p>
            </div>
            <div class="footer-links">
                <h4>Enlaces Rápidos</h4>
                <ul>
                    <li><a href="directorio.html">Directorio de Parroquias</a></li>
                    <li><a href="ambientes.html">Ambientes Seguros</a></li>
                    <li><a href="cancilleria.html">Cancillería</a></li>
                </ul>
            </div>
            <div class="footer-social">
                <h4>Síguenos</h4>
                <a href="#" aria-label="Instagram">@arquimcbo</a>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Arquidiócesis de Maracaibo. Todos los derechos reservados.</p>
        </div>
    </footer>
    <script src="js/app.js"></script>
</body>
</html>
"""

with open('arquidiocesis.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("arquidiocesis.html rebuilt successfully.")
