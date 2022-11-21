from typing import Optional
from pydantic import BaseModel

class Carrera(BaseModel):
    id_Carrera: int
    carrera: str
    coordinador: int

class CarreraNew(BaseModel):
    carrera: str
    coordinador: int

class CarreraUpdate(BaseModel):
    carrera: Optional[str]
    coordinador: Optional[int]