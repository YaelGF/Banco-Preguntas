
CREATE TABLE IF NOT EXISTS preguntas(
    id_preg	 		INTEGER		    PRIMARY KEY AUTOINCREMENT NOT NULL,
    pregunta	 	VARCHAR(255) 	NOT NULL,
    imagen          VARCHAR(200)	NULL,
    opc1			VARCHAR(75)		NOT NULL,
    opc2			VARCHAR(75)		NOT NULL,
    opc3			VARCHAR(75)		NOT NULL,
    respuesta		VARCHAR(75) 	NOT NULL,
    materia         INTEGER         NOT NULL,
    carrera         INTEGER         NOT NULL,
    FOREIGN KEY (materia) REFERENCES materias(id_mat),
    FOREIGN KEY (carrera) REFERENCES carreras(id_car)
);

CREATE TABLE IF NOT EXISTS respuestas(
    id_res	 		INTEGER		    PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_preg	 		INTEGER		    NOT NULL,
    id_alum	 		INTEGER		    NOT NULL,
    respuesta		VARCHAR(75) 	NOT NULL,
    FOREIGN KEY (id_preg) REFERENCES preguntas(id_preg),
    FOREIGN KEY (id_alum) REFERENCES alumnos(id_alum)
);

CREATE TABLE IF NOT EXISTS materias(
    id_mat	 		INTEGER		    PRIMARY KEY AUTOINCREMENT NOT NULL,
    materia	 		VARCHAR(75) 	NOT NULL
);

insert into materias(materia) values('Matematicas');

CREATE TABLE IF NOT EXISTS carreras(
    id_car	 		INTEGER		    PRIMARY KEY AUTOINCREMENT NOT NULL,
    carrera	 		VARCHAR(75) 	NOT NULL
);

insert into carreras(carrera) values('Ingenieria en Sistemas Computacionales');

CREATE TABLE IF NOT EXISTS alumnos(
    id_alum	 		INTEGER		    PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre	 		VARCHAR(75) 	NOT NULL,
    apellido		VARCHAR(75) 	NOT NULL,
    matricula		VARCHAR(75) 	NOT NULL,
    carrera         INTEGER         NOT NULL,
    FOREIGN KEY (carrera) REFERENCES carreras(id_car)
);

CREATE TABLE IF NOT EXISTS profesores(
    id_prof	 		INTEGER		    PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre	 		VARCHAR(75) 	NOT NULL,
    apellido		VARCHAR(75) 	NOT NULL,
    matricula		VARCHAR(75) 	NOT NULL,
    carrera         INTEGER         NOT NULL,
    FOREIGN KEY (carrera) REFERENCES carreras(id_car)
);

