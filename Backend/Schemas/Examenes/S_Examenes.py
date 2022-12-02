from typing import Optional
from pydantic import BaseModel

class Examen(BaseModel):
    id_Examen: int
    profesor: int
    fecha: str
    horaInicio: str
    horaFin: str
    id_Materia: int
    id_Grupo: int

class ExamenNew(BaseModel):
    profesor: int
    fecha: str
    horaInicio: str
    horaFin: str
    id_Materia: int
    id_Grupo: int

class ExamenUpdate(BaseModel):
    profesor: Optional[int]
    fecha: Optional[str]
    horaInicio: Optional[str]
    horaFin: Optional[str]
    id_Materia: Optional[int]
    id_Grupo: Optional[int]

class Configuracion(BaseModel):
    id_Configuracion: int
    id_Examen: int
    id_Materia: int
    NoPreguntas: int

class ConfiguracionNew(BaseModel):
    id_Examen: int
    id_Materia: int
    NoPreguntas: int

class ConfiguracionUpdate(BaseModel):
    id_Examen: Optional[int]
    id_Materia: Optional[int]
    NoPreguntas: Optional[int]

class Resultado(BaseModel):
    id_Resultado: int
    id_Examen: int
    id_Alumno: int
    calificacion: float

class ResultadoNew(BaseModel):
    id_Examen: int
    id_Alumno: int
    calificacion: float

class ResultadoUpdate(BaseModel):
    id_Examen: Optional[int]
    id_Alumno: Optional[int]
    calificacion: Optional[float]

class Respuesta(BaseModel):
    id_Pregunta: int
    id_Examen: int
    respuesta: str