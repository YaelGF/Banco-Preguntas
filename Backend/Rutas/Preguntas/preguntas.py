from Schemas.Preguntas import S_Preguntas
from fastapi import APIRouter, status, Depends
from Config.Conexion import database
from typing import List
from Modelos.BasedeDatos import preguntas_imagenes as preguntas_imagenesModel
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from Modelos.BasedeDatos import respuestas as respuestasModel
from Modelos.BasedeDatos import preguntas as preguntasModel
from Modelos.BasedeDatos import imagenes as imagenesModel
from Modelos.BasedeDatos import materias as materiasModel
from Modelos.BasedeDatos import n_materias as n_materiasModel
from Segurity.segurity import get_level
from Modelos.BasedeDatos import usuarios as usuariosModel
from sqlalchemy import select, insert, update, delete

preguntas = APIRouter()

securityBearer = HTTPBearer()

def concatenacion(pregunta, opcion1, opcion2, opcion3, opcion4):
    for i in range(len(pregunta)):
        pregunta[i]= dict(pregunta[i])
        opcion1[i]= list(opcion1[i])
        opcion2[i]= list(opcion2[i])
        opcion3[i]= list(opcion3[i])
        opcion4[i]= list(opcion4[i])
        pregunta[i]['opcion1'] = opcion1[i][0]
        pregunta[i]['opcion2'] = opcion2[i][0]
        pregunta[i]['opcion3'] = opcion3[i][0]
        pregunta[i]['opcion4'] = opcion4[i][0]
    return pregunta

def concatenar1(pregunta,opcion1,opcion2,opcion3,opcion4):
    opcion1 = list(opcion1)
    opcion2 = list(opcion2)
    opcion3 = list(opcion3)
    opcion4 = list(opcion4)
    pregunta['opcion1'] = opcion1[0]
    pregunta['opcion2'] = opcion2[0]
    pregunta['opcion3'] = opcion3[0]
    pregunta['opcion4'] = opcion4[0]
    return pregunta

@preguntas.get(
    "/preguntas/", 
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una lista de preguntas",
    description ="Regresa una lista de preguntas",
    tags        =["Preguntas"]
)
async def get_preguntas():
    try:
        query = select([preguntasModel.c.id_Pregunta,preguntasModel.c.pregunta,respuestasModel.c.respuesta,n_materiasModel.c.materia]).where(preguntasModel.c.id_Materia == materiasModel.c.id_Materia).where(materiasModel.c.id_N_Materia == n_materiasModel.c.id_N_Materia).where(preguntasModel.c.opcionCorrecta == respuestasModel.c.id_Respuesta)
        queryy = select([respuestasModel.c.respuesta]).where(preguntasModel.c.opcion1 == respuestasModel.c.id_Respuesta)
        opcion_1 = list(await database.fetch_all(queryy))
        queryy = select([respuestasModel.c.respuesta]).where(preguntasModel.c.opcion2 == respuestasModel.c.id_Respuesta)
        opcion_2 = list(await database.fetch_all(queryy))
        queryy = select([respuestasModel.c.respuesta]).where(preguntasModel.c.opcion3 == respuestasModel.c.id_Respuesta)
        opcion_3 = list(await database.fetch_all(queryy))
        queryy = select([respuestasModel.c.respuesta]).where(preguntasModel.c.opcion4 == respuestasModel.c.id_Respuesta)
        opcion_4 = list(await database.fetch_all(queryy))
        preguntas = list(await database.fetch_all(query))
        return concatenacion(preguntas, opcion_1, opcion_2, opcion_3, opcion_4)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener las preguntas"}

@preguntas.get(
    "/preguntas/respuestas/", 
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una lista de preguntas",
    description ="Regresa una lista de preguntas",
    tags        =["Preguntas"]
)
async def get_preguntas():
    try:
        query = select([preguntasModel.c.id_Pregunta,preguntasModel.c.pregunta,respuestasModel.c.respuesta,n_materiasModel.c.materia]).where(preguntasModel.c.id_Materia == materiasModel.c.id_Materia).where(materiasModel.c.id_N_Materia == n_materiasModel.c.id_N_Materia).where(preguntasModel.c.opcionCorrecta == respuestasModel.c.id_Respuesta)
        return await database.fetch_all(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener las preguntas"}

@preguntas.get(
    "/preguntas/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una pregunta",
    description ="Regresa una pregunta",
    tags=["Preguntas"]
)
async def get_pregunta(id: int):
    try:
        query = select([preguntasModel.c.id_Pregunta,preguntasModel.c.pregunta,respuestasModel.c.respuesta,n_materiasModel.c.materia]).where(preguntasModel.c.id_Materia == materiasModel.c.id_Materia).where(materiasModel.c.id_N_Materia == n_materiasModel.c.id_N_Materia).where(preguntasModel.c.opcionCorrecta == respuestasModel.c.id_Respuesta).where(preguntasModel.c.id_Pregunta == id)
        queryy = select([respuestasModel.c.respuesta]).where(preguntasModel.c.opcion1 == respuestasModel.c.id_Respuesta).where(preguntasModel.c.id_Pregunta == id)
        opcion_1 = list(await database.fetch_one(queryy))
        queryy = select([respuestasModel.c.respuesta]).where(preguntasModel.c.opcion2 == respuestasModel.c.id_Respuesta).where(preguntasModel.c.id_Pregunta == id)
        opcion_2 = list(await database.fetch_one(queryy))
        queryy = select([respuestasModel.c.respuesta]).where(preguntasModel.c.opcion3 == respuestasModel.c.id_Respuesta).where(preguntasModel.c.id_Pregunta == id)
        opcion_3 = list(await database.fetch_one(queryy))
        queryy = select([respuestasModel.c.respuesta]).where(preguntasModel.c.opcion4 == respuestasModel.c.id_Respuesta).where(preguntasModel.c.id_Pregunta == id)
        opcion_4 = list(await database.fetch_one(queryy))
        preguntas = dict(await database.fetch_one(query))
        print(preguntas)
        print(opcion_1)
        print(opcion_2)
        print(opcion_3)
        print(opcion_4)
        return concatenar1(preguntas, opcion_1, opcion_2, opcion_3, opcion_4)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener la pregunta"}

@preguntas.post(
    "/preguntas/", 
    status_code=status.HTTP_202_ACCEPTED,
    summary="Inserta una nueva pregunta",
    description="Inserta una nueva pregunta",
    tags=["Preguntas"]
)
async def post_preguntas(pregunta: List[S_Preguntas.PreguntaNew]):
    try:
        for i in pregunta:
            preguntaNew = i.dict()
            query = insert(preguntasModel).values(preguntaNew)
            await database.execute(query)
        return {"message": "Pregunta insertada correctamente"}
        
    except Exception as error:
        print(f"Error: {error}")
        return(f"Error: {error}")

@preguntas.put(
    "/preguntas/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Actualiza una pregunta",
    description="Actualiza una pregunta",
    tags=["Preguntas"]
)
async def put_pregunta(id: int, pregunta: S_Preguntas.PreguntaUpdate):
    try:
        pregunta = pregunta.dict(exclude_unset=True)
        query = update(preguntasModel).where(preguntasModel.c.id_Pregunta == id).values(pregunta)
        await database.execute(query)
        return {"message": "Pregunta actualizada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al actualizar la pregunta"}

@preguntas.delete(
    "/preguntas/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Elimina una pregunta",
    description="Elimina una pregunta",
    tags=["Preguntas"]
)
async def delete_pregunta(id: int):
    try:
        query = delete(preguntasModel).where(preguntasModel.c.id_Pregunta == id)
        await database.execute(query)
        return {"message": "Pregunta eliminada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al eliminar la pregunta"}

@preguntas.get(
    "/preguntas/imagenes/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Regresa una lista de preguntas con sus imagenes",
    description="Regresa una lista de preguntas con sus imagenes",
    tags=["Preguntas Con Imagenes"]
)
async def get_preguntas_imagenes():
    try:
        query = select(preguntas_imagenesModel)
        return await database.fetch_all(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener las preguntas con sus imagenes"}

@preguntas.get(
    "/preguntas/imagenes/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Regresa una pregunta con su imagen",
    description="Regresa una pregunta con su imagen",
    tags=["Preguntas Con Imagenes"]
)
async def get_pregunta_imagen(id: int):
    try:
        query = select(preguntas_imagenesModel).where(preguntas_imagenesModel.c.id_Pregunta_Imagen == id)
        return await database.fetch_one(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener la pregunta con su imagen"}

@preguntas.post(
    "/preguntas/imagenes/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Inserta una nueva pregunta con su imagen",
    description="Inserta una nueva pregunta con su imagen",
    tags=["Preguntas Con Imagenes"]
)
async def post_preguntas_imagenes(pregunta: List[S_Preguntas.Pregunta_ImagenesNew]):
    try:
        for i in pregunta:
            preguntaNew = i.dict()
            query = insert(preguntas_imagenesModel).values(preguntaNew)
            await database.execute(query)
        return {"message": "Pregunta insertada correctamente"}
        
    except Exception as error:
        print(f"Error: {error}")
        return(f"Error: {error}")

@preguntas.put(
    "/preguntas/imagenes/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Actualiza una pregunta con su imagen",
    description="Actualiza una pregunta con su imagen",
    tags=["Preguntas Con Imagenes"]
)
async def put_pregunta_imagen(id: int, pregunta: S_Preguntas.Pregunta_ImagenesUpdate):
    try:
        preguntaNew = pregunta.dict(exclude_unset=True)
        query = update(preguntas_imagenesModel).where(preguntas_imagenesModel.c.id_Pregunta_Imagen == id).values(preguntaNew)
        await database.execute(query)
        return {"message": "Pregunta actualizada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al actualizar la pregunta"}

@preguntas.delete(
    "/preguntas/imagenes/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Elimina una pregunta con su imagen",
    description="Elimina una pregunta con su imagen",
    tags=["Preguntas Con Imagenes"]
)
async def delete_pregunta_imagen(id: int):
    try:
        query = delete(preguntas_imagenesModel).where(preguntas_imagenesModel.c.id_Pregunta_Imagen == id)
        await database.execute(query)
        return {"message": "Pregunta eliminada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al eliminar la pregunta"}

@preguntas.get(
    "/respuestas/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Regresa una lista de respuestas",
    description="Regresa una lista de respuestas",
    tags=["Respuestas"]
)
async def get_respuestas():
    try:
        query = select(respuestasModel)
        return await database.fetch_all(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener las respuestas"}

@preguntas.get(
    "/respuestas/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Regresa una respuesta",
    description="Regresa una respuesta",
    tags=["Respuestas"]
)
async def get_respuesta(id: int):
    try:
        query = select(respuestasModel).where(respuestasModel.c.id_Respuesta == id)
        return await database.fetch_one(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener la respuesta"}

@preguntas.post(
    "/respuestas/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Inserta una nueva respuesta",
    description="Inserta una nueva respuesta",
    tags=["Respuestas"]
)
async def post_respuestas(respuestaM: List[S_Preguntas.RespuestaNew]):
    try:
        for i in respuestaM:
            query = insert(respuestasModel).values(
                respuesta = i.respuesta,
            )
            await database.execute(query)
        return {"message": "Respuestas insertada correctamente"}
        
    except Exception as error:
        print(f"Error: {error}")
        return(f"Error: {error}")

@preguntas.put(
    "/respuestas/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Actualiza una respuesta",
    description="Actualiza una respuesta",
    tags=["Respuestas"]
)
async def put_respuesta(id: int, respuestaM: S_Preguntas.RespuestaUpdate):
    try:
        query = update(respuestasModel).where(respuestasModel.c.id_Respuesta == id).values(respuestaM.dict(exclude_unset=True))
        await database.execute(query)
        return {"message": "Respuesta actualizada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al actualizar la respuesta"}

@preguntas.delete(
    "/respuestas/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Elimina una respuesta",
    description="Elimina una respuesta",
    tags=["Respuestas"]
)
async def delete_respuesta(id: int):
    try:
        query = delete(respuestasModel).where(respuestasModel.c.id_Respuesta == id)
        await database.execute(query)
        return {"message": "Respuesta eliminada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al eliminar la respuesta"}

@preguntas.get(
    "/imagenes/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Regresa una lista de imagenes",
    description="Regresa una lista de imagenes",
    tags=["Imagenes"]
)
async def get_imagenes():
    try:
        query = select(imagenesModel)
        return await database.fetch_all(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener las imagenes"}

@preguntas.get(
    "/imagenes/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Regresa una imagen",
    description="Regresa una imagen",
    tags=["Imagenes"]
)
async def get_imagen(id: int):
    try:
        query = select(imagenesModel).where(imagenesModel.c.id_Imagen == id)
        return await database.fetch_one(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener la imagen"}

@preguntas.post(
    "/imagenes/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Inserta una nueva imagen",
    description="Inserta una nueva imagen",
    tags=["Imagenes"]
)
async def post_imagenes(imagenM: List[S_Preguntas.ImagenNew]):
    try:
        for i in imagenM:
            newImage = i.dict()
            query = insert(imagenesModel).values(newImage)
            await database.execute(query)
        return {"message": "Imagen insertada correctamente"}
        
    except Exception as error:
        print(f"Error: {error}")
        return(f"Error: {error}")

@preguntas.put(
    "/imagenes/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Actualiza una imagen",
    description="Actualiza una imagen",
    tags=["Imagenes"]
)
async def put_imagen(id: int, imagenM: S_Preguntas.ImagenUpdate):
    try:
        query = update(imagenesModel).where(imagenesModel.c.id_Imagen == id).values(
            url = imagenM.url,
        )
        await database.execute(query)
        return {"message": "Imagen actualizada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al actualizar la imagen"}

@preguntas.delete(
    "/imagenes/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Elimina una imagen",
    description="Elimina una imagen",
    tags=["Imagenes"]
)
async def delete_imagen(id: int):
    try:
        query = delete(imagenesModel).where(imagenesModel.c.id_Imagen == id)
        await database.execute(query)
        return {"message": "Imagen eliminada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al eliminar la imagen"}

@preguntas.post(
    "/preguntas/Front/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Regresa una lista de preguntas",
    description="Regresa una lista de preguntas",
    tags=["Preguntas"]
)
async def add_preguntasFront(preguntaM: S_Preguntas.PreguntaFront,credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    try:
        opcion1 = {"respuesta": preguntaM.opcion1}
        opcion2 = {"respuesta": preguntaM.opcion2}
        opcion3 = {"respuesta": preguntaM.opcion3}
        opcion4 = {"respuesta": preguntaM.opcion4} 
        query  = insert(respuestasModel).values(opcion1)
        await database.execute(query)
        query  = insert(respuestasModel).values(opcion2)
        await database.execute(query)
        query  = insert(respuestasModel).values(opcion3)
        await database.execute(query)
        query  = insert(respuestasModel).values(opcion4)
        await database.execute(query)
        query = select(respuestasModel.c.id_Respuesta).where(respuestasModel.c.respuesta == preguntaM.opcion1)
        id1 = await database.fetch_one(query)
        query = select(respuestasModel.c.id_Respuesta).where(respuestasModel.c.respuesta == preguntaM.opcion2)
        id2 = await database.fetch_one(query)
        query = select(respuestasModel.c.id_Respuesta).where(respuestasModel.c.respuesta == preguntaM.opcion3)
        id3 = await database.fetch_one(query)
        query = select(respuestasModel.c.id_Respuesta).where(respuestasModel.c.respuesta == preguntaM.opcion4)
        id4 = await database.fetch_one(query)
        query = select(respuestasModel).where(respuestasModel.c.respuesta == preguntaM.opcionCorrecta)
        oC = await database.fetch_one(query)
        token = credentials.credentials
        user = get_level(token)
        uid = user['uid']
        query = select(usuariosModel.c.id_Usuario).where(usuariosModel.c.uid == uid)
        idUser = await database.fetch_one(query)
        query = select(n_materiasModel.c.id_N_Materia).where(n_materiasModel.c.materia == preguntaM.materia)
        idMateria = await database.fetch_one(query)
        query = select(materiasModel.c.id_Materia).where((materiasModel.c.id_N_Materia == idMateria["id_N_Materia"]) & (materiasModel.c.profesor == idUser["id_Usuario"]))
        idMateria = await database.fetch_one(query)
        print(oC)
        newPregunta = {
            "pregunta": preguntaM.pregunta,
            "opcion1": id1["id_Respuesta"],
            "opcion2": id2["id_Respuesta"],
            "opcion3": id3["id_Respuesta"],
            "opcion4": id4["id_Respuesta"],
            "opcionCorrecta": oC["id_Respuesta"],
            "id_Materia": idMateria["id_Materia"]
        }
        query = insert(preguntasModel).values(newPregunta)
        await database.execute(query)
        return {"message": "Pregunta insertada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener las preguntas"}