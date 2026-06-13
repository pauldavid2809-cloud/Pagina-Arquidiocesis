-- Script para inicializar Base de Datos en Supabase (Por Correo)
DROP TABLE IF EXISTS tramites;
DROP TABLE IF EXISTS sacerdotes;

CREATE TABLE sacerdotes (
  email VARCHAR(100) PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  password VARCHAR(100) NOT NULL,
  phone VARCHAR(20),
  role VARCHAR(20) DEFAULT 'priest',
  cedula VARCHAR(50) DEFAULT '',
  birth_date DATE NULL,
  ordination_date DATE NULL,
  ordaining_bishop VARCHAR(150) DEFAULT '',
  diocesis VARCHAR(150) DEFAULT '',
  parish VARCHAR(250) DEFAULT '',
  charge VARCHAR(150) DEFAULT ''
);

CREATE TABLE tramites (
  id VARCHAR(20) PRIMARY KEY,
  email VARCHAR(100) REFERENCES sacerdotes(email),
  priest_name VARCHAR(100) NOT NULL,
  priest_email VARCHAR(100) NOT NULL,
  type VARCHAR(100) NOT NULL,
  date DATE DEFAULT CURRENT_DATE,
  subject VARCHAR(200) NOT NULL,
  parish VARCHAR(200) NOT NULL,
  details TEXT NOT NULL,
  status VARCHAR(20) DEFAULT 'Pendiente',
  feedback TEXT DEFAULT '',
  document_content TEXT DEFAULT '',
  document_file_content TEXT DEFAULT '',
  document_file_name VARCHAR(255) DEFAULT '',
  institution VARCHAR(250) DEFAULT '',
  priest_file_content TEXT DEFAULT '',
  priest_file_name VARCHAR(255) DEFAULT ''
);

-- Deshabilitar RLS para desarrollo y pruebas del portal
ALTER TABLE sacerdotes DISABLE ROW LEVEL SECURITY;
ALTER TABLE tramites DISABLE ROW LEVEL SECURITY;

-- Insertar Sacerdotes del Directorio
INSERT INTO sacerdotes (email, name, password, phone, role) VALUES
('cancilleria@arquidiocesisdemaracaibo.org', 'Mons. José Luis Azuaje Ayala', 'canciller123', '0412-0000000', 'admin'),
('pauldavid2809@gmail.com', 'Pbro. Paul David', 'sacerdote123', '0412-2809280', 'priest'),
('pauldd28@gmail.com', 'Pbro. Paul David (Alt)', 'sacerdote123', '0412-2809280', 'priest'),
('nprimera40@gmail.com', 'Pbro. Néstor Primera', 'sacerdote123', '0412-7885662', 'priest'),
('rafael.angel@arquidiocesisdemaracaibo.org', 'Pbro. Rafael Ángel Villalobos Carmona', 'sacerdote123', '0414-3676212', 'priest'),
('santabarbaramaracaibo@hotmail.com', 'Pbro. José Gregorio Andrade Vecino', 'sacerdote123', '0412-7892388', 'priest'),
('basilicachiquinquira@gmail.com', 'Pbro. Nedward Jorge Andrade', 'sacerdote123', '0414-2889973', 'priest'),
('basilicachiquinquira1@gmail.com', 'Pbro. José Miguel Hernández', 'sacerdote123', '0414-2889973', 'priest'),
('pquiasanbenitopalermo@hotmail.com', 'Pbro. José Enrique Varela', 'sacerdote123', '0414-6620878', 'priest'),
('pquiasanbenitopalermo1@hotmail.com', 'Pbro. Jorge A. Dos Pasos', 'sacerdote123', '0414-6620878', 'priest'),
('pquiasanbenitopalermo2@hotmail.com', 'Pbro. Renzo O. Gotera', 'sacerdote123', '0414-6620878', 'priest'),
('juan.pablo@arquidiocesisdemaracaibo.org', 'Pbro. Juan Pablo Hernández', 'sacerdote123', '0261-7650404', 'priest'),
('monfercheo@hotmail.com', 'Pbro. José Gregorio Montenegro Fereira', 'sacerdote123', '0424-6361306', 'priest'),
('alfonso_rodriguez@cantv.net', 'Pbro. Alfonso Rodríguez', 'sacerdote123', '0414-6281643', 'priest'),
('parroquiasanjosemcbo@gmail.com', 'Pbro. Roberto Segundo Morales Carruyo', 'sacerdote123', '0424-6614822', 'priest'),
('jesus.colina@arquidiocesisdemaracaibo.org', 'Pbro. Jesús Colina', 'sacerdote123', '0424-6153784', 'priest'),
('parroquia.perpetuosocorro.mcbo@gmail.com', 'R.P. Fray José Vivas Vivas, OSA', 'sacerdote123', '0412-5147175', 'priest'),
('parroquia.perpetuosocorro.mcbo1@gmail.com', 'R.P. Fray Oswaldo Matheus González, OSA', 'sacerdote123', '0412-5147175', 'priest'),
('iglesialaconsolacion.mbo@gmail.com', 'R.P. Fray Ricardo Riaño, OAR', 'sacerdote123', '0414-7127606', 'priest'),
('elrosariomcbo@gmail.com', 'Pbro. Max Gregorio Guerere Rodríguez', 'sacerdote123', '0424-6293617', 'priest');

INSERT INTO sacerdotes (email, name, password, phone, role) VALUES
('andres.de@arquidiocesisdemaracaibo.org', 'Pbro. Andrés de Jesús Afanador Rodríguez', 'sacerdote123', '0412-7128907', 'priest'),
('licduarte@gmail.com', 'Pbro. Ovidio Eduardo Duarte Torres', 'sacerdote123', '0412-6275968', 'priest'),
('parroquialasmercedes@hotmail.com', 'Pbro. Lenín José Naranjo Flores (enero 2014)', 'sacerdote123', '0412-6467261', 'priest'),
('edgarjose@cantv.net', 'Pbro. Edgar J. Doria M.', 'sacerdote123', '0414-3612908', 'priest'),
('juan.jose@arquidiocesisdemaracaibo.org', 'Pbro. Juan José Navarro Robertis', 'sacerdote123', '0416-5611244', 'priest'),
('pbropedrocolmenares@hotmail.com', 'Pbro. Pedro Colmenares', 'sacerdote123', '0426-9655848', 'priest'),
('danilo.gonzalez@arquidiocesisdemaracaibo.org', 'Pbro. Danilo González', 'sacerdote123', '0416-7611987', 'priest'),
('parrnuestrasradelcarmenmcbo@gmail.com', 'Pbro. Eleuterio Segundo Cuevas Pereira', 'sacerdote123', '0414-6844539', 'priest'),
('kyke32@gmail.com', 'Pbro. Enrique Rojas Peña', 'sacerdote123', '0414-7539894', 'priest'),
('rafaelopez3303@gmail.com', 'Pbro. Rafael López', 'sacerdote123', '0414-6266122', 'priest'),
('padreabravo@yahoo.com', 'Pbro. José Andrés Bravo Henríquez', 'sacerdote123', '0414-6185341', 'priest'),
('pjosepineda@gmail.com', 'Pbro. José Pineda', 'sacerdote123', '0424-6755405', 'priest'),
('jesusvc55@hotmail.com', 'R.P. Jesús Vásquez, SchP', 'sacerdote123', '0412-0616901', 'priest'),
('mospino_martinez@hotmail.com', 'Pbro. Miguel Antonio Ospino', 'sacerdote123', '0416-0625909', 'priest'),
('mcbofatima@gmail.com', 'R.P. Francisco Ortiz Bran, O.de M.', 'sacerdote123', '0414-6715547', 'priest'),
('mcbofatima1@gmail.com', 'R.P. Alejandro Rincón Quiroz, O.de M.', 'sacerdote123', '0414-6715547', 'priest'),
('sanramonnonato@gmail.com', 'R.P. Poncs Capell Capell, O.de M.', 'sacerdote123', '0414-3466396', 'priest'),
('robert.alberto@arquidiocesisdemaracaibo.org', 'Pbro. Robert Alberto Álvarez Pérez', 'sacerdote123', '0424-6704586', 'priest'),
('hector.bermudez.c@hotmail.com', 'Pbro. Héctor de los Reyes Bermúdez C. (octubre 2014)', 'sacerdote123', '0416-1618046', 'priest'),
('fr..adelmo@arquidiocesisdemaracaibo.org', 'Pbro. Fr. Adelmo Irene, OAR', 'sacerdote123', '0424-1218537', 'priest');

INSERT INTO sacerdotes (email, name, password, phone, role) VALUES
('wilmer.olano@arquidiocesisdemaracaibo.org', 'Pbro. Wilmer Olano', 'sacerdote123', '0414-6920201', 'priest'),
('mcboparroquiasanonofre@gmail.com', 'R.P. Fray José Antonio Díaz, OAR', 'sacerdote123', '0424-6178408', 'priest'),
('mcboparroquiasanonofre1@gmail.com', 'R.P. Fray Juan Carlos Fernández, OAR', 'sacerdote123', '0424-6178408', 'priest'),
('sanjuanboscomcbo@gmail.com', 'Pbro. Dainer Prieto (Párroco', 'sacerdote123', '0414-3636962', 'priest'),
('fraypedrocarm@gmail.com', 'R.P. Pedro Castellano, OCarm', 'sacerdote123', '0424-6747353', 'priest'),
('jesus.sandoval@arquidiocesisdemaracaibo.org', 'Pbro. Jesús Sandoval', 'sacerdote123', '0414-9617569', 'priest'),
('padrereye@hotmail.com', 'Pbro. Dr. Carlos José Reyes B.', 'sacerdote123', '0412-2575199', 'priest'),
('p.n.s.jesucristorey@gmail.com', 'Pbro. Leonardo Martínez', 'sacerdote123', '0414-6654756', 'priest'),
('jorgeservi0518@gmail.com', 'Pbro. Jorge David Sánchez Urdaneta (Adm. Parroquial 10/01/2026)', 'sacerdote123', '0424-6219438', 'priest'),
('yonysmendoza@gmail.com', 'R.P. Yonys Mendoza, MSC', 'sacerdote123', '0414-6316996', 'priest'),
('dionni.jose@arquidiocesisdemaracaibo.org', 'Pbro. Dionni José Ríos Ríos (Adm. Parroquial 15/02/2026)', 'sacerdote123', '0414-1640886', 'priest'),
('silverio.antonio@arquidiocesisdemaracaibo.org', 'Pbro. Silverio Antonio Osorio Mora', 'sacerdote123', '0412-5142747', 'priest'),
('parroquiasmosacramento@gmail.com', 'Pbro. Ender Alexander Castillo Montoya (Administrador parroquial 15/11/2025)', 'sacerdote123', '0424-2582491', 'priest'),
('jose.domingo@arquidiocesisdemaracaibo.org', 'Pbro. José Domingo Alvarado', 'sacerdote123', '0414-6827366', 'priest'),
('andres.bravo@arquidiocesisdemaracaibo.org', 'Pbro. Andrés Bravo', 'sacerdote123', '0414-6185341', 'priest'),
('sanchezaandry@gmail.com', 'Pbro. Andry Sánchez', 'sacerdote123', '0424-6949290', 'priest'),
('henrybenito1@hotmail.com', 'Pbro. Henry Tapia', 'sacerdote123', '0416-9604224', 'priest'),
('joseanbarboza@gmail.com', 'Pbro. Lcdo. Richard Garrillo', 'sacerdote123', '0261-7320042', 'priest'),
('pbrolopezquintero@hotmail.com', 'Pbro. Leonardo López', 'sacerdote123', '0412-0619083', 'priest'),
('danilo.humberto@arquidiocesisdemaracaibo.org', 'Pbro. Danilo Humberto Calderón Matheus', 'sacerdote123', '0424-6268956', 'priest');

INSERT INTO sacerdotes (email, name, password, phone, role) VALUES
('stodomingogcatolicaparroquia@gmail.com', 'Pbro. Raúl R. Montoya Medero', 'sacerdote123', '0414-6799880', 'priest'),
('nestor.luis@arquidiocesisdemaracaibo.org', 'Pbro. Néstor Luis Pérez', 'sacerdote123', '0424-6919517', 'priest'),
('francisco.antonio@arquidiocesisdemaracaibo.org', 'Pbro. Francisco Antonio Niño Correa', 'sacerdote123', '0412-7683972', 'priest'),
('engelbert.alfredo@arquidiocesisdemaracaibo.org', 'Pbro. Engelbert Alfredo Jackson Carrasco', 'sacerdote123', '0414-6237799', 'priest'),
('padrecarlosquiva@gmail.com', 'Pbro. Carlos Quiva', 'sacerdote123', '0412-1285174', 'priest'),
('jorge.enrique@arquidiocesisdemaracaibo.org', 'Pbro. Jorge Enrique Rodríguez González', 'sacerdote123', '0414-6513813', 'priest'),
('raulalfredo1963@hotmail.com', 'Pbro. Raúl Moreno', 'sacerdote123', '0414-6326406', 'priest'),
('raulalfredo19631@hotmail.com', 'Pbro. Hebert de Jesús Rivera Cañizález', 'sacerdote123', '0414-6326406', 'priest'),
('daigelhml@gmail.com', 'Pbro. Daigel Medina', 'sacerdote123', '0414-6483753', 'priest'),
('jose.del@arquidiocesisdemaracaibo.org', 'Pbro. José del Carmen Chirinos (Adm. Parroquial)', 'sacerdote123', '0414-6089719', 'priest'),
('fabricio.medina@arquidiocesisdemaracaibo.org', 'Pbro. Fabricio Medina', 'sacerdote123', '0414-6266325', 'priest'),
('parroquiasanrafael@gmail.com', 'Pbro. Rafael Morales', 'sacerdote123', '0416-6667944', 'priest'),
('rafael.morales@arquidiocesisdemaracaibo.org', 'Pbro. Rafael Morales', 'sacerdote123', '0416-6667944', 'priest'),
('evelio.perez@arquidiocesisdemaracaibo.org', 'Pbro. Evelio Pérez', 'sacerdote123', '0424-6288234', 'priest'),
('yonder.javier@arquidiocesisdemaracaibo.org', 'Pbro. Yonder Javier Urdaneta Hiza (Adm. Parroquial 18/01/2026)', 'sacerdote123', '0412-1670969', 'priest'),
('william.chiquinquira@arquidiocesisdemaracaibo.org', 'Pbro. William Chiquinquirá Ortega Colmenares', 'sacerdote123', '0424-6539582', 'priest'),
('pquia.jesusredentor@gmail.com', 'Pbro. José G. Sánchez (in solidum)', 'sacerdote123', '0416-4617636', 'priest'),
('pquia.jesusredentor1@gmail.com', 'Pbro. Valentín Segundo Rodríguez López', 'sacerdote123', '0416-4617636', 'priest'),
('padresantosilva@gmail.com', 'Pbro. Santos Xavier Silva Blanco (Adm. Parroquial)', 'sacerdote123', '0412-1742378', 'priest'),
('eduardodaboin1991@gmail.com', 'Pbro. Eduardo José Daboin Bermúdez Diác. Francisco José Núñez Larez', 'sacerdote123', '0414-6690248', 'priest');

INSERT INTO sacerdotes (email, name, password, phone, role) VALUES
('german.palmar@arquidiocesisdemaracaibo.org', 'Pbro. Germán Palmar', 'sacerdote123', '0412-7980355', 'priest'),
('else-oresmiluz@hotmail.com', 'Pbro. Dilmer Báez', 'sacerdote123', '0426-4604314', 'priest'),
('padresantosilva1@gmail.com', 'Pbro. Santos Xavier Silva Blanco', 'sacerdote123', '0412-1742378', 'priest'),
('pedro.enrique@arquidiocesisdemaracaibo.org', 'R.P. Pedro Enrique Paredes Ramírez, IC', 'sacerdote123', '0412-7697073', 'priest'),
('laudi.zambrano@arquidiocesisdemaracaibo.org', 'Pbro. Laudi Zambrano', 'sacerdote123', '0414-3618152', 'priest'),
('familiajuandediana@gmail.com', 'R.P. Juan Esteban Padilla Ponce, O.H.', 'sacerdote123', '0424-6224357', 'priest'),
('evelio.perez1@arquidiocesisdemaracaibo.org', 'Pbro. Evelio Pérez', 'sacerdote123', '0424-6288234', 'priest'),
('padrecarlosquiva1@gmail.com', 'Pbro. Carlos Quiva', 'sacerdote123', '0412-1285174', 'priest'),
('pedro.enrique1@arquidiocesisdemaracaibo.org', 'R.P. Pedro Enrique Paredes Ramírez, IC', 'sacerdote123', '0412-7697073', 'priest');

-- Insertar trámites iniciales de prueba
INSERT INTO tramites (id, email, priest_name, priest_email, type, date, subject, parish, details, status, feedback, document_content) VALUES
('REQ-1001', 'pauldavid2809@gmail.com', 'Pbro. Paul David', 'pauldavid2809@gmail.com', 'Licencia Ministerial', '2026-06-01', 'Renovación de Licencia Ministerial Anual', 'Parroquia de Pruebas', 'Solicito la renovación de mi licencia ministerial.', 'Aprobado', 'Aprobado oficialmente.', 'DECRETO DE CANCILLERÍA Nº 024-2026

Maracaibo, 1 de Junio de 2026

CONCEDEMOS la renovación de su LICENCIA MINISTERIAL por el lapso de un año.

Mons. José Luis Azuaje Ayala, Arzobispo Metropolitano.'),
('REQ-1002', 'pauldavid2809@gmail.com', 'Pbro. Paul David', 'pauldavid2809@gmail.com', 'Certificado de Idoneidad (Celebret)', '2026-06-04', 'Certificado de Idoneidad para viaje', 'Parroquia de Pruebas', 'Solicito celebret para viajar a Bogotá.', 'Pendiente', '', ''),
('REQ-1003', 'pauldd28@gmail.com', 'Pbro. Paul David (Alt)', 'pauldd28@gmail.com', 'Licencia Ministerial', '2026-06-05', 'Solicitud de Licencia Ministerial', 'Parroquia de Pruebas', 'Prueba con mi otro correo electrónico.', 'Pendiente', '', '');
