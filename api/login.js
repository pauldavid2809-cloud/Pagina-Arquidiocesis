import fs from 'fs';
import path from 'path';
import { handleCors } from './_cors.js';

export default async function handler(req, res) {
  // CORS check
  if (!handleCors(req, res)) {
    return;
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

  const { loginType, password, email, parishCode } = body;

  if (!loginType || !password) {
    return res.status(400).json({ error: 'Missing parameters: loginType and password are required' });
  }

  const isParish = loginType === 'parish';
  
  // 1. Supabase Mode
  const supabaseUrl = process.env.SUPABASE_URL;
  const supabaseAnonKey = process.env.SUPABASE_ANON_KEY;

  if (supabaseUrl && supabaseAnonKey) {
    try {
      let url = '';
      if (isParish) {
        if (!parishCode) {
          return res.status(400).json({ error: 'Missing parishCode for parish login' });
        }
        url = `${supabaseUrl}/rest/v1/parroquias?code=eq.${encodeURIComponent(parishCode)}`;
      } else {
        if (!email) {
          return res.status(400).json({ error: 'Missing email for priest login' });
        }
        url = `${supabaseUrl}/rest/v1/sacerdotes?email=eq.${encodeURIComponent(email.trim().toLowerCase())}`;
      }

      const response = await fetch(url, {
        headers: {
          'apikey': supabaseAnonKey,
          'Authorization': `Bearer ${supabaseAnonKey}`
        }
      });

      if (!response.ok) {
        return res.status(response.status).json({ error: 'Database query failed' });
      }

      const users = await response.json();
      if (!users || users.length === 0) {
        return res.status(401).json({ error: isParish ? 'La parroquia seleccionada no está registrada.' : 'El correo ingresado no está registrado en el portal de la Cancillería.' });
      }

      const user = users[0];
      if (user.password !== password) {
        return res.status(401).json({ error: 'Contraseña incorrecta. Por favor intente de nuevo.' });
      }

      // Secure: Remove password before returning
      const userSafe = { ...user };
      delete userSafe.password;

      return res.status(200).json({ success: true, user: userSafe });
    } catch (err) {
      return res.status(500).json({ error: 'Database connection error', details: err.message });
    }
  }

  // 2. Local Offline Development Mode
  try {
    if (isParish) {
      if (!parishCode) {
        return res.status(400).json({ error: 'Missing parishCode for parish login' });
      }
      
      const parishesPath = path.join(process.cwd(), 'api', 'parishes_with_passwords.json');
      if (!fs.existsSync(parishesPath)) {
        return res.status(500).json({ error: 'Offline parish credentials file not found' });
      }

      const parishesData = JSON.parse(fs.readFileSync(parishesPath, 'utf-8'));
      const parish = parishesData.find(p => p.code === parishCode);

      if (!parish) {
        return res.status(401).json({ error: 'La parroquia seleccionada no está registrada.' });
      }

      if (parish.password !== password) {
        return res.status(401).json({ error: 'Contraseña incorrecta. Por favor intente de nuevo.' });
      }

      const userSafe = {
        code: parish.code,
        name: parish.name,
        email: parish.email,
        phone: parish.phone,
        role: parish.role || 'parish',
        direccion: parish.direccion || parish.address || "",
        parroco: parish.parroco || ""
      };

      return res.status(200).json({ success: true, user: userSafe });
    } else {
      if (!email) {
        return res.status(400).json({ error: 'Missing email for priest login' });
      }
      const cleanEmail = email.trim().toLowerCase();

      // Read from offline priests file
      const priestsPath = path.join(process.cwd(), 'api', 'unique_priests.json');
      let priest = null;
      
      if (fs.existsSync(priestsPath)) {
        const priestsData = JSON.parse(fs.readFileSync(priestsPath, 'utf-8'));
        priest = priestsData.find(p => p.email && p.email.toLowerCase() === cleanEmail);
      } else {
        // Fallback mockup if file is missing
        if (cleanEmail === 'cancilleria@arquidiocesisdemaracaibo.org') {
          priest = {
            name: "Mons. José Luis Azuaje Ayala",
            email: "cancilleria@arquidiocesisdemaracaibo.org",
            password: "canciller123",
            phone: "0412-0000000",
            role: "admin",
            parish: "Curia Metropolitana"
          };
        } else {
          priest = {
            name: "Pbro. Paul David",
            email: cleanEmail,
            password: "sacerdote123",
            phone: "0412-2809280",
            role: "priest",
            parish: "Parroquia de Pruebas"
          };
        }
      }

      if (!priest) {
        return res.status(401).json({ error: 'El correo ingresado no está registrado en el portal de la Cancillería.' });
      }

      if (priest.password !== password) {
        return res.status(401).json({ error: 'Contraseña incorrecta. Por favor intente de nuevo.' });
      }

      const userSafe = { ...priest };
      delete userSafe.password;

      return res.status(200).json({ success: true, user: userSafe });
    }
  } catch (err) {
    return res.status(500).json({ error: 'Offline authentication error', details: err.message });
  }
}
