from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from Config.Conexion import engine, meta
 
tipoUsuarios = Table('tipoUsuario', meta, 
Column('id_TipoUsuario', Integer, primary_key=True),
Column('tipoUsuario', String(50)))

usuarios = Table('usuario', meta,
Column('id_Usuario', Integer, primary_key=True),
Column('nombre', String(50)),
Column('apellido', String(50)),
Column('correo', String(50)),
Column('matricula', String(50)),
Column('id_TipoUsuario', String(50), ForeignKey('tipoUsuario.id_TipoUsuario')))

alumnos = Table('alumno', meta,
Column('id_Alumno', Integer, primary_key=True),
Column('id_Usuario', Integer, ForeignKey('usuario.id_Usuario')),
Column('id_Grupo', Integer, ForeignKey('grupo.id_Grupo')))

grupos = Table('grupo', meta,
Column('id_Grupo', Integer, primary_key=True),
Column('nombre', String(50)),
Column('id_Carrera', Integer, ForeignKey('carrera.id_Carrera')))

carreras = Table('carrera', meta,
Column('id_Carrera', Integer, primary_key=True),
Column('carrera', String(50)))
Column('coordinador', Integer, ForeignKey('usuario.id_Usuario'))

materias = Table('materia', meta,
Column('id_Materia', Integer, primary_key=True),
Column('id_N_Materia', Integer, ForeignKey('n_materia.id_N_Materia')),
Column('profesor', Integer, ForeignKey('usuario.id_Usuario')),
Column('id_Carrera', Integer, ForeignKey('carrera.id_Carrera')))

n_materias = Table('n_materia', meta,
Column('id_N_Materia', Integer, primary_key=True),
Column('materia', String(50)),
)

examenen = Table('examen', meta,
Column('id_Examen', Integer, primary_key=True),
Column('profesor', Integer, ForeignKey('usuario.id_Usuario')),
Column('fecha', String(50)),
Column('horaInicio', String(50)),
Column('horaFin', String(50)))

configuraciones = Table('configuracion', meta,
Column('id_Configuracion', Integer, primary_key=True),
Column('id_Examen', Integer, ForeignKey('examen.id_Examen')),
Column('id_Materia', Integer, ForeignKey('materia.id_Materia')),
Column('NoPreguntas', Integer))

resultados = Table('resultado', meta,
Column('id_Resultado', Integer, primary_key=True),
Column('id_Examen', Integer, ForeignKey('examen.id_Examen')),
Column('id_Alumno', Integer, ForeignKey('alumno.id_Alumno')),
Column('calificacion', Integer))

imagenes = Table('imagenes', meta,
Column('id_Imagen', Integer, primary_key=True),
Column('url', String(50)))

preguntas = Table('preguntas', meta,
Column('id_Pregunta', Integer, primary_key=True),
Column('opcion1', Integer, ForeignKey('respuestas.id_Respuesta')),
Column('opcion2', Integer, ForeignKey('respuestas.id_Respuesta')),
Column('opcion3', Integer, ForeignKey('respuestas.id_Respuesta')),
Column('opcion4', Integer, ForeignKey('respuestas.id_Respuesta')),
Column('opcionCorrecta', String(50)),
Column('id_materia', Integer, ForeignKey('materia.id_Materia')))

respuestas = Table('respuestas', meta,
Column('id_Respuesta', Integer, primary_key=True),
Column('respuesta', String(50)))

preguntas_imagenes = Table('preguntas_imagenes', meta,
Column('id_Pregunta_Imagen', Integer, primary_key=True),
Column('id_Pregunta', Integer, ForeignKey('preguntas.id_Pregunta')),
Column('id_Imagen', Integer, ForeignKey('imagenes.id_Imagen')))

meta.create_all(engine)