from typing import Optional
from pydantic import BaseModel

class Materia(BaseModel):
    id_materia: int
    id_N_Materia: int
    profesor: int
    id_Grupo: int

class MateriaNew(BaseModel):
    id_N_Materia: int
    profesor: int
    id_Grupo: int

class MateriaUpdate(BaseModel):
    id_N_Materia: Optional[int]
    profesor: Optional[int]
    id_Grupo: Optional[int]

class N_Materia(BaseModel):
    id_N_Materia: int
    materia: str

class N_MateriaNew(BaseModel):
    materia: str

class N_MateriaUpdate(BaseModel):
    materia: Optional[str]


