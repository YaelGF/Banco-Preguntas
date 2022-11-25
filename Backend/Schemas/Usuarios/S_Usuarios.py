from typing import Optional
from pydantic import BaseModel

class Usuario(BaseModel):
    id_Usuario: int
    nombre: str
    uid: str
    apellidoPaterno: str
    apellidoMaterno: str
    email: str
    matricula: str
    id_TipoUsuario: int

class UsuarioNew(BaseModel):
    nombre: str
    apellidoPaterno: str
    apellidoMaterno: str
    email: str
    uid: str
    matricula: str
    id_TipoUsuario: int

class UsuarioUpdate(BaseModel):
    nombre: Optional[str]
    apellidoPaterno: Optional[str]
    apellidoMaterno: Optional[str]
    email: Optional[str]
    matricula: Optional[str]
    id_TipoUsuario: Optional[int]

class TipoUsuario(BaseModel):
    id_TipoUsuario: int
    tipoUsuario: str

class TipoUsuarioNew(BaseModel):
    tipoUsuario: str

class TipoUsuarioUpdate(BaseModel):
    tipoUsuario: Optional[str]

class Alumno(BaseModel):
    id_Alumno: int
    id_Usuario: int
    id_Grupo: int

class AlumnoNew(BaseModel):
    id_Usuario: int
    id_Grupo: int

class AlumnoUpdate(BaseModel):
    id_Usuario: Optional[int]
    id_Grupo: Optional[int]


class Login(BaseModel):
    email: str
    password: str
    rol: str

class UserLogin(BaseModel):
    uid: str