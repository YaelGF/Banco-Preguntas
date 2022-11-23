from Schemas.Examenes import S_Examenes
from fastapi import APIRouter, status
from Config.Conexion import database
from typing import List
from Modelos.BasedeDatos import resultados as resulModel
from sqlalchemy import select, insert, update, delete

resultados = APIRouter()

@resultados.get(
    "/resultados/",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una lista de resultados",
    description ="Regresa una lista de resultados",
    tags=["Resultados"]
)
async def get_resultados():
    try:
        query = select(resulModel)
        return await database.fetch_all(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener los resultados"}

@resultados.get(
    "/resultados/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa un resultado",
    description ="Regresa un resultado",
    tags=["Resultados"]
)
async def get_resultado(id: int):
    try:
        query = select(resulModel).where(resulModel.c.id == id)
        return await database.fetch_one(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener el resultado"}
    
@resultados.post(
    "/resultados/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Inserta un nuevo resultado",
    description="Inserta un nuevo resultado",
    tags=["Resultados"]
)
async def post_resultados(resultado: List[S_Examenes.ResultadoNew]):
    try:
        for i in resultado:
            query = insert(resulModel).values(
                id_Examen=i.id_Examen,
                id_Alumno=i.id_Alumno,
                calificacion=i.calificacion
            )
            await database.execute(query)
        return {"message": "Resultado insertado correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al insertar el resultado"}
    
@resultados.put(
    "/resultados/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Actualiza un resultado",
    description="Actualiza un resultado",
    tags=["Resultados"]
)
async def put_resultados(id: int, resultado: S_Examenes.ResultadoUpdate):
    try:
        query = update(resulModel).where(resulModel.c.id == id).values(
            id_Examen=resultado.id_Examen,
            id_Alumno=resultado.id_Alumno,
            calificacion=resultado.calificacion
        )
        await database.execute(query)
        return {"message": "Resultado actualizado correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al actualizar el resultado"}
