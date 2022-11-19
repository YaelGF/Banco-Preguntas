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






/*Base de datos Brandon*/

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

CREATE TABLE IF NOT EXISTS preguntas_r(
    id_preg_r            INTEGER		        PRIMARY KEY AUTOINCREMENT NOT NULL,
    pregunta			 VARCHAR(75)		    NOT NULL,
    id_materia           INTEGER                NOT NULL,
    FOREIGN KEY (id_materia) REFERENCES materias(id_materia)
);

CREATE TABLE IF NOT EXISTS opciones(
    id_preg_opciones	INTEGER		        PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_preg_r		    INTEGER			    NOT NULL,
    opcion1             VARCHAR(75)		    NOT NULL,
    opcion2             VARCHAR(75)		    NOT NULL,
    opcion3             VARCHAR(75)		    NOT NULL,
    opcionc             VARCHAR(75)		    NOT NULL,
    FOREIGN KEY (id_preg_r) REFERENCES preguntas_r(id_preg_r)
);

/*Procedimiento almacenado que inserte registros en la tabla preguntas_r y en la tabla opciones*/

DELIMITER //
DROP PROCEDURE IF EXISTS insertar_preguntas_r//
CREATE PROCEDURE insertar_preguntas_r(
    @pregunta   VARCHAR(255),
    @opcion1    VARCHAR(75),
    @opcion2    VARCHAR(75),
    @opcion3    VARCHAR(75),
    @opcionc    VARCHAR(75),
    @id_materia INTEGER
)
BEGIN
    DECLARE id_preg_r INTEGER;
    INSERT INTO preguntas_r(pregunta, id_materia) VALUES(@pregunta, @id_materia);
    SET id_preg_r = LAST_INSERT_ID();
    INSERT INTO opciones(id_preg_r, opcion1, opcion2, opcion3, opcionc) VALUES(id_preg_r, @opcion1, @opcion2, @opcion3, @opcionc);
    
END
//
DELIMITER ;




/*Procedimiento almacenado que inserte registros en la tabla preguntas y en la tabla preguntas_imagenes*/
/*
CREATE PROCEDURE insertar_preguntas
(
    @pregunta VARCHAR(255),
    @opcion1 VARCHAR(75),
    @opcion2 VARCHAR(75),
    @opcion3 VARCHAR(75),
    @opcionc VARCHAR(75),
    @imagen VARCHAR(250),
    @id_materia INTEGER
)
AS
BEGIN
    BEGIN TRY
        BEGIN TRANSACTION
            INSERT INTO preguntas(pregunta, opcion1, opcion2, opcion3, opcionc, id_materia) VALUES(@pregunta, @opcion1, @opcion2, @opcion3, @opcionc, @id_materia);
            INSERT INTO preguntas_imagenes(id_preg, imagen) VALUES(@id_preg, @imagen);
        COMMIT TRANSACTION
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION
        SELECT ERROR_NUMBER() AS ErrorNumber, ERROR_MESSAGE() AS ErrorMessage;
    END CATCH
END
*/
/*Inserta dos registros en el procedimiento almacenado insertar_preguntas_r*/

EXEC insertar_preguntas_r '¿Cuál es el nombre de la mascota de la familia Simpson?', 'Pluto', 'Garfield', 'Santa Claus', 'Santa Claus', 1;

EXEC insertar_preguntas_r '¿Quíen descubrío America?', 'Pluto', 'Juan', 'Cristobal Colon', 'Americo Vespusio', 1;



/*prueba de tabla
CREATE TABLE IF NOT EXISTS preguntas_con_imagenes(
    id_preg_con_imagenes	INTEGER		        PRIMARY KEY AUTOINCREMENT NOT NULL,
    imagen                  VARCHAR(250)		    NULL,
    pregunta			    VARCHAR(255)		NOT NULL,
    opcion1			        VARCHAR(75)		    NOT NULL,
    opcion2			        VARCHAR(75)		    NOT NULL,
    opcion3			        VARCHAR(75)		    NOT NULL,
    opcionc 			     VARCHAR(75) 	    NOT NULL,
    id_materia              INTEGER             NOT NULL,
    FOREIGN KEY (id_materia) REFERENCES materias(id_materia)
);*/

CREATE TABLE IF NOT EXISTS materias(
    id_materia	 		INTEGER		    PRIMARY KEY AUTOINCREMENT NOT NULL,
    materia	 		VARCHAR(75) 	    NOT NULL,
    id_carrera      INTEGER, 
    FOREIGN KEY (id_carrera) REFERENCES carreras (id_carrera)
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



