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

  const { to, subject, html, attachments } = body;

  if (!to || !subject || !html) {
    return res.status(400).json({ error: 'Missing parameters: to, subject, and html are required' });
  }

  const resendApiKey = process.env.RESEND_API_KEY;

  // If no API key is configured, emulate success for local development and testing
  if (!resendApiKey) {
    console.log('--- ENVIO DE EMAIL EMULADO (RESEND_API_KEY no configurada) ---');
    console.log(`Para: ${to}`);
    console.log(`Asunto: ${subject}`);
    console.log(`Adjuntos: ${attachments ? attachments.map(a => a.filename).join(', ') : 'Ninguno'}`);
    console.log(`Contenido HTML: ${html}`);
    console.log('------------------------------------------------------------');
    return res.status(200).json({
      success: true,
      message: 'Email emulado con éxito. (Configura RESEND_API_KEY en tu entorno para envío real)',
      emulated: true
    });
  }

  try {
    const payload = {
      from: 'Cancillería Arquidiocesana <cancilleria@arquidiocesisdemaracaibo.org>',
      to: [to],
      subject: subject,
      html: html
    };

    if (attachments && attachments.length > 0) {
      payload.attachments = attachments;
    }

    const response = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${resendApiKey}`
      },
      body: JSON.stringify(payload)
    });

    const data = await response.json().catch(() => ({}));

    if (!response.ok) {
      // Check for Resend restrictions (e.g., using a domain not yet verified, which triggers 403 or requires onboarding@resend.dev)
      if (response.status === 403 || (data.message && data.message.includes('onboarding@resend.dev'))) {
        console.warn('Fallo con dominio personalizado, reintentando con onboarding@resend.dev...');
        
        const retryPayload = {
          from: 'Cancillería <onboarding@resend.dev>',
          to: [to],
          subject: `[Test] ${subject}`,
          html: `<div style="padding: 10px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; margin-bottom: 20px; font-family: sans-serif; color: #856404;">
                  <strong>Nota de Desarrollo:</strong> Este correo se envió usando la cuenta de pruebas de Resend (onboarding@resend.dev). Para usar la dirección oficial, debes verificar tu dominio en el panel de Resend.
                 </div>
                 ${html}`
        };

        if (attachments && attachments.length > 0) {
          retryPayload.attachments = attachments;
        }

        const retryResponse = await fetch('https://api.resend.com/emails', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${resendApiKey}`
          },
          body: JSON.stringify(retryPayload)
        });

        const retryData = await retryResponse.json().catch(() => ({}));
        if (retryResponse.ok) {
          return res.status(200).json({
            success: true,
            details: retryData,
            warning: 'Sent via onboarding@resend.dev fallback due to unverified sender domain'
          });
        } else {
          return res.status(retryResponse.status).json({
            error: 'Resend API fallback failed',
            details: retryData
          });
        }
      }

      return res.status(response.status).json({ error: 'Resend API error', details: data });
    }

    return res.status(200).json({ success: true, details: data });
  } catch (error) {
    return res.status(500).json({ error: 'Failed to send email', details: error.message });
  }
}
