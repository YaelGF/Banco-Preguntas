from typing import Optional
from pydantic import BaseModel

class Mensaje(BaseModel):
    mensaje     : str

class Token(BaseModel):
    token       : str

class Pregunta(BaseModel):
    pregunta    : str
    opcion1     : str
    opcion2     : str
    opcion3     : str
    opcionc     : str
    materia     : int