from fastapi import Depends, FastAPI , HTTPException, status, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware
from typing import List

import sqlite3 
import os 
from typing import List 
from fastapi import Depends, FastAPI, HTTPException, status 
from fastapi.security import HTTPBasic, HTTPBasicCredentials 
from pydantic import BaseModel 
from typing import Union  


app = FastAPI()

DATABASE_URL = os.path.join("sql/preguntas.sqlite") # Path to the database file

origins = [
    "http://0.0.0.0:8000/",
    "http://127.0.0.1:8000/",
    "*",   
            
    ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Pregunta(BaseModel):

    pregunta    : str
    imagen      : str
    opcion1     : str
    opcion2     : str
    opcion3     : str
    respuesta   : str
    materia     : int
    carrera     : int
    
class PreguntaIn(BaseModel):
    pregunta    : str
    imagen      : str
    opcion1     : str
    opcion2     : str
    opcion3     : str
    respuesta   : str



@app.get("/")
def root():
    return {"message": "Hola"}


#Obtiene las preguntas de la base de datos
@app.get(
    "/preguntas/", 
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una lista de preguntas",
    description ="Regresa una lista de preguntas",
)
#async def get_preguntas(credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
async def get_preguntas():
    try:
        with sqlite3.connect(DATABASE_URL) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM preguntas')
            response = cursor.fetchall()
            return response
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener las preguntas"}

#Obtiene un usuario por medio del id
@app.get(
    "/preguntas/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una pregunta",
    description ="Regresa una pregunta",
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
@app.post("/preguntas/", 
    status_code=status.HTTP_202_ACCEPTED,
    summary="Inserta una nueva pregunta",
    description="Inserta una nueva pregunta",
    tags=["auth"]
)
async def post_preguntas(pregunta: Pregunta):
    try:
        with sqlite3.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO preguntas (pregunta, imagen, opc1, opc2, opc3, respuesta, materia, carrera) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (pregunta.pregunta, pregunta.imagen, pregunta.opcion1, pregunta.opcion2, pregunta.opcion3, pregunta.respuesta, pregunta.materia, pregunta.carrera))
            connection.commit()
            response = cursor.fetchone()
            message = "Pregunta insertada correctamente"
            return {"message": message}
        
    except Exception as error:
        print(f"Error: {error}")
        return(f"Error: {error}")
        
    
