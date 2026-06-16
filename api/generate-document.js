export default async function handler(req, res) {
  // CORS configuration
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,DELETE,PATCH,POST,PUT,OPTIONS');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version, Authorization'
  );

  // Respond to preflight OPTIONS request
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  let body = {};
  if (typeof req.body === 'string') {
    try {
      body = JSON.parse(req.body);
    } catch (e) {
      return res.status(400).json({ error: 'Invalid JSON body' });
    }
  } else {
    body = req.body || {};
  }

  const { priestName, parish, reqType, details, status, feedback } = body;

  if (!priestName || !reqType || !status || !feedback) {
    return res.status(400).json({ 
      error: 'Missing required parameters. Required: priestName, reqType, status, feedback' 
    });
  }

  const groqKey = process.env.GROQ_API_KEY;

  // Formatting date in Spanish
  const today = new Date();
  const options = { day: 'numeric', month: 'long', year: 'numeric' };
  const dateStr = today.toLocaleDateString('es-ES', options);

  if (!groqKey) {
    // Return a beautiful static template fallback if Groq Key is not configured (e.g. local development)
    console.warn('GROQ_API_KEY no configurada. Usando plantilla de respaldo.');
    let fallbackText = '';
    
    if (status === 'Aprobado') {
      if (reqType === "Licencia Ministerial") {
        fallbackText = `DECRETO ARZOBISPAL Nº 082/2026\n\nMaracaibo, ${dateStr}\n\nPor cuanto el reverendo presbítero ${priestName} goza del aprecio doctrinal, pastoral y moral en nuestra Arquidiócesis de Maracaibo, desempeñando actualmente su ministerio en la ${parish || 'jurisdicción diocesana'}.\n\nPor las presentes letras y en virtud de nuestras facultades ordinarias, CONCEDEMOS a dicho presbítero la prórroga de su LICENCIA MINISTERIAL por el período de un año fiscal, facultándole para la celebración pública del Santo Sacrificio de la Eucaristía, la predicación de la Palabra de Dios y la administración de los sacramentos litúrgicos correspondientes a su ministerio pastoral, en conformidad con las normas de la Iglesia Católica y las disposiciones locales.\n\nNotivos de la concesión: ${feedback}\n\nNotifíquese a los interesados.\n\nMons. José Luis Azuaje Ayala, Arzobispo Metropolitano.`;
      } else if (reqType.includes("Celebret") || reqType.includes("Idoneidad")) {
        fallbackText = `CERTIFICADO DE IDONEIDAD MINISTERIAL (CELEBRET)\n\nMaracaibo, ${dateStr}\n\nLa Curia Metropolitana de la Arquidiócesis de Maracaibo certifica por la presente que el reverendo presbítero ${priestName} es sacerdote ordenado en comunión con la Sede Apostólica y con el Arzobispado metropolitano.\n\nEl mencionado presbítero goza de una conducta moral intachable y está plenamente autorizado para ejercer las funciones ministeriales y los sacramentos en el territorio de su jurisdicción, no teniendo ningún impedimento canónico para la celebración del culto divino.\n\nJustificación: ${feedback}\n\nRecomendamos fraternalmente su acogida litúrgica a las autoridades eclesiásticas del lugar adonde se traslada temporalmente.\n\nMons. José Luis Azuaje Ayala, Arzobispo Metropolitano.`;
      } else {
        fallbackText = `RESOLUCIÓN ARZOBISPAL\n\nMaracaibo, ${dateStr}\n\nEn atención a la solicitud presentada por el presbítero ${priestName} adscrito a la ${parish || 'jurisdicción diocesana'}, referente a la solicitud de: "${reqType}".\n\nEste Arzobispado metropolitano, oído el parecer del Ordinario del lugar y habiendo cumplido con los requerimientos exigidos, CONCEDE la autorización oficial correspondiente para el fin descrito en su solicitud, fundamentado en: "${feedback}".\n\nDado para fe pública de lo decretado.\n\nMons. José Luis Azuaje Ayala, Arzobispo Metropolitano.`;
      }
    } else {
      fallbackText = `RESOLUCIÓN DE CANCILLERÍA\n\nMaracaibo, ${dateStr}\n\nEn relación con la solicitud de "${reqType}" interpuesta por el presbítero ${priestName} adscrito a la ${parish || 'jurisdicción diocesana'}.\n\nEsta Curia Metropolitana, habiendo evaluado detenidamente los recaudos y las circunstancias pastorales actuales, lamenta informar que no es posible conceder la solicitud en esta oportunidad, debido a los siguientes motivos:\n\n"${feedback}"\n\nSe exhorta al solicitante a continuar su abnegada labor pastoral y a coordinar con el Vicario General las medidas conducentes para solventar los requerimientos indicados.\n\nEn la caridad pastoral,\n\nCancillería Metropolitana de Maracaibo.`;
    }

    return res.status(200).json({ 
      success: true, 
      documentText: fallbackText, 
      warning: 'Fallback static template used (GROQ_API_KEY environment variable is missing).' 
    });
  }

  try {
    const prompt = `Actúa como el Canciller de la Arquidiócesis de Maracaibo. Tu tarea es redactar el texto de un documento eclesiástico oficial (decreto, certificado o resolución) emitido por el Arzobispo Metropolitano, Excmo. Mons. José Luis Azuaje Ayala, en respuesta a una solicitud de un sacerdote o parroquia.

Información de la Solicitud:
- Sacerdote/Solicitante: ${priestName}
- Parroquia/Lugar de origen: ${parish || 'Diócesis de Maracaibo'}
- Tipo de Trámite: ${reqType}
- Motivo original/detalles indicados por el solicitante: "${details || 'No especificados'}"
- Decisión de la Curia: ${status === 'Aprobado' ? 'APROBADO' : 'RECHAZADO'}
- Justificación/Motivos del Canciller para esta resolución: "${feedback}"

Pautas de redacción eclesiástica:
1. Usa un tono extremadamente formal, solemne, canónico y pastoral.
2. Si la decisión es APROBADO:
   - Para "Licencia Ministerial": Estructura como DECRETO ARZOBISPAL (ej: DECRETO ARZOBISPAL Nº [Generar número correlativo ficticio]/2026). Debe contener considerandos ("Por cuanto..."), la concesión de facultades específicas (celebrar Eucaristía, predicar, administrar sacramentos en la jurisdicción) por un plazo determinado (un año), e incorporar de forma fluida y formal el motivo de aprobación indicado: "${feedback}". Firma Mons. José Luis Azuaje Ayala, Arzobispo Metropolitano.
   - Para "Celebret" o "Idoneidad": Estructura como CERTIFICADO DE IDONEIDAD MINISTERIAL (CELEBRET). Certifica que el sacerdote está en plena comunión, goza de buena conducta, no tiene impedimentos canónicos y recomiéndalo a otros obispos.
   - Para otros trámites: Estructura como RESOLUCIÓN ARZOBISPAL formal concediendo lo solicitado basándote en los motivos indicados.
3. Si la decisión es RECHAZADO:
   - Estructura como RESOLUCIÓN DE CANCILLERÍA formal. Explica con firmeza e institucionalidad pero manteniendo la caridad pastoral que, tras la evaluación y por las razones justificadas ("${feedback}"), la solicitud no ha sido concedida en esta oportunidad. Firma el despacho de la Cancillería Metropolitana.
4. Usa fórmulas tradicionales solemnes de la Iglesia Católica: "Dada en el Arzobispado de Maracaibo...", "Notifíquese a los interesados...", "Para fe pública de lo decretado...".
5. Coloca la fecha del documento como: "Maracaibo, ${dateStr}".
6. Devuelve ÚNICAMENTE el texto limpio del documento eclesiástico redactado. No agregues formato markdown, bloques de código (como \`\`\` o \`\`\`text), preámbulos ni notas aclaratorias. El resultado debe ser texto plano listo para ser cargado y editado en la caja de texto.`;

    const groqResponse = await fetch('https://api.groq.com/openai/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${groqKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        model: 'llama-3.1-8b-instant',
        messages: [{ role: 'user', content: prompt }],
        temperature: 0.3
      })
    });

    if (!groqResponse.ok) {
      const errorData = await groqResponse.json().catch(() => ({}));
      return res.status(groqResponse.status).json({ 
        error: 'Groq API error', 
        details: errorData 
      });
    }

    const groqData = await groqResponse.json();
    let documentText = groqData.choices?.[0]?.message?.content || '';
    
    // Clean up potential markdown code fences wrapped by LLM
    documentText = documentText.trim();
    if (documentText.startsWith('```')) {
      documentText = documentText.replace(/^```[a-zA-Z]*\n/, '').replace(/\n```$/, '');
    }

    return res.status(200).json({ 
      success: true, 
      documentText: documentText.trim() 
    });

  } catch (error) {
    return res.status(500).json({ 
      error: 'Failed to generate document via Groq', 
      details: error.message 
    });
  }
}
