from typing import Optional
from pydantic import BaseModel

class Pregunta(BaseModel):
    id_Pregunta: int
    pregunta: str
    opcion1: int
    opcion2: int
    opcion3: int
    opcion4: int
    opcionCorrecta: int
    id_Materia: int

class PreguntaNew(BaseModel):
    pregunta: str
    opcion1: int
    opcion2: int
    opcion3: int
    opcion4: int
    opcionCorrecta: int
    id_Materia: int

class PreguntaUpdate(BaseModel):
    pregunta: Optional[str]
    opcion1: Optional[str]
    opcion2: Optional[str]
    opcion3: Optional[str]
    opcion4: Optional[str]
    opcionCorrecta: Optional[str]
    id_Materia: Optional[int]

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

class PreguntaFront(BaseModel):
    pregunta: str
    opcion1: str
    opcion2: str
    opcion3: str
    opcion4: str
    opcionCorrecta: str
    id_Materia: int
    
