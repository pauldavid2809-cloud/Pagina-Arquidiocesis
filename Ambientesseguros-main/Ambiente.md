import os

# Content for the Markdown file
md_content = """# Instrucciones para la Creación de la Página de Ambientes Seguros
## Arquidiócesis de Maracaibo

Este documento define la estructura, contenido y diseño necesarios para implementar el portal de la **Comisión Arquidiocesana para la Promoción de Ambientes Seguros**, tomando como referencia el modelo de excelencia de la Archidiócesis de Chicago y el enfoque pastoral de la Archidiócesis de Madrid.

---

## 1. Concepto General
- **Objetivo:** Crear un espacio digital transparente, seguro y accesible que centralice la prevención de abusos, la formación de agentes de pastoral y la atención a víctimas.
- **Dominio Sugerido:** `ambientesseguros.arquidiocesisdemaracaibo.org` o un apartado destacado en `arquidiocesisdemaracaibo.org/ambientes-seguros`.
- **Idioma:** Español (con opción a traducción simplificada de protocolos clave).

## 2. Estructura de Navegación (Site Map)

### A. Inicio (Home)
- **Banner de Emergencia:** Botón rojo de alto contraste: **"DENUNCIAR UN ABUSO / REPORTAR PREOCUPACIÓN"**.
- **Mensaje del Arzobispo:** Breve video o carta de Mons. José Luis Azuaje reafirmando el compromiso de "Tolerancia Cero".
- **Cuatro Pilares de Acceso Rápido:**
  1. **Víctimas y Supervivientes:** "¿Necesitas ayuda o ser escuchado?".
  2. **Padres y Familias:** "Cómo proteger a tus hijos en la parroquia y el hogar".
  3. **Voluntarios y Empleados:** "Requisitos de cumplimiento y formación".
  4. **Clero y Religiosos:** "Protocolos y Código de Ética".

### B. Área de Denuncia y Asistencia (Prioridad 1)
- **Protocolo de denuncia:** Pasos claros (Llamar a las autoridades civiles primero - LOPNA/Ministerio Público).
- **Línea de Ayuda:** Número telefónico directo y correo electrónico de la Comisión.
- **Asistencia a Víctimas:** Descripción del equipo multidisciplinario (psicológico, jurídico y espiritual).

### C. Formación y Prevención (Compliance)
- **Sistema de Formación:** Enlace a talleres (presenciales o virtuales) sobre el buen trato.
- **Requisitos para Voluntarios:** Lista de verificación (Cédula, Antecedentes Penales, Taller de Ambientes Seguros).
- **Material Didáctico:** Guías descargables para catequistas y docentes.

### D. Marco Legal y Documentación
- **Protocolo CEV:** "Protocolo para la Prevención de Abusos" de la Conferencia Episcopal Venezolana.
- **Código de Conducta:** Normas específicas para el trato con menores en Maracaibo.
- **Leyes Nacionales:** Enlace y resumen de la LOPNA y leyes contra la violencia de género.

## 3. Especificaciones Técnicas y de Diseño
- **Diseño Móvil:** El 80% de los usuarios en Venezuela accederán vía móvil; el sitio debe ser ligero y 100% responsivo.
- **Privacidad:** Formulario de contacto cifrado (SSL) para proteger la identidad de quienes reporten.
- **Iconografía:** Uso de iconos amigables y profesionales (evitar imágenes de archivo genéricas; preferir arte eclesial local o infografías claras).

## 4. Hoja de Ruta de Implementación
1. **Fase 1 (Diseño):** Wireframe basado en el modelo de Chicago adaptado a Maracaibo.
2. **Fase 2 (Contenido):** Redacción de textos por parte de la Comisión (Alberto Sobalvarro y equipo).
3. **Fase 3 (Lanzamiento):** Campaña de difusión en todas las parroquias mediante códigos QR en las carteleras parroquiales.

---
*Documento preparado como guía técnica para la Comisión de Ambientes Seguros - Arquidiócesis de Maracaibo.*
"""

# Save the content to a file
file_path = '/mnt/data/instrucciones_pagina_ambientes_seguros_maracaibo.md'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(md_content)

print(f"File created at: {file_path}")