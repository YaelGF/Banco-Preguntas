from fastapi import APIRouter, status, Depends
from Config.Conexion import database
from typing import List
from Schemas.Examenes.S_Examenes import Respuesta as respuestaSchema
from Segurity.segurity import get_level
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from Modelos.BasedeDatos import usuarios  as usuariosModel
from Modelos.BasedeDatos import alumnos as alumnosModel
from Modelos.BasedeDatos import examenes as examenesModel
from Modelos.BasedeDatos import resultados as resultadosModel
from Modelos.BasedeDatos import configuraciones as configuracionesModel
from Modelos.BasedeDatos import preguntas as preguntasModel
from Modelos.BasedeDatos import respuestas as respuestasModel
from Modelos.BasedeDatos import materias as materiasModel
from Modelos.BasedeDatos import n_materias as n_materiasModel
from sqlalchemy import select, insert, update, delete, func
import datetime
import random

examenOnline = APIRouter()

securityBearer = HTTPBearer()

@examenOnline.get(
    "/ValidateExamen/",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Verifica si el examen esta activo",
    description ="Verifica si el examen esta activo",
    tags=["ExamenOnline"]
)
async def get_examenes(credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    try:
        user = get_level(credentials.credentials)
        uid = user['uid']
        query = select([usuariosModel.c.id_Usuario]).where(usuariosModel.c.uid == uid)
        idUsuario = await database.fetch_one(query)
        query = select([alumnosModel.c.id_Grupo,alumnosModel.c.id_Alumno]).where(alumnosModel.c.id_Usuario == idUsuario['id_Usuario'])
        idGrupo = await database.fetch_one(query)
        query = select([examenesModel]).where(examenesModel.c.id_Grupo == idGrupo['id_Grupo']).where(examenesModel.c.fecha == datetime.datetime.now().strftime("%x")).where(examenesModel.c.horaInicio <= datetime.datetime.now().strftime("%H %M")).where(examenesModel.c.horaFin >= datetime.datetime.now().strftime("%H %M"))
        examen = await database.fetch_all(query)
        print(examen)
        print(datetime.datetime.now().strftime("%x"))
        print("------------------")
        print(datetime.datetime.now().strftime("%H %M"))
        print("------------------")
        print(datetime.datetime.now().strftime("%X"))
        if len(examen) != 0:
            print(examen[0]["id_Examen"])
            for i in range(len(examen)):
                idExamen = examen[i]['id_Examen']
                idAlumno = idGrupo['id_Alumno']
                query = select([resultadosModel]).where(resultadosModel.c.id_Examen == idExamen).where(resultadosModel.c.id_Alumno == idAlumno)
                resultado = await database.fetch_one(query)
                print(resultado)
                if resultado == None:
                    return {"status": True}
        return {"status": False}

    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener los usuarios"}

@examenOnline.get(
    "/GenerarExamen/",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Genera el examen",
    description ="Genera el examen",
    tags=["ExamenOnline"]
)
async def get_examenes(credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    try:
        exameen = []
        dataa = []
        user = get_level(credentials.credentials)
        uid = user['uid']
        query = select([usuariosModel.c.id_Usuario]).where(usuariosModel.c.uid == uid)
        idUsuario = await database.fetch_one(query)
        query = select([alumnosModel.c.id_Grupo,alumnosModel.c.id_Alumno]).where(alumnosModel.c.id_Usuario == idUsuario['id_Usuario'])
        idGrupo = await database.fetch_one(query)
        print(idGrupo)
        query = select([examenesModel]).where(examenesModel.c.id_Grupo == idGrupo['id_Grupo']).where(examenesModel.c.fecha == datetime.datetime.now().strftime("%x")).where(examenesModel.c.horaInicio <= datetime.datetime.now().strftime("%H %M")).where(examenesModel.c.horaFin >= datetime.datetime.now().strftime("%H %M"))
        examen = await database.fetch_one(query)
        print(datetime.datetime.now().strftime("%H %M"))
        if examen != None:
            idExamen = examen['id_Examen']
            query = select([configuracionesModel]).where(configuracionesModel.c.id_Examen == idExamen)
            configuracion = await database.fetch_all(query)
            print("q")
            for i in range(len(configuracion)):
                idMateria = configuracion[i]['id_Materia']
                query = select([preguntasModel]).where(preguntasModel.c.id_Materia == idMateria).order_by(func.random()).limit(configuracion[i]['NoPreguntas'])
                preguntas = await database.fetch_all(query)
                exameen.append(preguntas)
            for i in range(len(exameen)):
                for j in range(len(exameen[i])):
                    idPregunta = preguntas[j]['id_Pregunta']
                    pregunta = preguntas[j]['pregunta']
                    opcion1 = preguntas[j]['opcion1']
                    opcion2 = preguntas[j]['opcion2']
                    opcion3 = preguntas[j]['opcion3']
                    opcion4 = preguntas[j]['opcion4']
                    materia = preguntas[j]['id_Materia']
                    lista = [opcion1,opcion2,opcion3,opcion4]
                    n1 = random.randint(0,len(lista)-1)
                    opcion1 = lista[n1]
                    lista.pop(n1)
                    n1 = random.randint(0,len(lista)-1)
                    opcion2 = lista[n1]
                    lista.pop(n1)
                    n1 = random.randint(0,len(lista)-1)
                    opcion3 = lista[n1]
                    lista.pop(n1)
                    n1 = random.randint(0,len(lista)-1)
                    opcion4 = lista[n1]
                    lista.pop(n1)
                    opcion1 = select([respuestasModel.c.respuesta]).where(respuestasModel.c.id_Respuesta == opcion1)
                    opcion1 = await database.fetch_one(opcion1)
                    opcion2 = select([respuestasModel.c.respuesta]).where(respuestasModel.c.id_Respuesta == opcion2)
                    opcion2 = await database.fetch_one(opcion2)
                    opcion3 = select([respuestasModel.c.respuesta]).where(respuestasModel.c.id_Respuesta == opcion3)
                    opcion3 = await database.fetch_one(opcion3)
                    opcion4 = select([respuestasModel.c.respuesta]).where(respuestasModel.c.id_Respuesta == opcion4)
                    opcion4 = await database.fetch_one(opcion4)

                    materia = select([materiasModel.c.id_N_Materia]).where(materiasModel.c.id_Materia == materia)
                    materia = await database.fetch_one(materia)

                    materia = select([n_materiasModel.c.materia]).where(n_materiasModel.c.id_N_Materia == materia['id_N_Materia'])
                    materia = await database.fetch_one(materia)

                    data = {
                        "id_Pregunta": idPregunta,
                        "id_Examen": idExamen,
                        "pregunta": pregunta,
                        "opcion1": opcion1["respuesta"],
                        "opcion2": opcion2["respuesta"],
                        "opcion3": opcion3["respuesta"],
                        "opcion4": opcion4["respuesta"],
                        "materia": materia["materia"],
                    }
                    dataa.append(data)
            return dataa
        return {"message": "No hay examen"}

    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener los usuarios"}

@examenOnline.post(
    "/CalificarExamen/",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Califica el examen",
    description ="Califica el examen",
    tags=["ExamenOnline"]
)
async def calificar_examen(resultados: List[respuestaSchema],credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    try:
        user = get_level(credentials.credentials)
        uid = user['uid']
        query = select([usuariosModel.c.id_Usuario]).where(usuariosModel.c.uid == uid)
        idUsuario = await database.fetch_one(query)
        query = select([alumnosModel]).where(alumnosModel.c.id_Usuario == idUsuario['id_Usuario'])
        idUsuario = await database.fetch_one(query)
        idUsuario= idUsuario['id_Alumno']
        id_Examen = resultados[0].id_Examen
        count = 0
        for i in range(len(resultados)):
            r = dict(resultados[i])
            idPregunta = r['id_Pregunta']
            respuesta = r['respuesta']
            query = select([preguntasModel.c.opcionCorrecta]).where(preguntasModel.c.id_Pregunta == idPregunta)
            opcionCorrecta = await database.fetch_one(query)
            query = select([respuestasModel.c.respuesta]).where(respuestasModel.c.id_Respuesta == opcionCorrecta['opcionCorrecta'])
            opcionCorrecta = await database.fetch_one(query)
            if opcionCorrecta['respuesta'] == respuesta:
                count += 1
        calificacion = count/len(resultados)*(10)
        print(idUsuario)
        print(id_Examen)
        query = insert(resultadosModel).values(id_Examen=id_Examen,id_Alumno=idUsuario,calificacion=calificacion)
        await database.execute(query)
        return {"message": f"Tu calificacion es de {calificacion}"}

    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener los usuarios"}