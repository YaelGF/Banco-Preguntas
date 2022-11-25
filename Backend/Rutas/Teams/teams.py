from Schemas.Grupos import S_Grupos
from fastapi import APIRouter, status
from Config.Conexion import database
from typing import List
from Modelos.BasedeDatos import grupos as gruposModel
from Modelos.BasedeDatos import carreras as carrerasModel
from sqlalchemy import select, insert, update, delete

groups = APIRouter()

@groups.get(
    "/grupos/",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una lista de grupos",
    description ="Regresa una lista de grupos",
    tags=["Grupos"]
)
async def get_grupos():
    try:
        #select([gruposModel.c.grupo,gruposModel.c.semestre, carrerasModel.c.carrera]).where(gruposModel.c.id_Carrera == carrerasModel.c.id_Carrera)
        query = select(gruposModel)
        return await database.fetch_all(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener los grupos"}

@groups.get(
    "/grupos/{id_Grupo}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa un grupo",
    description ="Regresa un grupo",
    tags=["Grupos"]
)
async def get_grupo(id_Grupo: int):
    try:
        query = select(gruposModel).where(gruposModel.c.id_Grupo == id_Grupo)
        return await database.fetch_one(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener el grupo"}

@groups.post(
    "/grupos/",
    status_code=status.HTTP_201_CREATED,
    summary     ="Crea un grupo",
    description ="Crea un grupo",
    tags=["Grupos"]
)
async def post_grupo(grupo: List[S_Grupos.GrupoNew]):
    try:
        for i in grupo:
            grupoNew = i.dict()
            query = insert(gruposModel).values(grupoNew)
            await database.execute(query)
        return {"message": "Grupos creado correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error"+error+"al crear el grupo"}

@groups.put(
    "/grupos/{id_Grupo}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Actualiza un grupo",
    description ="Actualiza un grupo",
    tags=["Grupos"]
)
async def put_grupo(id_Grupo: int, grupo: S_Grupos.GrupoUpdate):
    try:
        grupoUpdate = grupo.dict(exclude_unset=True)
        query = update(gruposModel).where(gruposModel.c.id_Grupo == id_Grupo).values(grupoUpdate)
        await database.execute(query)
        return {"message": "Grupo actualizado correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al actualizar el grupo"}

@groups.delete(
    "/grupos/{id_Grupo}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Elimina un grupo",
    description ="Elimina un grupo",
    tags=["Grupos"]
)
async def delete_grupo(id_Grupo: int):
    try:
        query = delete(gruposModel).where(gruposModel.c.id_Grupo == id_Grupo)
        await database.execute(query)
        return {"message": "Grupo eliminado correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al eliminar el grupo"}


