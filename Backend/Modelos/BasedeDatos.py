from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Float
from Config.Conexion import engine, meta
 
tipoUsuarios = Table('tipoUsuarios', meta, 
Column('id_TipoUsuario', Integer, primary_key=True),
Column('tipoUsuario', String(50)))

usuarios = Table('usuarios', meta,
Column('id_Usuario', Integer, primary_key=True),
Column('nombre', String(50)),
Column('uid', String),
Column('apellidoPaterno', String(50)),
Column('apellidoMaterno', String(50)),
Column('email', String(50)),
Column('matricula', String(50)),
Column('id_TipoUsuario', Integer, ForeignKey('tipoUsuarios.id_TipoUsuario')))

alumnos = Table('alumnos', meta,
Column('id_Alumno', Integer, primary_key=True),
Column('id_Usuario', Integer, ForeignKey('usuarios.id_Usuario')),
Column('id_Grupo', Integer, ForeignKey('grupos.id_Grupo')))

grupos = Table('grupos', meta,
Column('id_Grupo', Integer, primary_key=True),
Column('grupo', String(50)),
Column('semestre', String(50)),
Column('id_Carrera', Integer, ForeignKey('carreras.id_Carrera')))

carreras = Table('carreras', meta,
Column('id_Carrera', Integer, primary_key=True),
Column('carrera', String(50)),
Column('coordinador', Integer, ForeignKey('usuarios.id_Usuario')))

materias = Table('materias', meta,
Column('id_Materia', Integer, primary_key=True),
Column('id_N_Materia', Integer, ForeignKey('n_materias.id_N_Materia')),
Column('profesor', Integer, ForeignKey('usuarios.id_Usuario')),
Column('id_Grupo', Integer, ForeignKey('grupos.id_Grupo')))

n_materias = Table('n_materias', meta,
Column('id_N_Materia', Integer, primary_key=True),
Column('materia', String(50)),
)

examenes = Table('examenes', meta,
Column('id_Examen', Integer, primary_key=True),
Column('profesor', Integer, ForeignKey('usuarios.id_Usuario')),
Column('id_Materia', Integer, ForeignKey('materias.id_Materia')),
Column('id_Grupo', Integer, ForeignKey('grupos.id_Grupo')),
Column('fecha', String(50)),
Column('horaInicio', String(50)),
Column('horaFin', String(50)))

configuraciones = Table('configuraciones', meta,
Column('id_Configuracion', Integer, primary_key=True),
Column('id_Examen', Integer, ForeignKey('examenes.id_Examen')),
Column('id_Materia', Integer, ForeignKey('materias.id_Materia')),
Column('NoPreguntas', Integer))

resultados = Table('resultados', meta,
Column('id_Resultado', Integer, primary_key=True),
Column('id_Examen', Integer, ForeignKey('examenes.id_Examen')),
Column('id_Alumno', Integer, ForeignKey('alumnos.id_Alumno')),
Column('calificacion', Float))

imagenes = Table('imagenes', meta,
Column('id_Imagen', Integer, primary_key=True),
Column('url', String(300)))

preguntas = Table('preguntas', meta,
Column('id_Pregunta', Integer, primary_key=True),
Column('pregunta', String(300)),
Column('opcion1', Integer, ForeignKey('respuestas.id_Respuesta')),
Column('opcion2', Integer, ForeignKey('respuestas.id_Respuesta')),
Column('opcion3', Integer, ForeignKey('respuestas.id_Respuesta')),
Column('opcion4', Integer, ForeignKey('respuestas.id_Respuesta')),
Column('opcionCorrecta', Integer, ForeignKey('respuestas.id_Respuesta')),
Column('id_Materia', Integer, ForeignKey('materias.id_Materia')))

respuestas = Table('respuestas', meta,
Column('id_Respuesta', Integer, primary_key=True),
Column('respuesta', String(50)))

preguntas_imagenes = Table('preguntas_imagenes', meta,
Column('id_Pregunta_Imagen', Integer, primary_key=True),
Column('id_Pregunta', Integer, ForeignKey('preguntas.id_Pregunta')),
Column('id_Imagen', Integer, ForeignKey('imagenes.id_Imagen')))

meta.create_all(engine)