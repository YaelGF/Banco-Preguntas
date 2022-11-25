from Schemas.Usuarios import S_Usuarios
from fastapi import APIRouter, status
from Config.Conexion import database
from typing import List
from Modelos.BasedeDatos import usuarios  as usuariosModel
from Modelos.BasedeDatos import alumnos as alumnosModel
from Modelos.BasedeDatos import tipoUsuarios as tipoUsuariosModel
from sqlalchemy import select, insert, update, delete

usuarios = APIRouter()

@usuarios.get(
    "/usuarios/",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una lista de usuarios",
    description ="Regresa una lista de usuarios",
    tags=["Usuarios"]
)
async def get_usuarios():
    try:
        query = select(usuariosModel)
        return await database.fetch_all(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener los usuarios"}

@usuarios.post(
    "/usuarios/Login/",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa un usuario",
    description ="Regresa un usuario",
    tags=["Usuarios"]
)
async def get_usuario(usuario: S_Usuarios.UserLogin): 
    try:
        query = select(usuariosModel).where(usuariosModel.c.uid == usuario.uid)
        result = await database.fetch_one(query)
        if result:
            return "Success"
        return "Fail"
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener el usuario"}

@usuarios.get(
    "/usuarios/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa un usuario",
    description ="Regresa un usuario",
    tags=["Usuarios"]
)
async def get_usuario(id: int):
    try:
        query = select(usuariosModel).where(usuariosModel.c.id_Usuario == id)
        return await database.fetch_one(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener el usuario"}

@usuarios.post(
    "/usuarios/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Inserta un nuevo usuario",
    description="Inserta un nuevo usuario",
    tags=["Usuarios"]
)
async def post_usuarios(usuario: List[S_Usuarios.UsuarioNew]):
    try:
        for i in usuario:
            usuarioNew = i.dict()
            query = insert(usuariosModel).values(usuarioNew)
            await database.execute(query)
        return {"message": "Usuario insertado correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al insertar el usuario"}

@usuarios.put(
    "/usuarios/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Actualiza un usuario",
    description="Actualiza un usuario",
    tags=["Usuarios"]
)
async def put_usuarios(id: int, usuario: S_Usuarios.UsuarioUpdate):
    try:
        usuarioUpdate = usuario.dict(exclude_unset=True)
        query = update(usuariosModel).where(usuariosModel.c.id_Usuario == id).values(usuarioUpdate)
        await database.execute(query)
        return {"message": "Usuario actualizado correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al actualizar el usuario"}

@usuarios.delete(
    "/usuarios/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Elimina un usuario",
    description="Elimina un usuario",
    tags=["Usuarios"]
)
async def delete_usuarios(id: int):
    try:
        query = delete(usuariosModel).where(usuariosModel.c.id_Usuario == id)
        await database.execute(query)
        return {"message": "Usuario eliminado correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al eliminar el usuario"}

@usuarios.get(
    "/usuarios/alumnos/",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una lista de alumnos",
    description ="Regresa una lista de alumnos",
    tags=["Alumnos"]
)
async def get_alumnos():
    try:
        query = select(alumnosModel)
        return await database.fetch_all(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener los alumnos"}

@usuarios.get(
    "/usuarios/alumnos/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa un alumno",
    description ="Regresa un alumno",
    tags=["Alumnos"]
)
async def get_alumno(id: int):
    try:
        query = select(alumnosModel).where(alumnosModel.c.id_Alumno == id)
        return await database.fetch_one(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener el alumno"}
    
@usuarios.post(
    "/usuarios/alumnos",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Inserta un nuevo alumno",
    description="Inserta un nuevo alumno",
    tags=["Alumnos"]
)
async def post_alumnos(alumno: List[S_Usuarios.AlumnoNew]):
    try:
        for i in alumno:
            alumnoNew = i.dict()
            query = insert(alumnosModel).values(alumnoNew)
            await database.execute(query)
        return {"message": "Alumno insertado correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al insertar el alumno"}

@usuarios.put(
    "/usuarios/alumnos/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Actualiza un alumno",
    description="Actualiza un alumno",
    tags=["Alumnos"]
)
async def put_alumnos(id: int, alumno: S_Usuarios.AlumnoUpdate):
    try:
        alumnoUpdate = alumno.dict(exclude_unset=True)
        query = update(alumnosModel).where(alumnosModel.c.id_Alumno == id).values(alumnoUpdate)
        await database.execute(query)
        return {"message": "Alumno actualizado correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al actualizar el alumno"}

@usuarios.delete(
    "/usuarios/alumnos/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Elimina un alumno",
    description="Elimina un alumno",
    tags=["Alumnos"]
)
async def delete_alumnos(id: int):
    try:
        query = delete(alumnosModel).where(alumnosModel.c.id_Alumno == id)
        await database.execute(query)
        return {"message": "Alumno eliminado correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al eliminar el alumno"}
        
@usuarios.get(
    "/usuarios/tipos/",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una lista de tipos de usuarios",
    description ="Regresa una lista de tipos de usuarios",
    tags=["Tipos de usuarios"]
)
async def get_tipos():
    try:
        query = select(tipoUsuariosModel)
        return await database.fetch_all(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener los tipos de usuarios"}

@usuarios.get(
    "/usuarios/tipos/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa un tipo de usuario",
    description ="Regresa un tipo de usuario",
    tags=["Tipos de usuarios"]
)
async def get_tipo(id: int):
    try:
        query = select(tipoUsuariosModel).where(tipoUsuariosModel.c.id_TipoUsuario == id)
        return await database.fetch_one(query)
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener el tipo de usuario"}

@usuarios.post(
    "/usuarios/tipos",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Inserta un nuevo tipo de usuario",
    description="Inserta un nuevo tipo de usuario",
    tags=["Tipos de usuarios"]
)
async def post_tipos(tipo: List[S_Usuarios.TipoUsuarioNew]):
    try:
        for i in tipo:
            tipoNew =i.dict()
            query = insert(tipoUsuariosModel).values(tipoNew)
            await database.execute(query)
        return {"message": "Tipo de usuario insertado correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al insertar el tipo de usuario"}

@usuarios.put(
    "/usuarios/tipos/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Actualiza un tipo de usuario",
    description="Actualiza un tipo de usuario",
    tags=["Tipos de usuarios"]
)
async def put_tipos(id: int, tipo: S_Usuarios.TipoUsuarioUpdate):
    try:
        tipoNew = tipo.dict(exclude_unset=True)
        query = update(tipoUsuariosModel).where(tipoUsuariosModel.c.id_TipoUsuario == id).values(tipoNew)
        await database.execute(query)
        return {"message": "Tipo de usuario actualizado correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al actualizar el tipo de usuario"}

@usuarios.delete(
    "/usuarios/tipos/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Elimina un tipo de usuario",
    description="Elimina un tipo de usuario",
    tags=["Tipos de usuarios"]
)
async def delete_tipos(id: int):
    try:
        query = delete(tipoUsuariosModel).where(tipoUsuariosModel.c.id_TipoUsuario == id)
        await database.execute(query)
        return {"message": "Tipo de usuario eliminado correctamente"}
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al eliminar el tipo de usuario"}

