from typing import Optional
from pydantic import BaseModel

class Grupo(BaseModel):
    id_Grupo: int
    grupo: str
    semestre: str
    id_Carrera: int

class GrupoNew(BaseModel):
    grupo: str
    semestre: str
    id_Carrera: int

class GrupoUpdate(BaseModel):
    grupo: Optional[str]
    semestre: Optional[str]
    id_Carrera: Optional[int]

