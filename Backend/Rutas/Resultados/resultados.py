from Schemas.Examenes import S_Examenes
from fastapi import APIRouter, status
from Config.Conexion import database
from typing import List
from Modelos.BasedeDatos import resultados as resulModel
from Modelos.BasedeDatos import alumnos as alumnosModel
from Modelos.BasedeDatos import examenes as examenesModel
from Modelos.BasedeDatos import usuarios as usuariosModel
from Modelos.BasedeDatos import n_materias as n_materiasModel
from Modelos.BasedeDatos import materias as materiasModel
from Modelos.BasedeDatos import grupos as gruposModel
from Modelos.BasedeDatos import carreras as carrerasModel
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
        query = select([resulModel,examenesModel,n_materiasModel]).where(resulModel.c.id_Examen == examenesModel.c.id_Examen).where(examenesModel.c.id_Materia == materiasModel.c.id_Materia).where(materiasModel.c.id_N_Materia == n_materiasModel.c.id_N_Materia)
        resultados = await database.fetch_all(query)
        newResultados = []
        for i in resultados:
            query = select([gruposModel]).where(gruposModel.c.id_Grupo == i["id_Grupo"])
            grupo = await database.fetch_one(query)
            query = select([carrerasModel]).where(carrerasModel.c.id_Carrera == grupo["id_Carrera"])
            carrera = await database.fetch_one(query)
            query = select([usuariosModel]).where(usuariosModel.c.id_Usuario == i["profesor"])
            profesor = await database.fetch_one(query)
            query = select([alumnosModel]).where(alumnosModel.c.id_Alumno == i["id_Alumno"])
            alumno = await database.fetch_one(query)
            if(alumno != None):
                query = select([usuariosModel]).where(usuariosModel.c.id_Usuario == alumno["id_Usuario"])
                usuarioAlumno = await database.fetch_one(query)
                data = {
                    "id_Resultado": i["id_Resultado"],
                    "Alumno": usuarioAlumno["nombre"],
                    "Matricula_Alumno": usuarioAlumno["matricula"],
                    "Calificacion": i["calificacion"],
                    "Hora_Inicio": i["horaInicio"],
                    "Hora_Fin": i["horaFin"],
                    "Fecha": i["fecha"],
                    "Materia": i["materia"],
                    "Profesor": profesor["nombre"],
                    "Grupo": grupo["grupo"],
                    "Semestre": grupo["semestre"],
                    "Carrera": carrera["carrera"]
                    }
                newResultados.append(data)

        return newResultados

                
        
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
        query = select(resulModel).where(resulModel.c.id_Resultado == id)
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
            query = insert(resulModel).values(i.dict())
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
        query = update(resulModel).where(resulModel.c.id_Resultado == id).values(resultado.dict(exclude_unset=True))
        await database.execute(query)
        return {"message": "Resultado actualizado correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al actualizar el resultado"}

@resultados.delete(
    "/resultados/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Elimina un resultado",
    description="Elimina un resultado",
    tags=["Resultados"]
)
async def delete_resultados(id: int):
    try:
        query = delete(resulModel).where(resulModel.c.id_Resultado == id)
        await database.execute(query)
        return {"message": "Resultado eliminado correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al eliminar el resultado"}