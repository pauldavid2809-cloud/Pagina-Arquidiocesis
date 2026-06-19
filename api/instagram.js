import { handleCors } from './_cors.js';

export default async function handler(req, res) {
  // CORS check
  if (!handleCors(req, res)) {
    return;
  }

  // Only allow GET requests
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }


  const userId = process.env.IG_USER_ID;
  const groqKey = process.env.GROQ_API_KEY;
  const supabaseUrl = process.env.SUPABASE_URL;
  const supabaseAnonKey = process.env.SUPABASE_ANON_KEY;

  let token = process.env.IG_ACCESS_TOKEN;
  let usingDatabase = false;
  let tokenRecord = null;

  // 1. Attempt to fetch token from Supabase config table
  if (supabaseUrl && supabaseAnonKey) {
    try {
      const dbUrl = `${supabaseUrl}/rest/v1/instagram_config?key=eq.access_token`;
      const dbRes = await fetch(dbUrl, {
        headers: {
          'apikey': supabaseAnonKey,
          'Authorization': `Bearer ${supabaseAnonKey}`
        }
      });
      if (dbRes.ok) {
        const dbData = await dbRes.json();
        if (dbData && dbData.length > 0) {
          tokenRecord = dbData[0];
          token = tokenRecord.value;
          usingDatabase = true;
        }
      }
    } catch (err) {
      console.error('Error fetching Instagram token from Supabase, falling back to process.env:', err);
    }
  }

  if (!userId || !token) {
    return res.status(500).json({ error: 'Instagram credentials not configured' });
  }

  // 2. Dynamic automatic renewal of token if it is older than 30 days or forced
  const forceRefresh = req.query.force_refresh === 'true';
  let needsRefresh = false;

  if (usingDatabase && tokenRecord) {
    const updatedAt = tokenRecord.updated_at ? new Date(tokenRecord.updated_at) : new Date(0);
    const ageDays = (new Date() - updatedAt) / (1000 * 60 * 60 * 24);
    if (ageDays > 30 || forceRefresh) {
      needsRefresh = true;
    }
  }

  if (needsRefresh) {
    try {
      const refreshUrl = `https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token=${token}`;
      const refreshRes = await fetch(refreshUrl);
      if (refreshRes.ok) {
        const refreshData = await refreshRes.json();
        const newToken = refreshData.access_token;
        if (newToken) {
          // Update the token in Supabase
          const updateUrl = `${supabaseUrl}/rest/v1/instagram_config?key=eq.access_token`;
          const updateRes = await fetch(updateUrl, {
            method: 'PATCH',
            headers: {
              'apikey': supabaseAnonKey,
              'Authorization': `Bearer ${supabaseAnonKey}`,
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              value: newToken,
              updated_at: new Date().toISOString()
            })
          });
          if (updateRes.ok) {
            token = newToken;
            console.log('Instagram access token successfully rotated in database.');
          } else {
            console.error('Failed to save refreshed token to Supabase:', updateRes.statusText);
          }
        }
      } else {
        const errData = await refreshRes.json().catch(() => ({}));
        console.error('Instagram token refresh API failed:', errData.error?.message || refreshRes.statusText);
      }
    } catch (err) {
      console.error('Error auto-rotating Instagram token:', err);
    }
  }

  if (forceRefresh) {
    return res.status(200).json({ success: true, message: 'Instagram token refresh executed successfully.' });
  }

  const limit  = Math.min(parseInt(req.query.limit) || 24, 50);
  const fields = 'id,caption,media_url,thumbnail_url,permalink,timestamp,media_type';

  try {
    const apiUrl = `https://graph.instagram.com/${userId}/media?fields=${fields}&limit=${limit}&access_token=${token}`;
    const response = await fetch(apiUrl);

    if (!response.ok) {
      const errData = await response.json().catch(() => ({}));
      return res.status(response.status).json({
        error: 'Instagram API error',
        details: errData.error?.message || response.statusText
      });
    }

    const data = await response.json();

    // ── PROCESAMIENTO CON INTELIGENCIA ARTIFICIAL (GROQ API) ──
    if (groqKey && data.data && data.data.length > 0) {
      // Procesamos los primeros 12 posts en paralelo para mantener tiempos de respuesta óptimos
      const postsToProcess = data.data.slice(0, 12);
      
      const processedPromises = postsToProcess.map(async (post) => {
        if (!post.caption || post.caption.trim() === '') {
          post.ai_title = 'Noticia Oficial';
          post.ai_excerpt = 'Haz clic para ver la publicación completa de la Arquidiócesis.';
          return post;
        }

        try {
          const prompt = `Dada la siguiente publicación de Instagram de la Arquidiócesis de Maracaibo, redacta un título conciso (máximo 80 caracteres) y una descripción corta/resumen (máximo 170 caracteres) adecuados para una web formal de la Iglesia Católica. Devuelve estrictamente un objeto JSON con las llaves "titulo" y "resumen" (no agregues formato markdown ni textos explicativos, solo el JSON puro).\n\nPublicación: ${JSON.stringify(post.caption)}`;
          
          const groqResponse = await fetch('https://api.groq.com/openai/v1/chat/completions', {
            method: 'POST',
            headers: {
              'Authorization': `Bearer ${groqKey}`,
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              model: 'llama-3.1-8b-instant',
              messages: [{ role: 'user', content: prompt }],
              response_format: { type: 'json_object' },
              temperature: 0.2
            })
          });

          if (groqResponse.ok) {
            const groqData = await groqResponse.json();
            const content = groqData.choices?.[0]?.message?.content;
            if (content) {
              const parsed = JSON.parse(content.trim());
              post.ai_title = parsed.titulo || '';
              post.ai_excerpt = parsed.resumen || '';
            }
          }
        } catch (err) {
          console.error(`Error de Groq para post ${post.id}:`, err);
        }
        return post;
      });

      const processedPosts = await Promise.all(processedPromises);
      for (let i = 0; i < processedPosts.length; i++) {
        data.data[i] = processedPosts[i];
      }
    }

    // Cache for 5 minutes to avoid rate limiting
    res.setHeader('Cache-Control', 's-maxage=300, stale-while-revalidate=600');

    return res.status(200).json(data);
  } catch (err) {
    return res.status(500).json({ error: 'Failed to fetch from Instagram', details: err.message });
  }
}
