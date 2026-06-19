import { createClient } from '@supabase/supabase-js';

export default async function handler(req, res) {
  // 1. Verify Request Method (only GET/POST is typically sent by Vercel Cron)
  if (req.method !== 'GET' && req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  // 2. Optional: Verify Cron Secret to prevent unauthorized invocations
  const authHeader = req.headers.authorization;
  if (process.env.NODE_ENV === 'production' && process.env.CRON_SECRET && authHeader !== `Bearer ${process.env.CRON_SECRET}`) {
    return res.status(401).json({ error: 'Unauthorized' });
  }

  const supabaseUrl = process.env.SUPABASE_URL;
  const supabaseServiceKey = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_ANON_KEY;

  if (!supabaseUrl || !supabaseServiceKey) {
    console.error('Supabase environment variables are missing (SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY or SUPABASE_ANON_KEY)');
    return res.status(500).json({ error: 'Supabase configuration is missing on the server' });
  }

  // Initialize Supabase Client (uses Service Role Key if available, falls back to Anon Key)
  const supabase = createClient(supabaseUrl, supabaseServiceKey);

  try {
    console.log('Fetching current Instagram access token from Supabase...');
    
    // 3. Read current token from 'integraciones' table
    const { data: integration, error: fetchError } = await supabase
      .from('integraciones')
      .select('ig_access_token')
      .limit(1)
      .single();

    if (fetchError) {
      console.error('Error fetching token from Supabase:', fetchError);
      return res.status(500).json({ error: 'Failed to retrieve token from database', details: fetchError.message });
    }

    if (!integration || !integration.ig_access_token) {
      console.error('No instagram token found in the "integraciones" table');
      return res.status(404).json({ error: 'No active Instagram token found in table "integraciones"' });
    }

    const currentToken = integration.ig_access_token;
    console.log('Token successfully fetched. Requesting refresh from Meta Graph API...');

    // 4. Request refreshed token from Meta API
    const refreshUrl = `https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token=${currentToken}`;
    const response = await fetch(refreshUrl);

    if (!response.ok) {
      const errData = await response.json().catch(() => ({}));
      const errMsg = errData.error?.message || response.statusText;
      console.error(`Meta API token refresh failed: ${errMsg}`, errData);
      return res.status(response.status).json({
        error: 'Instagram Graph API refresh failed',
        details: errMsg
      });
    }

    const json = await response.json();
    const newToken = json.access_token;

    if (!newToken) {
      console.error('Meta API response did not contain access_token', json);
      return res.status(500).json({ error: 'Meta API response did not return a valid token' });
    }

    console.log('Refreshed token received. Updating Supabase database...');

    // 5. Update token in 'integraciones' table
    const { error: updateError } = await supabase
      .from('integraciones')
      .update({ ig_access_token: newToken })
      .eq('ig_access_token', currentToken);

    if (updateError) {
      console.error('Error updating token in Supabase:', updateError);
      return res.status(500).json({ error: 'Failed to update new token in database', details: updateError.message });
    }

    console.log('Instagram access token refreshed and saved successfully!');
    return res.status(200).json({ success: true, message: 'Instagram access token refreshed successfully' });

  } catch (err) {
    console.error('Unexpected error during Instagram token refresh execution:', err);
    return res.status(500).json({ error: 'Internal Server Error', details: err.message });
  }
}
