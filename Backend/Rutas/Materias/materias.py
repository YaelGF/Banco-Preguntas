from Config.Conexion import Conexion
from Schemas import Schemas
from fastapi import APIRouter, status
import sqlite3

materias = APIRouter()

@materias.get(
    "/materias/",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una lista de materias",
    description ="Regresa una lista de materias",
    tags=["Materias"]
)
async def get_materias():
    try:
        with sqlite3.connect(Conexion) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM materias')
            response = cursor.fetchall()
            return response
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener las materias"}

@materias.get(
    "/materias/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una materia",
    description ="Regresa una materia",
    tags=["Materias"]
)
async def get_materia(id: int):
    try:
        with sqlite3.connect(Conexion) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM materias WHERE id_materia = ?', (id,))
            response = cursor.fetchone()
            return response
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener la materia"}

@materias.post(
    "/materias/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Inserta una nueva materia",
    description="Inserta una nueva materia",
    tags=["Materias"]
)
async def post_materias(materia: Schemas.MateriaNew):
    try:
        with sqlite3.connect(Conexion) as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO materias (materia,id_carrera) VALUES (?,?)', ( materia.materia, materia.id_carrera))
            connection.commit()
            message = "Materia insertada correctamente"
            return {"message": message}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al insertar la materia"}
