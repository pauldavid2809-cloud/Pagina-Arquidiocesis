export default async function handler(req, res) {
  // Only allow GET requests
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const userId = process.env.IG_USER_ID;
  const token  = process.env.IG_ACCESS_TOKEN;
  const groqKey = process.env.GROQ_API_KEY;

  if (!userId || !token) {
    return res.status(500).json({ error: 'Instagram credentials not configured' });
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
    res.setHeader('Access-Control-Allow-Origin', '*');

    return res.status(200).json(data);
  } catch (err) {
    return res.status(500).json({ error: 'Failed to fetch from Instagram', details: err.message });
  }
}
