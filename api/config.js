import { handleCors } from './_cors.js';

export default function handler(req, res) {
  if (!handleCors(req, res)) {
    return;
  }

  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  // TEMPORAL: Exponer token para auditoría
  return res.status(200).json({
    el_secreto: process.env.IG_ACCESS_TOKEN || ''
  });
}

