// Validación de certificados emitidos por los sistemas de las parroquias.
// Cada parroquia tiene su propia base de datos; aquí solo se consulta la función
// pública de verificación (no da acceso a los libros ni a las actas escaneadas).
// La clave "publishable" es pública por diseño: solo permite llamar esa función.
const PARROQUIAS_CERTIFICADOS = [
    {
        prefijo: /^SB[0-9A-F]{20}$/,
        nombre: 'Parroquia San Benito de Palermo',
        supabaseUrl: 'https://zanbuungsgmsdirhqxcg.supabase.co',
        clave: 'sb_publishable__Au-6CN5Qn9wVpBmLrBP-g_6sLI4M9p',
        rpc: 'parroquia_verificar_certificado',
    },
];

function parroquiaDelCodigo(codigo) {
    const limpio = (codigo || '').trim().toUpperCase();
    return PARROQUIAS_CERTIFICADOS.find(p => p.prefijo.test(limpio)) || null;
}

async function consultarCertificadoParroquial(parroquia, codigo) {
    const res = await fetch(`${parroquia.supabaseUrl}/rest/v1/rpc/${parroquia.rpc}`, {
        method: 'POST',
        headers: { apikey: parroquia.clave, 'Content-Type': 'application/json' },
        body: JSON.stringify({ p_token: codigo.trim().toUpperCase() }),
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return res.json();
}

const escHtml = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

const MESES_LARGOS = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];
function fechaLargaParroquial(iso) {
    if (!iso) return '';
    const [a, m, d] = String(iso).slice(0, 10).split('-').map(Number);
    if (!a) return escHtml(iso);
    if (!m) return `${a}`;
    if (!d) return `${MESES_LARGOS[m - 1]} de ${a}`;
    return `${d} de ${MESES_LARGOS[m - 1]} de ${a}`;
}

async function validarCertificadoParroquial(parroquia, codigo) {
    const resultDiv = document.getElementById('validation-result');
    let r;
    try {
        r = await consultarCertificadoParroquial(parroquia, codigo);
    } catch (e) {
        console.error('Error al consultar la parroquia:', e);
        showInvalidDocument('No se pudo consultar el registro parroquial en este momento. Revise su conexión e intente de nuevo.');
        return;
    }

    if (!r) {
        showInvalidDocument(`El código <strong>${escHtml(codigo)}</strong> no corresponde a ningún certificado emitido por la ${escHtml(parroquia.nombre)}. No acepte este documento.`);
        return;
    }

    if (r.estado === 'vencido') {
        resultDiv.innerHTML = `
            <div class="validation-card overflow-hidden">
                <div class="invalid-badge p-6 flex items-center justify-center gap-3 font-label font-bold text-[16px] uppercase tracking-wider">
                    <i class="ti ti-clock-x text-[24px]"></i> Vencido
                </div>
            </div>`;
        return;
    }

    const a = r.acta || {};
    const p = a.persona || {};
    const esNina = p.sexo === 'F';
    const dato = (etiqueta, valor) => `
        <div class="py-2.5 border-b border-slate-100">
            <span class="text-[10px] uppercase font-bold tracking-wider text-slate-400 block">${etiqueta}</span>
            <div class="text-[14px] text-slate-900 mt-0.5">${valor || '—'}</div>
        </div>`;
    const notas = (a.notasMarginales || []).length
        ? `<ul class="space-y-1.5 text-[13px] text-slate-800">${a.notasMarginales.map(n =>
            `<li><strong>${escHtml(n.tipo)}:</strong> ${escHtml(n.contenido)}${n.parroquiaOrigen ? ` <span class="text-slate-500">(${escHtml(n.parroquiaOrigen)})</span>` : ''}</li>`).join('')}</ul>`
        : '<p class="text-[13px] text-slate-600 italic">No consta ninguna nota marginal.</p>';

    resultDiv.innerHTML = `
        <div class="validation-card overflow-hidden">
            <div class="verified-badge px-6 py-4 flex items-center justify-center gap-2.5 font-label font-bold text-[13px] uppercase tracking-[0.15em]">
                <i class="ti ti-rosette-discount-check text-[20px]"></i> Fe de Bautismo auténtica y vigente
            </div>
            <div class="p-6 md:p-8 space-y-6">
                <p class="text-center text-[13px] text-slate-600">
                    Emitida el ${fechaLargaParroquial(r.emitidoEn)} · <strong>válida hasta el ${fechaLargaParroquial(r.venceEn)}</strong>
                </p>
                <div>
                    <span class="text-[10px] uppercase font-bold tracking-wider text-slate-400 block">${esNina ? 'Bautizada' : 'Bautizado'}</span>
                    <h2 class="font-display text-[26px] font-bold text-crimson-deep leading-tight">${escHtml(p.nombres)} ${escHtml(p.apellidos)}</h2>
                    ${p.cedula ? `<p class="text-[12px] font-mono text-slate-500 mt-1">C.I. ${escHtml(p.cedula)}</p>` : ''}
                </div>
                <div class="grid md:grid-cols-2 gap-x-6">
                    ${dato(esNina ? 'Nacida' : 'Nacido', `${escHtml(p.lugarNacimiento)}${p.fechaNacimiento ? `, ${fechaLargaParroquial(p.fechaNacimiento)}` : ''}`)}
                    ${dato('Fecha de bautismo', fechaLargaParroquial(a.fechaBautismo))}
                    ${dato('Padre', escHtml(a.padreNombre))}
                    ${dato('Madre', escHtml(a.madreNombre))}
                    ${dato('Padrino', escHtml(a.padrino))}
                    ${dato('Madrina', escHtml(a.madrina))}
                    ${dato('Ministro', escHtml(a.ministro))}
                    ${dato('Libro · Folio · Acta', `${escHtml(a.libro)} · ${escHtml(a.folio)} · ${escHtml(a.acta)}`)}
                    ${r.fines ? dato('Expedida para fines de', escHtml(r.fines)) : ''}
                    ${r.parroco ? dato('Certifica', `${escHtml(r.parroco.nombre)}, ${escHtml(r.parroco.titulo)}`) : ''}
                </div>
                <div class="rounded-xl bg-[#7A1A22]/[0.04] border border-[#7A1A22]/15 p-4">
                    <span class="text-[10px] uppercase font-bold tracking-wider text-[#7A1A22] block mb-1.5">Notas marginales</span>
                    ${notas}
                </div>
                <p class="text-[12px] text-slate-500 text-center">
                    Compare estos datos con el documento impreso. Si no coinciden, el documento fue alterado.
                </p>
                <div class="text-center text-[11px] text-slate-400 font-mono">
                    ${escHtml(parroquia.nombre)} · Código ${escHtml(codigo.trim().toUpperCase())}
                </div>
            </div>
        </div>`;
}
