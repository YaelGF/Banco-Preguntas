from Schemas.Materias import S_Materias
from fastapi import APIRouter, status
from Config.Conexion import database
from typing import List
from Modelos.BasedeDatos import materias as materiasModel
from Modelos.BasedeDatos import n_materias as n_materiasModel
from Modelos.BasedeDatos import grupos as gruposModel
from Modelos.BasedeDatos import carreras as carrerasModel
from Modelos.BasedeDatos import usuarios as usuariosModel
from sqlalchemy import select, insert, update, delete

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
        
        query = select([materiasModel.c.id_Materia,usuariosModel.c.id_Usuario,usuariosModel.c.nombre,n_materiasModel.c.materia,gruposModel.c.grupo,carrerasModel.c.carrera]).where(materiasModel.c.id_N_Materia == n_materiasModel.c.id_N_Materia).where(materiasModel.c.id_Grupo == gruposModel.c.id_Grupo).where(gruposModel.c.id_Carrera == carrerasModel.c.id_Carrera).where(materiasModel.c.profesor == usuariosModel.c.id_Usuario)
        return await database.fetch_all(query)
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
        query = select([materiasModel.c.id_Materia,usuariosModel.c.nombre,n_materiasModel.c.materia,gruposModel.c.grupo,carrerasModel.c.carrera]).where(materiasModel.c.id_N_Materia == n_materiasModel.c.id_N_Materia).where(materiasModel.c.id_Grupo == gruposModel.c.id_Grupo).where(gruposModel.c.id_Carrera == carrerasModel.c.id_Carrera).where(materiasModel.c.profesor == usuariosModel.c.id_Usuario).where(materiasModel.c.id_Materia == id)
        return await database.fetch_one(query)
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
async def post_materias(materia: List[S_Materias.MateriaNew]):
    try:
        for i in materia:
            materiaNew = i.dict()
            query = insert(materiasModel).values(materiaNew)
            await database.execute(query)
        return {"message": "Materia insertada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al insertar la materia"}

@materias.put(
    "/materias/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Actualiza una materia",
    description="Actualiza una materia",
    tags=["Materias"]
)
async def put_materias(id: int, materiaM: S_Materias.MateriaNewF):
    try:
        query = delete(materiasModel).where(materiasModel.c.id_Materia == id)
        await database.execute(query)
        query = select(n_materiasModel).where(n_materiasModel.c.materia == materiaM.materia)
        materia = await database.fetch_one(query)
        if materia != None:
            query = insert(materiasModel).values({'id_N_Materia': materia['id_N_Materia'], 'profesor': materiaM.profesor, 'id_Grupo': materiaM.id_Grupo})
            await database.execute(query)
            return {"message": "Materia insertada correctamente"}
        query = insert(n_materiasModel).values({'materia': materiaM.materia})
        await database.execute(query)
        query = select(n_materiasModel).where(n_materiasModel.c.materia == materiaM.materia)
        materia = await database.fetch_one(query)
        query = insert(materiasModel).values({'id_N_Materia': materia['id_N_Materia'], 'profesor': materiaM.profesor, 'id_Grupo': materiaM.id_Grupo})
        await database.execute(query)
        return {"message": "Materia insertada correctamente"}

    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al actualizar la materia"}

@materias.delete(
    "/materias/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Elimina una materia",
    description="Elimina una materia",
    tags=["Materias"]
)
async def delete_materias(id: int):
    try:
        query = delete(materiasModel).where(materiasModel.c.id_Materia == id)
        await database.execute(query)
        return {"message": "Materia eliminada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al eliminar la materia"}

@materias.get(
    "/nombre_materias/",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una lista de Nombres de materias",
    description ="Regresa una lista de Nombres de materias",
    tags=["Nombre Materias"]
)
async def get_n_materias():
    try:
        query = select(n_materiasModel)
        return await database.fetch_all(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener las materias"}

@materias.get(
    "/nombre_materias/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una materia",
    description ="Regresa una materia",
    tags=["Nombre Materias"]
)
async def get_n_materia(id: int):
    try:
        query = select(n_materiasModel).where(n_materiasModel.c.id_N_Materia == id)
        return await database.fetch_one(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener la materia"}
    
@materias.post(
    "/nombre_materias/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Inserta una nueva materia",
    description="Inserta una nueva materia",
    tags=["Nombre Materias"]
)
async def post_n_materias(materia:List[S_Materias.N_MateriaNew]):
    try:
        for i in materia:
            query = insert(n_materiasModel).values(i.dict())
            await database.execute(query)
        return {"message": "Materias insertada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al insertar la materia"}
    
@materias.put(
    "/nombre_materias/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Actualiza una materia",
    description="Actualiza una materia",
    tags=["Nombre Materias"]
)
async def put_n_materias(id: int, materia: S_Materias.N_MateriaUpdate):
    try:
        query = update(n_materiasModel).where(n_materiasModel.c.id_N_Materia == id).values(materia.dict(exclude_unset=True))
        await database.execute(query)
        return {"message": "Materia actualizada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al actualizar la materia"}

@materias.delete(
    "/nombre_materias/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Elimina una materia",
    description="Elimina una materia",
    tags=["Nombre Materias"]
)
async def delete_n_materias(id: int):
    try:
        query = delete(n_materiasModel).where(n_materiasModel.c.id_N_Materia == id)
        await database.execute(query)
        return {"message": "Materia eliminada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al eliminar la materia"}


@materias.post(
    "/materias/Front/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Inserta una nueva materia",
    description="Inserta una nueva materia",
    tags=["Materias"]
)
async def post_materias_Front(materiaN: S_Materias.MateriaNewF):
    try:
        query = select(n_materiasModel).where(n_materiasModel.c.materia == materiaN.materia)
        materia = await database.fetch_one(query)
        print(materia)
        if materia != None:
            query = insert(materiasModel).values({'id_N_Materia': materia['id_N_Materia'], 'profesor': materiaN.profesor, 'id_Grupo': materiaN.id_Grupo})
            await database.execute(query)
            return {"message": "Materia insertada correctamente"}
        query = insert(n_materiasModel).values({'materia': materiaN.materia})
        await database.execute(query)
        query = select(n_materiasModel).where(n_materiasModel.c.materia == materiaN.materia)
        materia = await database.fetch_one(query)
        query = insert(materiasModel).values({'id_N_Materia': materia['id_N_Materia'], 'profesor': materiaN.profesor, 'id_Grupo': materiaN.id_Grupo})
        await database.execute(query)
        return {"message": "Materia insertada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al insertar la materia"}