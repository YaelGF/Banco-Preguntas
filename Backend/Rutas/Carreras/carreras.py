from Schemas.Carreras import S_Carreras
from fastapi import APIRouter, status
from Config.Conexion import database
from typing import List
from Modelos.BasedeDatos import carreras as carrerasModel
from Modelos.BasedeDatos import usuarios as usuariosModel
from Modelos.BasedeDatos import tipoUsuarios as tipoUsuariosModel
from sqlalchemy import select, insert, update, delete

carreras = APIRouter()

@carreras.get(
    "/carreras/",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una lista de carreras",
    description ="Regresa una lista de carreras",
    tags=["Carreras"]
)
async def get_carreras():
    try:
        query = select([carrerasModel,usuariosModel,tipoUsuariosModel.c.tipoUsuario]).where(carrerasModel.c.coordinador == usuariosModel.c.id_Usuario).where(usuariosModel.c.id_TipoUsuario == tipoUsuariosModel.c.id_TipoUsuario)
        return await database.fetch_all(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener las carreras"}
    
@carreras.get(
    "/carreras/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una carrera",
    description ="Regresa una carrera",
    tags=["Carreras"]
)
async def get_carrera(id: int):
    try:
        query =  select([carrerasModel,usuariosModel,tipoUsuariosModel.c.tipoUsuario]).where(carrerasModel.c.coordinador == usuariosModel.c.id_Usuario).where(usuariosModel.c.id_TipoUsuario == tipoUsuariosModel.c.id_TipoUsuario).where(carrerasModel.c.id_Carrera == id)
        return await database.fetch_one(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener la carrera"}

@carreras.post(
    "/carreras/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Inserta una nueva carrera",
    description="Inserta una nueva carrera",
    tags=["Carreras"]
)
async def post_carreras(carrera: List[S_Carreras.CarreraNew]):
    try:
        for i in carrera:
            carreraNew = i.dict()
            query = insert(carrerasModel).values(carreraNew)
            await database.execute(query)
        return {"message": "Carrera insertada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al insertar la carrera"}

@carreras.put(
    "/carreras/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Actualiza una carrera",
    description="Actualiza una carrera",
    tags=["Carreras"]
)
async def put_carreras(id: int, carrera: S_Carreras.CarreraUpdate):
    try:
        query = update(carrerasModel).where(carrerasModel.c.id_Carrera == id).values(carrera.dict(exclude_unset=True))
        await database.execute(query)
        return {"message": "Carrera actualizada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al actualizar la carrera"}

@carreras.delete(
    "/carreras/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Elimina una carrera",
    description="Elimina una carrera",
    tags=["Carreras"]
)
async def delete_carreras(id: int):
    try:
        query = delete(carrerasModel).where(carrerasModel.c.id_carrera == id)
        await database.execute(query)
        return {"message": "Carrera eliminada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al eliminar la carrera"}
