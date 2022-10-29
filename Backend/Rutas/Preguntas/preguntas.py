from fastapi import APIRouter

preguntas = APIRouter()

#Obtiene las preguntas de la base de datos
@preguntas.get(
    "/preguntas/", 
    #status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una lista de preguntas",
    description ="Regresa una lista de preguntas",
    tags        =["Preguntas"]
)
#async def get_preguntas(credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
async def get_preguntas():
    return "Hola"
    """try:
        with sqlite3.connect(DATABASE_URL) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM preguntas')
            response = cursor.fetchall()
            return response
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener las preguntas"}

#Obtiene una pregunta por medio del id
@preguntas.get(
    "/preguntas/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una pregunta",
    description ="Regresa una pregunta",
    tags=["Preguntas"]
)
async def get_pregunta(id: int):
    try:
        with sqlite3.connect(DATABASE_URL) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM preguntas WHERE id_preg = ?', (id,))
            response = cursor.fetchone()
            return response
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener la pregunta"}


#Inserta una nueva pregunta a la base de datos
@preguntas.post("/preguntas/", 
    status_code=status.HTTP_202_ACCEPTED,
    summary="Inserta una nueva pregunta",
    description="Inserta una nueva pregunta",
    tags=["Preguntas"]
)
async def post_preguntas(pregunta: Schemas.Pregunta):
    try:
        with sqlite3.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO preguntas (pregunta, opcion1, opcion2, opcion3, opcionc, id_materia) VALUES (?, ?, ?, ?, ?, ?)', (pregunta.pregunta, pregunta.opcion1, pregunta.opcion2, pregunta.opcion3, pregunta.opcionc, pregunta.materia))
            connection.commit()
            response = cursor.fetchone()
            message = "Pregunta insertada correctamente"
            return {"message": message}
        
    except Exception as error:
        print(f"Error: {error}")
        return(f"Error: {error}")"""