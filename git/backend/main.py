from random import random
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
import random


app = FastAPI()

DATABASE_URL = os.path.join("sql/preguntas.sqlite") # Path to the database file

origins = [
    "http://0.0.0.0:8000/",
    "http://0.0.0.0:8080/",
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
    opcion1     : str
    opcion2     : str
    opcion3     : str
    opcionc     : str
    materia     : int

class Calificar_Preguntas(BaseModel):
    id_pregunta : int
    respuesta   : str





@app.get("/")
def root():
    return {"message": "Esta es una API de Banco de Preguntas"}


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
            cursor      = connection.cursor()
            preguntas_p = []
            opciones_p  = []
            preg_opc    = {}
            #cursor.execute('SELECT * FROM preguntas ORDER BY RANDOM() LIMIT 10')
            cursor.execute('SELECT * FROM preguntas ORDER BY RANDOM()')
            preguntas = cursor.fetchall()
            for pregunta in preguntas:
                preguntas_p.append(pregunta)
                cursor.execute('SELECT opcion1, opcion2, opcion3, opcionc from preguntas  WHERE id_preg = ?', (pregunta['id_preg'],))
                opciones = cursor.fetchall()
                for opcion in opciones:
                    opciones_p.append(opcion)
            preg_opc['preguntas']   = preguntas_p
            return preg_opc

    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener las preguntas"}




#Obtiene una pregunta por medio del id
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
            cursor.execute('INSERT INTO preguntas (pregunta, opcion1, opcion2, opcion3, opcionc, id_materia) VALUES (?, ?, ?, ?, ?, ?)', (pregunta.pregunta, pregunta.opcion1, pregunta.opcion2, pregunta.opcion3, pregunta.opcionc, pregunta.materia))
            connection.commit()
            response = cursor.fetchone()
            message = "Pregunta insertada correctamente"
            return {"message": message}
        
    except Exception as error:
        print(f"Error: {error}")
        return(f"Error: {error}")


#Obtiene las preguntas de la base de datos
@app.get(
    "/materias/",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una lista de materias",
    description ="Regresa una lista de materias",
)
async def get_materias():
    try:
        with sqlite3.connect(DATABASE_URL) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM materias')
            response = cursor.fetchall()
            return response
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener las materias"}



#calificar respuestas
@app.post(
    "/calificar/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Califica las respuestas",
    description="Califica las respuestas",
    tags=["auth"]
)
async def calificar_respuestas(calificar: Calificar_Preguntas):
    
    try:
        with sqlite3.connect(DATABASE_URL) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            correctas = 0
            for respuesta in calificar:
                cursor.execute('SELECT opcionc FROM preguntas WHERE id_preg = ?', (respuesta.id_pregunta,))
                response = cursor.fetchone()
                if response[0] == 1:
                    correctas += 1
                return {"correctas": correctas}
                
    except Exception as error:
        print(f"Error: {error}")
        return(f"Error: {error}")



#CALIFICAR RESPUESTAS CON UNA PREGUNTA
"""
@app.post("/calificar/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Califica una respuesta",
    description="Califica una respuesta",
    tags=["auth"]
)

async def calificar_respuesta(id: int, respuesta: str):
    try:
        with sqlite3.connect(DATABASE_URL) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM preguntas WHERE id_preg = ?', (id,))
            response = cursor.fetchone()
            if response['opcionc'] == respuesta:
                return {"correcta": True}
            else:
                return {"incorrecta": False}
    except Exception as error:
        print(f"Error: {error}")
        return(f"Error: {error}")

"""
