Drop table if exists usuarios;
CREATE TABLE usuarios(
    email TEXT,
    password varchar(32),
    rol varchar(10)
);

CREATE UNIQUE INDEX index_usuario ON usuarios(email);

INSERT INTO usuarios(email, password, rol) VALUES('admin@utectulancingo.edu.mx','123456','Admin');
INSERT INTO usuarios(email, password, rol) VALUES('profesor@utectulancingo.edu.mx','123456','Profesor');
INSERT INTO usuarios(email, password, rol) VALUES('1719110736@utectulancingo.edu.mx','123456','user');

SELECT * FROM usuarios;