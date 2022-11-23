from Schemas.Examenes import S_Examenes
from fastapi import APIRouter, status
from Config.Conexion import database
from typing import List
from Modelos.BasedeDatos import examenes as examenesModel
from Modelos.BasedeDatos import configuraciones as configuracionesModel
from sqlalchemy import select, insert, update, delete

examenes = APIRouter()

@examenes.get(
    "/examenes/",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una lista de examenes",
    description ="Regresa una lista de examenes",
    tags=["Examenes"]
)
async def get_examenes():
    try:
        query = select(examenesModel)
        return await database.fetch_all(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener los examenes"}

@examenes.get(
    "/examenes/{id_Examen}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa un examen",
    description ="Regresa un examen",
    tags=["Examenes"]
)
async def get_examen(id_Examen: int):
    try:
        query = select(examenesModel).where(examenesModel.c.id_Examen == id_Examen)
        return await database.fetch_one(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener el examen"}

@examenes.post(
    "/examenes/",
    status_code=status.HTTP_201_CREATED,
    summary     ="Crea un examen",
    description ="Crea un examen",
    tags=["Examenes"]
)
async def post_examen(examen: List[S_Examenes.ExamenNew]):
    try:
        for i in examen:
            query = insert(examenesModel).values(
                profesor = i.profesor,
                fecha    = i.fecha,
                horaInicio = i.horaInicio,
                horafin  = i.horaFin,
            )
            await database.execute(query)
        return {"message": "Examen creado correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error"+error+"al crear el examen"}

@examenes.put(
    "/examenes/{id_Examen}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Actualiza un examen",
    description ="Actualiza un examen",
    tags=["Examenes"]
)
async def put_examen(id_Examen: int, examen: S_Examenes.ExamenUpdate):
    try:
        query = update(examenesModel).where(examenesModel.c.id_Examen == id_Examen).values(
            profesor = examen.profesor,
            fecha    = examen.fecha,
            horaInicio = examen.horaInicio,
            horafin  = examen.horaFin,
        )
        await database.execute(query)
        return {"message": "Examen actualizado correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al actualizar el examen"}

@examenes.delete(
    "/examenes/{id_Examen}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Elimina un examen",
    description ="Elimina un examen",
    tags=["Examenes"]
)
async def delete_examen(id_Examen: int):
    try:
        query = delete(examenesModel).where(examenesModel.c.id_Examen == id_Examen)
        await database.execute(query)
        return {"message": "Examen eliminado correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al eliminar el examen"}

@examenes.get(
    "/configuraciones/",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una lista de configuraciones",
    description ="Regresa una lista de configuraciones",
    tags=["Configuraciones"]
)
async def get_configuraciones():
    try:
        query = select(configuracionesModel)
        return await database.fetch_all(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener las configuraciones"}

@examenes.get(
    "/configuraciones/{id_Configuracion}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una configuracion",
    description ="Regresa una configuracion",
    tags=["Configuraciones"]
)
async def get_configuracion(id_Configuracion: int):
    try:
        query = select(configuracionesModel).where(configuracionesModel.c.id_Configuracion == id_Configuracion)
        return await database.fetch_one(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener la configuracion"}

@examenes.post(
    "/configuraciones/",
    status_code=status.HTTP_201_CREATED,
    summary     ="Crea una configuracion",
    description ="Crea una configuracion",
    tags=["Configuraciones"]
)
async def post_configuracion(configuracion: List[S_Examenes.ConfiguracionNew]):
    try:
        for i in configuracion:
            query = insert(configuracionesModel).values(
                id_Examen = i.id_Examen,
                id_Materia = i.id_Materia,
                NoPreguntas = i.NoPreguntas,
            )
            await database.execute(query)
        return {"message": "Configuracion creada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error"+error+"al crear la configuracion"}

@examenes.put(
    "/configuraciones/{id_Configuracion}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Actualiza una configuracion",
    description ="Actualiza una configuracion",
    tags=["Configuraciones"]
)
async def put_configuracion(id_Configuracion: int, configuracion: S_Examenes.ConfiguracionUpdate):
    try:
        query = update(configuracionesModel).where(configuracionesModel.c.id_Configuracion == id_Configuracion).values(
            id_Examen = configuracion.id_Examen,
            id_Materia = configuracion.id_Materia,
            NoPreguntas = configuracion.NoPreguntas,
        )
        await database.execute(query)
        return {"message": "Configuracion actualizada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al actualizar la configuracion"}

@examenes.delete(
    "/configuraciones/{id_Configuracion}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Elimina una configuracion",
    description ="Elimina una configuracion",
    tags=["Configuraciones"]
)
async def delete_configuracion(id_Configuracion: int):
    try:
        query = delete(configuracionesModel).where(configuracionesModel.c.id_Configuracion == id_Configuracion)
        await database.execute(query)
        return {"message": "Configuracion eliminada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al eliminar la configuracion"}