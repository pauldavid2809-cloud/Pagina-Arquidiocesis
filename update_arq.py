with open('arquidiocesis.html', 'r', encoding='utf-8') as f:
    content = f.read()

with open('priests_html.txt', 'r', encoding='utf-8') as f:
    priests_html = f.read()

# 1. Iglesia Universal
iglesia_universal = """
        <!-- Sección Iglesia Universal -->
        <section id="iglesia-universal" class="mb-4">
            <h3 class="section-title text-center mb-4">Iglesia Universal</h3>
            <div class="feature-section" style="align-items: center;">
                <div class="feature-text" style="text-align: left;">
                    <h4 style="color: var(--color-primary); margin-bottom: 1rem;">La Centralidad de Jesucristo</h4>
                    <p>La Iglesia Católica tiene como único centro y cabeza a Jesucristo, el Hijo de Dios. Todo nuestro actuar, organización y misión pastoral nacen del encuentro vivo con Él, buscando hacer presente el Reino de Dios en la sociedad.</p>
                    
                    <h4 style="color: var(--color-primary); margin-bottom: 1rem; margin-top: 1.5rem;">Una Iglesia Católica Universal</h4>
                    <p>Nuestra Arquidiócesis de Maracaibo no es una entidad aislada, sino una porción del Pueblo de Dios integrada plenamente a la Iglesia Católica Universal, unida en comunión de fe, sacramentos y disciplina.</p>
                    
                    <h4 style="color: var(--color-primary); margin-bottom: 1rem; margin-top: 1.5rem;">En Comunión con el Santo Padre</h4>
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
"""

# 2. Nuestra Patrona
patrona = """
        <!-- Sección Nuestra Patrona -->
        <section id="patrona" class="mb-4" style="margin-top: 4rem;">
            <h3 class="section-title text-center mb-4">Nuestra Patrona: Ntra. Sra. del Rosario de Chiquinquirá</h3>
            <div class="feature-section">
                <div class="feature-image">
                    <img src="https://placehold.co/600x800/e6e6e6/999?text=La+Chinita" alt="Nuestra Patrona" onerror="this.src='https://placehold.co/600x800/e6e6e6/999?text=Virgen+de+Chiquinquira'">
                </div>
                <div class="feature-text">
                    <p>La venerada imagen de <strong>Nuestra Señora del Rosario de Chiquinquirá</strong>, cariñosamente llamada "La Chinita", es el corazón espiritual del Zulia y Patrona indiscutible de nuestra Arquidiócesis.</p>
                    <p>Cuenta la historia que en 1709, en las orillas del Lago de Maracaibo, una humilde mujer encontró una pequeña tabla que llevó a su casa. Días después, el 18 de noviembre, escuchó unos golpes que provenían del cuarto donde había colgado la tabla. Al asomarse, la vivienda se llenó de un gran resplandor: en la madera se había dibujado nítidamente la imagen de la Virgen de Chiquinquirá.</p>
                    <p>Desde aquel milagro de la renovación, hace más de tres siglos, la Basílica Santuario alberga la Reliquia, siendo centro de peregrinación continua y manifestación del profundo fervor mariano de todo el pueblo zuliano.</p>
                </div>
            </div>
        </section>
"""

# 3. Territorio
territorio = """
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
"""

# Priest list HTML block to append in Organizacion
priests_block = f"""
                <!-- Sacerdotes Incardinados -->
                <div class="card glass-card" style="text-align: left; padding: 2rem; grid-column: 1 / -1;">
                    <h4 style="margin-bottom: 1rem; border-bottom: 2px solid var(--color-secondary); padding-bottom: 0.5rem; text-align: left;">Sacerdotes Incardinados</h4>
                    <p style="font-size: 0.95rem; margin-bottom: 1rem;">Listado oficial de sacerdotes incardinados al servicio de la Arquidiócesis de Maracaibo.</p>
                    <ul class="feature-list" style="margin-top: 0; padding-left: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1rem;">
{priests_html}
                    </ul>
                </div>
"""

# Insert at specific markers
content = content.replace('<!-- Sección Historia -->', iglesia_universal + '\n<!-- Sección Historia -->')
content = content.replace('<!-- Sección Organización -->', patrona + '\n' + territorio + '\n<!-- Sección Organización -->')
content = content.replace('</div>\n        </section>', priests_block + '            </div>\n        </section>')

with open('arquidiocesis.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated arquidiocesis.html")
