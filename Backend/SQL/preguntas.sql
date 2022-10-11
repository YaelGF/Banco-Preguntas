CREATE TABLE IF NOT EXISTS preguntas(
    id_preg	 		INTEGER		    PRIMARY KEY AUTOINCREMENT NOT NULL,
    pregunta	 	VARCHAR(255) 	NOT NULL,
    opcion1			VARCHAR(75)		NOT NULL,
    opcion2			VARCHAR(75)		NOT NULL,
    opcion3			VARCHAR(75)		NOT NULL,
    opcionc 		VARCHAR(75) 	NOT NULL,
    id_materia      INTEGER         NOT NULL,
    FOREIGN KEY (id_materia) REFERENCES materias(id_materia)
    
);

CREATE TABLE IF NOT EXISTS preguntas_imagenes(
    id_preg_imagenes	INTEGER		        PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_preg			    INTEGER			    NOT NULL,
    imagen			    VARCHAR(250)		NOT NULL,
    FOREIGN KEY (id_preg) REFERENCES preguntas(id_preg)
);


CREATE TABLE IF NOT EXISTS materias(
    id_materia	 		INTEGER		    PRIMARY KEY AUTOINCREMENT NOT NULL,
    materia	 		VARCHAR(75) 	    NOT NULL,
    id_carrera      INTEGER, 
    FOREIGN KEY (id_carrera) REFERENCES carrera (id_carrera)
);

insert into materias(materia) values('Matematicas');

CREATE TABLE IF NOT EXISTS carreras(
    id_carrera	 		INTEGER		    PRIMARY KEY AUTOINCREMENT NOT NULL,
    carrera	 		VARCHAR(75) 	NOT NULL
);

insert into carreras(carrera) values('Ingenieria en Sistemas Computacionales');

CREATE TABLE IF NOT EXISTS alumnos(
    id_alum	 		INTEGER		    PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre	 		VARCHAR(75) 	NOT NULL,
    apellido		VARCHAR(75) 	NOT NULL,
    matricula		VARCHAR(75) 	NOT NULL,
    id_carrera         INTEGER         NOT NULL,
    FOREIGN KEY (id_carrera) REFERENCES carreras(id_carrera)
);

CREATE TABLE IF NOT EXISTS profesores(
    id_prof	 		INTEGER		    PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre	 		VARCHAR(75) 	NOT NULL,
    apellido		VARCHAR(75) 	NOT NULL,
    matricula		VARCHAR(75) 	NOT NULL
    
);

CREATE TABLE IF NOT EXISTS Asignacion_P_M(
    id_asignacion	INTEGER		    PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_prof	 		INTEGER		    NOT NULL,
    id_materia		INTEGER		    NOT NULL,
    FOREIGN KEY (id_prof) REFERENCES profesores(id_prof),
    FOREIGN KEY (id_materia) REFERENCES materias(id_materia)
);

