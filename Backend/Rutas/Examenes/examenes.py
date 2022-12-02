from Schemas.Examenes import S_Examenes
from fastapi import APIRouter, status
from Config.Conexion import database
from typing import List
from Modelos.BasedeDatos import examenes as examenesModel
from Modelos.BasedeDatos import usuarios as usuariosModel
from Modelos.BasedeDatos import configuraciones as configuracionesModel
from Modelos.BasedeDatos import materias as materiasModel
from Modelos.BasedeDatos import n_materias as n_materiasModel
from Modelos.BasedeDatos import preguntas as preguntasModel
from Modelos.BasedeDatos import respuestas as respuestasModel
from Modelos.BasedeDatos import tipoUsuarios as tipousuarioModel
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
        query = select(examenesModel, usuariosModel,tipousuarioModel).where(examenesModel.c.profesor == usuariosModel.c.id_Usuario).where(usuariosModel.c.id_TipoUsuario == tipousuarioModel.c.id_TipoUsuario)
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
        query = select(examenesModel, usuariosModel,tipousuarioModel).where(examenesModel.c.profesor == usuariosModel.c.id_Usuario).where(usuariosModel.c.id_TipoUsuario == tipousuarioModel.c.id_TipoUsuario).where(examenesModel.c.id_Examen == id_Examen)
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
            examenNew = i.dict()
            query = insert(examenesModel).values(examenNew)
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
        query = update(examenesModel).where(examenesModel.c.id_Examen == id_Examen).values(examen.dict(exclude_unset=True))
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
    tags=["Configuracion Examen"]
)
async def get_configuraciones():
    try:
        query = select([configuracionesModel, n_materiasModel.c.materia,examenesModel,usuariosModel]).where(materiasModel.c.id_N_Materia == n_materiasModel.c.id_N_Materia).where(configuracionesModel.c.id_Examen == examenesModel.c.id_Examen).where(examenesModel.c.profesor == usuariosModel.c.id_Usuario)
        return await database.fetch_all(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener las configuraciones"}

@examenes.get(
    "/configuraciones/{id_Configuracion}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una configuracion",
    description ="Regresa una configuracion",
    tags=["Configuracion Examen"]
)
async def get_configuracion(id_Configuracion: int):
    try:
        query = select([configuracionesModel, n_materiasModel.c.materia,examenesModel,usuariosModel]).where(materiasModel.c.id_N_Materia == n_materiasModel.c.id_N_Materia).where(configuracionesModel.c.id_Examen == examenesModel.c.id_Examen).where(examenesModel.c.profesor == usuariosModel.c.id_Usuario).where(configuracionesModel.c.id_Configuracion == id_Configuracion)
        return await database.fetch_one(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener la configuracion"}

@examenes.post(
    "/configuraciones/",
    status_code=status.HTTP_201_CREATED,
    summary     ="Crea una configuracion",
    description ="Crea una configuracion",
    tags=["Configuracion Examen"]
)
async def post_configuracion(configuracion: List[S_Examenes.ConfiguracionNew]):
    try:
        for i in configuracion:
            query = insert(configuracionesModel).values(i.dict())
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
    tags=["Configuracion Examen"]
)
async def put_configuracion(id_Configuracion: int, configuracion: S_Examenes.ConfiguracionUpdate):
    try:
        configuracionNew = configuracion.dict(exclude_unset=True)
        query = update(configuracionesModel).where(configuracionesModel.c.id_Configuracion == id_Configuracion).values(configuracionNew)
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
    tags=["Configuracion Examen"]
)
async def delete_configuracion(id_Configuracion: int):
    try:
        query = delete(configuracionesModel).where(configuracionesModel.c.id_Configuracion == id_Configuracion)
        await database.execute(query)
        return {"message": "Configuracion eliminada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al eliminar la configuracion"}