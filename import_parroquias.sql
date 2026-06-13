-- Script para inicializar tabla de Parroquias en Supabase
DROP TABLE IF EXISTS parroquias CASCADE;

CREATE TABLE parroquias (
  code VARCHAR(20) PRIMARY KEY,
  name VARCHAR(200) NOT NULL,
  password VARCHAR(10) NOT NULL,
  email VARCHAR(100),
  phone VARCHAR(100),
  address TEXT,
  role VARCHAR(20) DEFAULT 'parish'
);

ALTER TABLE parroquias DISABLE ROW LEVEL SECURITY;

INSERT INTO parroquias (code, name, password, email, phone, address, role) VALUES
('PZ1-1', 'PARROQUIA EL SAGRARIO · Catedral de los Santos Apóstoles Pedro y Pablo', '80606', 'nprimera40@gmail.com', '0412-7885662, 0416-5619091', 'Av. 4 con calle 95, frente a la Plaza Bolívar', 'parish'),
('PZ1-2', 'PARROQUIA SANTA LUCÍA', '32731', '', '0412-5556236', 'Av. 2 entre Calle 89 y 90, frente a la Plaza Dr. Serrano', 'parish'),
('PZ1-3', 'PARROQUIA SANTA BÁRBARA', '11732', 'santabarbaramaracaibo@hotmail.com', '0261-7230509, 0412-7892388', 'Av. 8 Calle Páez con calle 95 Venezuela', 'parish'),
('PZ1-4', 'PARROQUIA SAN JUAN DE DIOS Y BASÍLICA SANTUARIO DE NTRA. SRA. DE CHIQUINQUIRÁ', '13172', 'basilicachiquinquira@gmail.com', '0412-2473657, 0424-6155550', '', 'parish'),
('PZ1-5', 'PARROQUIA SAN BENITO DE PALERMO', '89512', 'pquiasanbenitopalermo@hotmail.com', '0412-5147107, 0414-6620878', 'Av. Nº 3A con Calle 86, Sector Valle Frío', 'parish'),
('PZ1-6', 'PARROQUIA NTRA. SRA. DE LA ASUNCIÓN', '75810', '', '0426-4436922, 0261-7650404', 'Av. 17 Los Haticos', 'parish'),
('PZ1-7', 'PARROQUIA NTRA. SRA. DE LA MEDALLA MILAGROSA', '50804', 'monfercheo@hotmail.com', '0424-6361306, 0424-6197583', 'Av. 17 Los Haticos', 'parish'),
('PZ1-8', 'PARROQUIA SANTO CRISTO DE ARANZA', '52612', 'alfonso_rodriguez@cantv.net', '0414-6281643, 0261-4237583', 'Av. 17 con Calle 106, Los Haticos', 'parish'),
('PZ2-1', 'PARROQUIA SAN JOSÉ', '32631', 'parroquiasanjosemcbo@gmail.com', '0424-6614822, 0424-6004278', 'Calle 77 N° 16-30', 'parish'),
('PZ2-2', 'PARROQUIA SAN ALFONSO MARÍA DE LIGORIO', '36258', '', '0414-6920240, 0261-7519818', 'Urb. Santa María Av. 27 Nº 69A-70', 'parish'),
('PZ2-3', 'PARROQUIA NTRA. SRA. DEL PERPETUO SOCORRO', '34832', 'parroquia.perpetuosocorro.mcbo@gmail.com', '0412-5238206, 0424-1354551', 'Av. 9B N° 64-64, Barrio Tierra Negra', 'parish'),
('PZ2-4', 'PARROQUIA NTRA. SRA. DE LA CONSOLACIÓN', '32635', 'iglesialaconsolacion.mbo@gmail.com', '0414-7127606, 0416-5030067', 'Av. Bella Vista Esq. Calle 79', 'parish'),
('PZ2-5', 'PARROQUIA NTRA. SRA. DEL ROSARIO', '19856', 'elrosariomcbo@gmail.com', '0414-6464689, 0424-6293617', 'Urb. La Virginia, entre calles 67A y 72, sector La Lago', 'parish'),
('PZ2-6', 'PARROQUIA SAN JUDAS TADEO', '50343', '', '0412-7128907, 0412-7857731', 'Calle 85 Falcón, Sector Las Delicias', 'parish'),
('PZ2-7', 'PARROQUIA SAN ANTONIO MARÍA CLARET', '54098', 'licduarte@gmail.com', '0412-6275968', 'Calle Dr. Portillo N° 3E-20', 'parish'),
('PZ2-8', 'PARROQUIA NTRA. SRA. DE LAS MERCEDES', '68279', 'parroquialasmercedes@hotmail.com', '0412-6467261, 0412-7113145', '', 'parish'),
('PZ2-9', 'PARROQUIA SAGRADO CORAZÓN DE JESÚS', '75383', 'edgarjose@cantv.net', '0414-3612908', 'Av. 4 Calle 68A Bella Vista', 'parish'),
('PZ3-1', 'PARROQUIA NTRA. SRA. DE LOURDES (MARACAIBO)', '44206', '', '0416-5611244, 0261-7525301', 'Av. 28 La Limpia', 'parish'),
('PZ3-2', 'PARROQUIA SAN MIGUEL ARCÁNGEL', '90441', 'pbropedrocolmenares@hotmail.com', '0426-9655848, 0261-7292806', 'Sabaneta Larga Av. 20 Calle 100 s/n', 'parish'),
('PZ3-3', 'PARROQUIA LA SAGRADA FAMILIA', '84006', '', '0416-7611987, 0261-7874331', 'Urb. San Miguel Av. 60 N# 96G-30', 'parish');

INSERT INTO parroquias (code, name, password, email, phone, address, role) VALUES
('PZ3-4', 'PARROQUIA NTRA. SRA. DEL CARMEN (MARACAIBO)', '27373', 'parrnuestrasradelcarmenmcbo@gmail.com', '0414-3615185', 'Barrio Andrés Eloy Blanco, Av. 53 N° 98C-100, Sector Gallo Verde', 'parish'),
('PZ3-5', 'PARROQUIA SAN PEDRO APÓSTOL', '60130', 'kyke32@gmail.com', '0414-7539894, 0261-7649041', 'Haticos por Arriba, calle 113A Nº 19C-36', 'parish'),
('PZ3-6', 'PARROQUIA SAN MARTÍN DE PORRES', '33434', 'psanmartindeporres2016@hotmail.com', '0414-6266122, 0414-6596076', 'Barrio Los Estanques calle 113', 'parish'),
('PZ3-7', 'PARROQUIA SANTA TERESITA DEL NIÑO JESÚS', '35811', 'padreabravo@yahoo.com', '0414-6185341', 'Avenida 29, Zulia Amparo. Casa cural: calle 81 #57B-75, Cacique Mara', 'parish'),
('PZ3-8', 'PARROQUIA NIÑA MARÍA', '53961', 'pjosepineda@gmail.com', '0424-6755405, 0261-7341013', 'Av. 11-4D Sector Los Robles', 'parish'),
('PZ3-9', 'PARROQUIA SAN IGNACIO DE LOYOLA', '82018', 'jesusvc55@hotmail.com', '0412-0616901, 0424-6123229', 'Av. Principal del Barrio Los Andes', 'parish'),
('PZ3-10', 'PARROQUIA SAN TARSICIO', '75087', 'mospino_martinez@hotmail.com', '0416-0625909', 'Circunvalación Nº 2 Barrio Jorge Hernández calle 56A', 'parish'),
('PZ4-1', 'PARROQUIA SANTA MÓNICA (LA CONCEPCIÓN)', '23667', 'fraypedrocarm@gmail.com', '0414-7444553, 0412-7347435, 0422-7170825', 'La Concepción, Mcpio. Jesús Enrique Lossada', 'parish'),
('PZ4-2', 'PARROQUIA NTRA. SRA. DE COROMOTO', '91613', '', '0414-6713708, 0414-9617569, 0424-6214417', 'Urb. Los Olivos, calle 73 con calle 67', 'parish'),
('PZ4-3', 'PARROQUIA SAN PABLO APÓSTOL', '59187', 'padrereye@hotmail.com', '0412-2575199, 0261-7542280', 'Urb. La Rotaria Av. 85', 'parish'),
('PZ4-4', 'PARROQUIA NUESTRO SEÑOR JESUCRISTO REY', '31026', 'P.N.S.Jesucristorey@gmail.com', '0414-6654756', 'Barrio Panamericano, AV 91', 'parish'),
('PZ4-5', 'PARROQUIA EL BUEN PASTOR', '35238', 'jorgeservi0518@gmail.com', '0424-6219438, 04126451573', 'Urb. Cuatricentenario 1ª etapa, Av. principal 66g', 'parish'),
('PZ4-6', 'PARROQUIA NTRA. SRA. DE LA PAZ', '58365', 'yonysmendoza@gmail.com', '0414-6316996, 0261-7549581', 'Av. 78 1ª Etapa Urb. La Victoria', 'parish'),
('PZ4-7', 'PARROQUIA LA RESURRECCIÓN DEL SEÑOR', '26528', '', '0412-6695642, 0261-3283191', 'Barrio Libertador Av. 93C Nº 79J-48', 'parish'),
('PZ4-8', 'PARROQUIA SAN ISIDRO LABRADOR', '16873', '', '0412-5470157, 0414-6143544', 'Sector San Isidro, Carretera Vía La Concepción', 'parish'),
('PZ4-9', 'PARROQUIA SANTÍSIMO SACRAMENTO', '28142', 'parroquiasmosacramento@gmail.com', '0424-2582491, 0412-1691326', '', 'parish'),
('PZ4-10', 'PARROQUIA SANTA INÉS', '80610', '', '04146827366, 0424-6305238', 'Barrio Indio Mara', 'parish'),
('PZ4-11', 'PARROQUIA SAN JUAN CRISÓSTOMO Y SAN JUAN PABLO II (Parroquia Universitaria)', '88598', '', '0414-6185341', '', 'parish'),
('PZ5-1', 'PARROQUIA NTRA. SRA. DE GUADALUPE', '20211', 'sanchezaandry@gmail.com', '0414-1748270, 0261-7344890', 'Av. 16 con calle 11, Sierra Maestra', 'parish'),
('PZ5-2', 'PARROQUIA JESÚS NAZARENO', '20805', 'henrybenito1@hotmail.com', '0416-9604224, 0261-7615915', 'Av. 16 entre C/c 11 y 12, barrio El Manzanillo', 'parish');

INSERT INTO parroquias (code, name, password, email, phone, address, role) VALUES
('PZ5-3', 'PARROQUIA SANTÍSIMO SALVADOR', '35904', 'joseanbarboza@gmail.com', '0412-6405000, 0261-7320042', 'Calle 4 con Av. 49 al lado de la E.A. Madre Laura (El Callao)', 'parish'),
('PZ5-4', 'PARROQUIA SANTÍSIMO CRISTO DE SAN FRANCISCO', '68014', 'pbrolopezquintero@hotmail.com', '0412-1277017, 0414-6445575', 'San Francisco Av. 5 calle 27', 'parish'),
('PZ5-5', 'PARROQUIA SAN JUAN BAUTISTA', '91288', '', '0424-6268956', 'Urb. San Francisco Sector 8 calle 161', 'parish'),
('PZ5-6', 'PARROQUIA SANTO DOMINGO DE GUZMÁN', '31942', 'stodomingogcatolicaparroquia@gmail.com', '0424-6482025, 0424-6247041', 'Urb. La Coromoto calle 171 Nº 48-61', 'parish'),
('PZ5-7', 'PARROQUIA SAN FELIPE NERI', '47397', '', '0414-0626736', 'Urb. San Felipe, San Francisco', 'parish'),
('PZ5-8', 'PARROQUIA NTRA. SRA. DE LA DEL COBRE', '83947', '', '0412-7683972, 0424-6828646', 'Urb. San Francisco, La Popular Av. 53', 'parish'),
('PZ5-9', 'PARROQUIA TRANSFIGURACIÓN DEL SEÑOR', '98472', '', '0414-6237799', 'Km. 13 Vía Perijá Av. 49H, Los Cortijos, Mcpio. San Francisco', 'parish'),
('PZ5-10', 'PARROQUIA SANTA MARIANA DE JESÚS', '72465', 'padrecarlosquiva@gmail.com', '0412-1285174', 'Barrio Sur América, calle 149 con avenida 54A, San Francisco', 'parish'),
('PZ5-11', 'PARROQUIA PURÍSIMA MADRE DE DIOS Y SAN BENITO DE PALERMO', '96997', '', '0414-3688646', 'Final Av. 5 de San Francisco con C/ 55 de El Bajo, vía a la Refinería Bajo Grande', 'parish'),
('PZ6-1', 'PARROQUIA NTRA. SRA. DE FÁTIMA', '88760', 'mcbofatima@gmail.com', '0412-9844169, 0414-6715547', 'Urb. Monte Claro Av. 2', 'parish'),
('PZ6-2', 'PARROQUIA SAN RAMÓN NONATO', '40537', 'sanramonnonato@gmail.com', '0414-3466396, 0414-6388401', 'AV. 1 Monte Bello', 'parish'),
('PZ6-3', 'PARROQUIA LA SANTÍSIMA TRINIDAD', '26072', '', '0424-6704586, 0414-6477288', 'Calle 55 Nº 15J-132 Urb. La Trinidad', 'parish'),
('PZ6-4', 'PARROQUIA NTRA. SRA. DE LA CANDELARIA', '53213', 'hector.bermudez.c@hotmail.com', '0416-1618046, 0261-7573672', 'Urb. San Jacinto, Sector 8 Calle 3', 'parish'),
('PZ6-5', 'PARROQUIA SANTA ROSA DE LIMA / Santa Rita de Casia', '65543', '', '0424-1218537, 0261-7422818', 'Altos del Jalisco, Maracaibo', 'parish'),
('PZ6-6', 'PARROQUIA SAN BARTOLOMÉ (Ziruma)', '88970', '', '0414-6920201, 0261-5254318', 'Ziruma', 'parish'),
('PZ6-7', 'PARROQUIA SAN ONOFRE', '16965', 'mcboparroquiasanonofre@gmail.com', '0412-3670531, 0424-6065719', '', 'parish'),
('PZ6-8', 'PARROQUIA SAN JUAN BOSCO (Sede Seminario Propedéutico)', '26315', 'sanjuanboscomcbo@gmail.com', '0426-8618035, 04143636962', 'Urb. Lago Mar Beach', 'parish'),
('PZ7-1', 'PARROQUIA SAN RAFAEL ARCÁNGEL (El Moján)', '93849', 'padrerafaeljmoralesf@hotmail.com', '0416-6667944, 0262-8721193', 'AV. 2 El Moján, Mcpio. Mara', 'parish'),
('PZ7-3', 'PARROQUIA NTRA. SRA. DE LOURDES (Isla de Toas)', '40923', 'padrerafaeljmoralesf@hotmail.com', '0416-6667944, 0262-8676068', 'Av. Principal Campo Elías, Sector el Toro, Mcpio. Insular Padilla', 'parish'),
('PZ7-6', 'PARROQUIA MARÍA AUXILIADORA (Santa Cruz de Mara)', '33208', '', '0424-6288234', 'Av. Principal Troncal del Caribe Vía al Moján, Santa Cruz de Mara', 'parish');

INSERT INTO parroquias (code, name, password, email, phone, address, role) VALUES
('PZ7-7', 'PARROQUIA LA INMACULADA CONCEPCIÓN (Carrasquero)', '34112', '', '0412-1670969, 0262-9940227', 'Av. Principal frente a la Plaza Bolívar, Carrasquero, Mcpio. Mara', 'parish'),
('PZ7-9', 'PARROQUIA NTRA. SEÑORA DE COROMOTO Y SAN JOSÉ OBRERO (La Sierrita)', '89768', '', '0424-6539582, 0262-8581131', 'La Sierrita, Mcpio. Mara', 'parish'),
('PZ7-10', 'PARROQUIA JESÚS REDENTOR (Tamare)', '79837', 'pquia.jesusredentor@gmail.com', '0416-4617636, 0414-6122354', 'Mcpio. Mara Km. 29', 'parish'),
('PZ8-1', 'PARROQUIA LA INMACULADA CONCEPCIÓN (La Cañada de Urdaneta)', '68244', 'raulalfredo1963@hotmail.com', '0414-6326406, 0412-6582059', 'Av. 1 Gral Rafael Urdaneta, sector la Plaza, La Cañada de Urdaneta', 'parish'),
('PZ8-2', 'PARROQUIA NTRA. SRA. DEL CARMEN (El Carmelo, La Cañada de Urdaneta)', '61749', 'daigelhml@gmail.com', '0414-6483753', 'El Carmelo, Mcpio. Urdaneta', 'parish'),
('PZ8-3', 'PARROQUIA NTRA. SRA. DE CHIQUINQUIRÁ (La Ensenada)', '83570', '', '0414-6089719, 0262-8084331', 'Av. Principal, La Ensenada, Mcpio. Urdaneta', 'parish'),
('PZ8-4', 'PARROQUIA SAN ANTONIO DE PADUA Y NTRA. SRA. VIRGEN DE LOS PARRALES', '26654', '', '0414-1695885, 0414-6266325', 'La Cañada de Urdaneta, Panal del Sur Av. Principal', 'parish'),
('PZ9-1', 'PARROQUIA SAN BARTOLOMÉ APÓSTOL (Sinamaica)', '48345', 'padresantosilva@gmail.com', '0412-1742378, 0414-6452186', 'Av. Principal frente a la Plaza Bolívar, Sinamaica, Mcpio. Páez', 'parish'),
('PZ9-2', 'PARROQUIA SAN JOSÉ DE PARAGUAIPOA', '61589', 'eduardodaboin1991@gmail.com', '0414-6690248, 0262-9691145', 'Paraguaipoa Plaza Bolívar, Mcpio. Páez', 'parish'),
('PZ9-3', 'PARROQUIA EL SAGRADO CORAZÓN DE JESÚS (Guarero)', '53696', '', '0412-7980355', 'Guarero, sector Juamana', 'parish'),
('PZ9-4', 'PARROQUIA SANTA MARÍA (Guana)', '13956', 'else-oresmiluz@hotmail.com', '0426-4604314, 0262-5150815', 'Km. 47 Santa María de Guana, Vía Carrasquero-Guarero', 'parish'),
('PZ9-5', 'Parroquia Personal Eclesiástica Ntra. Sra. del Carmen (Añú)', '26284', 'padresantosilva@gmail.com', '0412-1742378', 'Laguna de Sinamaica, Mcpio. Páez', 'parish'),
('RZ6-10', 'RECTORÍA SAN FRANCISCO DE ASÍS', '82349', '', '', 'Av. Milagro Norte (ZP-6)', 'rectoria'),
('RZ5-13', 'RECTORÍA EL DIVINO NIÑO', '41800', '', '7320586', 'ZP-5 Santísimo Salvador', 'rectoria'),
('RZ4-12', 'RECTORÍA SANTO TOMÁS MORO', '65254', '', '0414-3618152, 0261-7591449', 'Urb. Sucre Calle 62 Nº 130-25 (ZP-4)', 'rectoria'),
('RZ2-10', 'RECTORÍA HOGAR CLÍNICA SAN RAFAEL', '11853', 'familiajuandediana@gmail.com', '0424-6224357, 0261-7911790', 'Calle 64 con Av. 3F (ZP-2)', 'rectoria'),
('RZ5-12', 'RECTORÍA SAN FRANCISCO JAVIER', '53047', '', '0261-8144854', 'Av. Principal Barrio Carabobo (ZP-5)', 'rectoria'),
('RZ7-12', 'RECTORÍA LA SANTÍSIMA CRUZ DE MARA', '96308', '', '0424-6288234', 'Las Cruces, carretera hacia el Moján, Santa Cruz de Mara', 'rectoria'),
('RZ5-11', 'RECTORÍA JESÚS LA BUENA ESPERANZA', '20065', 'padrecarlosquiva@gmail.com', '0412-1285174', 'Barrio El Silencio Av. 49A #152-41, Mcpio. San Francisco', 'rectoria'),
('RZ6-SP', 'RECTORÍA SAN ANTONIO DE PADUA', '23702', '', '', 'ZP-6 Ntra. Sra. de la Candelaria', 'rectoria');
