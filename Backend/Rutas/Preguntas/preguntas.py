from Schemas.Preguntas import S_Preguntas
from fastapi import APIRouter, status
from Config.Conexion import database
from typing import List
from Modelos.BasedeDatos import preguntas_imagenes as preguntas_imagenesModel
from Modelos.BasedeDatos import respuestas as respuestasModel
from Modelos.BasedeDatos import preguntas as preguntasModel
from Modelos.BasedeDatos import imagenes as imagenesModel
from sqlalchemy import select, insert, update, delete

preguntas = APIRouter()

@preguntas.get(
    "/preguntas/", 
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una lista de preguntas",
    description ="Regresa una lista de preguntas",
    tags        =["Preguntas"]
)
async def get_preguntas():
    try:
        query = select(preguntasModel)
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
        query = select(preguntasModel).where(preguntasModel.c.id == id)
        return await database
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
            query = insert(preguntasModel).values(
                opcion1 = pregunta.opcion1,
                opcion2 = pregunta.opcion2,
                opcion3 = pregunta.opcion3,
                opcion4 = pregunta.opcion4,
                opcionCorrecta = pregunta.opcionCorrecta,
                id_Materia = pregunta.id_Materia,
            )
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
        query = update(preguntasModel).where(preguntasModel.c.id == id).values(
            opcion1 = pregunta.opcion1,
            opcion2 = pregunta.opcion2,
            opcion3 = pregunta.opcion3,
            opcion4 = pregunta.opcion4,
            opcionCorrecta = pregunta.opcionCorrecta,
            id_Materia = pregunta.id_Materia,
        )
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
        query = delete(preguntasModel).where(preguntasModel.c.id == id)
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
    tags=["Preguntas"]
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
    tags=["Preguntas"]
)
async def get_pregunta_imagen(id: int):
    try:
        query = select(preguntas_imagenesModel).where(preguntas_imagenesModel.c.id == id)
        return await database.fetch_one(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener la pregunta con su imagen"}

@preguntas.post(
    "/preguntas/imagenes/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Inserta una nueva pregunta con su imagen",
    description="Inserta una nueva pregunta con su imagen",
    tags=["Preguntas"]
)
async def post_preguntas_imagenes(pregunta: List[S_Preguntas.Pregunta_ImagenesNew]):
    try:
        for i in pregunta:
            query = insert(preguntas_imagenesModel).values(
                id_Pregunta = pregunta.id_Pregunta,
                id_Imagen = pregunta.id_Imagen,
            )
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
    tags=["Preguntas"]
)
async def put_pregunta_imagen(id: int, pregunta: S_Preguntas.Pregunta_ImagenesUpdate):
    try:
        query = update(preguntas_imagenesModel).where(preguntas_imagenesModel.c.id == id).values(
            id_Pregunta = pregunta.id_Pregunta,
            id_Imagen = pregunta.id_Imagen,
        )
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
    tags=["Preguntas"]
)
async def delete_pregunta_imagen(id: int):
    try:
        query = delete(preguntas_imagenesModel).where(preguntas_imagenesModel.c.id == id)
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
        query = select(respuestasModel).where(respuestasModel.c.id == id)
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
                respuesta = respuestaM.respuesta,
            )
            await database.execute(query)
        return {"message": "Respuesta insertada correctamente"}
        
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
        query = update(respuestasModel).where(respuestasModel.c.id == id).values(
            respuesta = respuestaM.respuesta,
        )
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
        query = delete(respuestasModel).where(respuestasModel.c.id == id)
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
        query = select(imagenesModel).where(imagenesModel.c.id == id)
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
            query = insert(imagenesModel).values(
                url = imagenM.url,
            )
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
        query = update(imagenesModel).where(imagenesModel.c.id == id).values(
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
        query = delete(imagenesModel).where(imagenesModel.c.id == id)
        await database.execute(query)
        return {"message": "Imagen eliminada correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al eliminar la imagen"}
