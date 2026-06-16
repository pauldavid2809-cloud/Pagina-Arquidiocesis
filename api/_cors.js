export function handleCors(req, res) {
  const origin = req.headers.origin;
  const allowedOrigins = [
    'https://pagina-arquidiocesis.vercel.app',
    'https://pagina-arquidiocesis-main.vercel.app'
  ];
  
  let allowedOrigin = 'https://pagina-arquidiocesis.vercel.app';
  let isAllowed = true;
  
  if (origin) {
    const isLocalhost = /^http:\/\/(localhost|127\.0\.0\.1)(:\d+)?$/.test(origin) || 
                        origin.startsWith('http://localhost') || 
                        origin.startsWith('http://127.0.0.1');
    const isVercel = origin.endsWith('.vercel.app');
    const isExplicitlyAllowed = allowedOrigins.includes(origin);
    
    if (isLocalhost || isVercel || isExplicitlyAllowed) {
      allowedOrigin = origin;
    } else {
      isAllowed = false;
    }
  }
  
  res.setHeader('Access-Control-Allow-Credentials', 'true');
  res.setHeader('Access-Control-Allow-Origin', isAllowed ? allowedOrigin : 'https://pagina-arquidiocesis.vercel.app');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,POST,DELETE,PUT,PATCH');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version, Authorization'
  );
  
  if (!isAllowed) {
    res.status(403).json({ error: 'CORS policy: Origin not allowed' });
    return false;
  }
  
  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return false;
  }
  
  return true;
}
