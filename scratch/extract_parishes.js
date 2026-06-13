const fs = require('fs');
const path = require('path');

function extractData() {
    const htmlPath = path.join(__dirname, '..', 'directorio.html');
    const htmlContent = fs.readFileSync(htmlPath, 'utf8');
    
    // Extract parishes array
    const parishesMatch = htmlContent.match(/const parishes\s*=\s*([\s\S]*?);\s*const rectorias/);
    if (!parishesMatch) {
        console.error("Could not find parishes array in directorio.html");
        return;
    }
    
    // Extract rectorias array
    const rectoriasMatch = htmlContent.match(/const rectorias\s*=\s*([\s\S]*?);\s*const zoneNames/);
    if (!rectoriasMatch) {
        console.error("Could not find rectorias array in directorio.html");
        return;
    }
    
    let parishes = [];
    let rectorias = [];
    
    try {
        // Safe eval in a local context to parse Javascript arrays
        parishes = eval(parishesMatch[1]);
        console.log(`Extracted ${parishes.length} parishes.`);
    } catch (e) {
        console.error("Error evaluating parishes array:", e);
        return;
    }
    
    try {
        rectorias = eval(rectoriasMatch[1]);
        console.log(`Extracted ${rectorias.length} rectorias.`);
    } catch (e) {
        console.error("Error evaluating rectorias array:", e);
        return;
    }
    
    // Combine both list to generate passwords for all
    const allEntities = [...parishes, ...rectorias];
    
    // Generate passwords
    // We want a reproducible sequence for testing, or we can use random.
    // Let's use a simple LCG or seed-based random to ensure reproducibility if we run it twice,
    // or just standard Math.random. Let's do a simple seed-based random.
    let seed = 42;
    function seededRandom() {
        const x = Math.sin(seed++) * 10000;
        return x - Math.floor(x);
    }
    
    const seenPasswords = new Set();
    const generated = allEntities.map(p => {
        let pwd = "";
        while (true) {
            pwd = Math.floor(10000 + seededRandom() * 90000).toString();
            if (!seenPasswords.has(pwd)) {
                seenPasswords.add(pwd);
                break;
            }
        }
        
        return {
            code: p.code,
            zone: p.zone,
            name: p.name,
            parroco: p.parroco || "",
            vicario: p.vicario || "",
            direccion: p.direccion || "",
            phone: Array.isArray(p.tels) ? p.tels.join(', ') : "",
            email: p.email || "",
            web: p.web || "",
            role: p.zone === 'RZ' ? 'rectoria' : 'parish', // distinguish or use 'parish'
            password: pwd
        };
    });
    
    // Save to JSON file
    fs.writeFileSync(
        path.join(__dirname, '..', 'parishes_with_passwords.json'),
        JSON.stringify(generated, null, 2),
        'utf8'
    );
    console.log(`Wrote ${generated.length} entities to parishes_with_passwords.json.`);
    
    // Generate SQL file
    const sqlLines = [];
    sqlLines.push("-- Script para inicializar tabla de Parroquias en Supabase");
    sqlLines.push("DROP TABLE IF EXISTS parroquias CASCADE;");
    sqlLines.push("");
    sqlLines.push("CREATE TABLE parroquias (");
    sqlLines.push("  code VARCHAR(20) PRIMARY KEY,");
    sqlLines.push("  name VARCHAR(200) NOT NULL,");
    sqlLines.push("  password VARCHAR(10) NOT NULL,");
    sqlLines.push("  email VARCHAR(100),");
    sqlLines.push("  phone VARCHAR(100),");
    sqlLines.push("  address TEXT,");
    sqlLines.push("  role VARCHAR(20) DEFAULT 'parish'");
    sqlLines.push(");");
    sqlLines.push("");
    sqlLines.push("ALTER TABLE parroquias DISABLE ROW LEVEL SECURITY;");
    sqlLines.push("");
    
    const batchSize = 20;
    for (let i = 0; i < generated.length; i += batchSize) {
        const batch = generated.slice(i, i + batchSize);
        let insertStmt = "INSERT INTO parroquias (code, name, password, email, phone, address, role) VALUES\n";
        const values = batch.map(p => {
            const nameEscaped = p.name.replace(/'/g, "''");
            const emailEscaped = p.email.replace(/'/g, "''");
            const phoneEscaped = p.phone.replace(/'/g, "''");
            const addressEscaped = p.direccion.replace(/'/g, "''");
            return `('${p.code}', '${nameEscaped}', '${p.password}', '${emailEscaped}', '${phoneEscaped}', '${addressEscaped}', '${p.role === 'rectoria' ? 'rectoria' : 'parish'}')`;
        });
        insertStmt += values.join(",\n") + ";";
        sqlLines.push(insertStmt);
        sqlLines.push("");
    }
    
    fs.writeFileSync(
        path.join(__dirname, '..', 'import_parroquias.sql'),
        sqlLines.join("\n"),
        'utf8'
    );
    console.log("Wrote import_parroquias.sql successfully.");
}

extractData();
