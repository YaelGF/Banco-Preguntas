from typing import Optional
from pydantic import BaseModel

class Pregunta(BaseModel):
    id_Pregunta: int
    opcion1: int
    opcion2: int
    opcion3: int
    opcion4: int
    opcionCorrecta: int
    id_materia: int

class PreguntaNew(BaseModel):
    opcion1: int
    opcion2: int
    opcion3: int
    opcion4: int
    opcionCorrecta: int
    id_materia: int

class PreguntaUpdate(BaseModel):
    opcion1: Optional[int]
    opcion2: Optional[int]
    opcion3: Optional[int]
    opcion4: Optional[int]
    opcionCorrecta: Optional[int]
    id_materia: Optional[int]

class Respuesta(BaseModel):
    id_Respuesta: int
    respuesta: str

class RespuestaNew(BaseModel):
    respuesta: str

class RespuestaUpdate(BaseModel):
    respuesta: Optional[str]

class Pregunta_Imagenes(BaseModel):
    id_Pregunta_Imagen: int
    id_Pregunta: int
    id_Imagen: int

class Pregunta_ImagenesNew(BaseModel):
    id_Pregunta: int
    id_Imagen: int

class Pregunta_ImagenesUpdate(BaseModel):
    id_Pregunta: Optional[int]
    id_Imagen: Optional[int]

class Imagen(BaseModel):
    id_Imagen: int
    url: str

class ImagenNew(BaseModel):
    url: str

class ImagenUpdate(BaseModel):
    url: Optional[str]
    
