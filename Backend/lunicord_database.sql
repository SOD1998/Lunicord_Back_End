-- create schemas
CREATE SCHEMA lunicord;
-- create tables
CREATE TABLE lunicord.usuarios (
	id_usuario INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	usuario VARCHAR (10) NOT NULL,
    nombre VARCHAR (30) NOT NULL,
    apellido VARCHAR (30) NOT NULL,
	clave VARCHAR (20) NOT NULL,
	fecha_nacimiento DATE NOT NULL,
    imagen BOOLEAN DEFAULT FALSE,
	email VARCHAR (30) NOT NULL
);
CREATE TABLE lunicord.servidores (
	id_servidor INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR (100) NOT NULL
);
CREATE TABLE lunicord.canales (
	id_canal INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR (100) NOT NULL,
	descripcion VARCHAR (255) NOT NULL,
    id_servidor INT NOT NULL,
    FOREIGN KEY (id_servidor) REFERENCES lunicord.servidores (id_servidor) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE lunicord.chat (
	id_chat INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	mensaje VARCHAR (1000) NOT NULL,
    fecha DATETIME DEFAULT NOW(),
    id_canal INT NOT NULL,
    FOREIGN KEY (id_canal) REFERENCES lunicord.canales (id_canal) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE lunicord.lista_de_usuarios_por_servidor (
	id_usuario INT,
	id_servidor INT,
	PRIMARY KEY (id_usuario, id_servidor),
    FOREIGN KEY (id_usuario) REFERENCES lunicord.usuarios (id_usuario) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (id_servidor) REFERENCES lunicord.servidores (id_servidor) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE lunicord.registro_chats (
	id_usuario INT,
	id_chat INT,
	PRIMARY KEY (id_usuario, id_chat),
    FOREIGN KEY (id_usuario) REFERENCES lunicord.usuarios (id_usuario) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (id_chat) REFERENCES lunicord.chat (id_chat) ON DELETE CASCADE ON UPDATE CASCADE
);