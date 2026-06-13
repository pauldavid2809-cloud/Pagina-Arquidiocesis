import json

def generate_sql():
    with open('parishes_with_passwords.json', 'r', encoding='utf-8') as f:
        parishes = json.load(f)
        
    sql_lines = []
    sql_lines.append("-- Script para inicializar tabla de Parroquias en Supabase")
    sql_lines.append("DROP TABLE IF EXISTS parroquias CASCADE;")
    sql_lines.append("")
    sql_lines.append("CREATE TABLE parroquias (")
    sql_lines.append("  code VARCHAR(20) PRIMARY KEY,")
    sql_lines.append("  name VARCHAR(200) NOT NULL,")
    sql_lines.append("  password VARCHAR(10) NOT NULL,")
    sql_lines.append("  email VARCHAR(100),")
    sql_lines.append("  phone VARCHAR(100),")
    sql_lines.append("  role VARCHAR(20) DEFAULT 'parish'")
    sql_lines.append(");")
    sql_lines.append("")
    sql_lines.append("ALTER TABLE parroquias DISABLE ROW LEVEL SECURITY;")
    sql_lines.append("")
    
    # We will write inserts in batches of 20 to be safe and clean
    batch_size = 20
    for i in range(0, len(parishes), batch_size):
        batch = parishes[i:i+batch_size]
        insert_stmt = "INSERT INTO parroquias (code, name, password, email, phone) VALUES\n"
        values = []
        for p in batch:
            name_escaped = p['name'].replace("'", "''")
            email_escaped = p['email'].replace("'", "''")
            phone_escaped = p['phone'].replace("'", "''")
            values.append(f"('{p['code']}', '{name_escaped}', '{p['password']}', '{email_escaped}', '{phone_escaped}')")
        insert_stmt += ",\n".join(values) + ";"
        sql_lines.append(insert_stmt)
        sql_lines.append("")
        
    with open('import_parroquias.sql', 'w', encoding='utf-8') as f_out:
        f_out.write("\n".join(sql_lines))
        
    print("Generated import_parroquias.sql successfully.")

if __name__ == '__main__':
    generate_sql()
