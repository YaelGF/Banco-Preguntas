from fastapi import APIRouter, status, Depends
from Config.Conexion import database
from typing import List
from Schemas.Examenes.S_Examenes import Respuesta as respuestaSchema
from Segurity.segurity import get_level
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from Modelos.BasedeDatos import resultados as resulModel
from Modelos.BasedeDatos import alumnos as alumnosModel
from Modelos.BasedeDatos import examenes as examenesModel
from Modelos.BasedeDatos import usuarios as usuariosModel
from Modelos.BasedeDatos import n_materias as n_materiasModel
from Modelos.BasedeDatos import materias as materiasModel
from Modelos.BasedeDatos import grupos as gruposModel
from Modelos.BasedeDatos import carreras as carrerasModel
from sqlalchemy import select, insert, update, delete
import datetime
import random

dashboard = APIRouter()

securityBearer = HTTPBearer()

@dashboard.get(
    "/Dashboard/Alumno",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Obtiene los datos para el dashboard",
    description ="Obtiene los datos para el dashboard",
    tags=["Dashboard"]
)
async def get_dashboard(credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):

    try:
        user = get_level(credentials.credentials)
        uid = user['uid']
        query = select([usuariosModel.c.id_Usuario]).where(usuariosModel.c.uid == uid)
        idUsuario = await database.fetch_one(query)
        query = select([alumnosModel]).where(alumnosModel.c.id_Usuario == idUsuario["id_Usuario"])
        alumno = await database.fetch_one(query)
        query = select([resulModel,examenesModel,n_materiasModel]).where(resulModel.c.id_Examen == examenesModel.c.id_Examen).where(examenesModel.c.id_Materia == materiasModel.c.id_Materia).where(materiasModel.c.id_N_Materia == n_materiasModel.c.id_N_Materia).where(resulModel.c.id_Alumno == alumno["id_Alumno"])
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
                    "Calificacion": i["calificacion"],
                    "Fecha": i["fecha"],
                    "Materia": i["materia"],
                    "Profesor": profesor["nombre"]
                    }
                newResultados.append(data)
        return newResultados
    except Exception as e:
        return {"Error": str(e)}

@dashboard.get(
    "/Dashboard/Profesor",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Obtiene los datos para el dashboard",
    description ="Obtiene los datos para el dashboard",
    tags=["Dashboard"]
)
async def get_dashboard(credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    try:
        user = get_level(credentials.credentials)
        uid = user['uid']
        query = select([usuariosModel.c.id_Usuario]).where(usuariosModel.c.uid == uid)
        idUsuario = await database.fetch_one(query)
        query = select([materiasModel.c.id_Materia,n_materiasModel.c.materia,gruposModel.c.grupo]).where(materiasModel.c.id_N_Materia == n_materiasModel.c.id_N_Materia).where(materiasModel.c.id_Grupo == gruposModel.c.id_Grupo).where(materiasModel.c.profesor == idUsuario["id_Usuario"])
        return await database.fetch_all(query)
    except Exception as e:  
        return {"Error": str(e)}
    
@dashboard.get(
    "/Dashboard/Administrador",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Obtiene los datos para el dashboard",
    description ="Obtiene los datos para el dashboard",
    tags=["Dashboard"]
)
async def get_dashboard():
    try:
        query = select(usuariosModel).where(usuariosModel.c.id_TipoUsuario == 2)
        profesores = await database.fetch_all(query)
        data = []
        for i in profesores:
            value={
                "id_Usuario": i["id_Usuario"],
                "Nombre": i["nombre"],
                "Matricula": i["matricula"]
            }
            data.append(value)
        return data
    except Exception as e:
        return {"Error": str(e)}
