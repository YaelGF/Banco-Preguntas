from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from Rutas.Materias.materias import materias
from Rutas.Preguntas.preguntas import preguntas
from Rutas.Resultados.resultados import resultados
from Rutas.Usuarios.usuarios import usuarios
from Rutas.Examenes.examenes import examenes
from Rutas.Carreras.carreras import carreras
from Rutas.Login.login import login
from Rutas.Teams.teams import groups
from Rutas.ExamenesOnline.examenesonline import examenOnline
from Rutas.Dashboards.dashboards import dashboard

from sqlalchemy import select, insert, update, delete

origins = [
    "http://127.0.0.1:8000",
    "http://0.0.0.0:8080",
    "http://localhost:8080",
    "*"
]

app = FastAPI(
    title="Banco de Preguntas",
    description="API para el Banco de Preguntas",
    version="1.0.0",
    docs_url="/",
    openapi_tags=[
        {
            "name": "Login",
            "description": "Operaciones sobre el login dentro de la aplicación",
        },
        {
            "name": "Preguntas",
            "description": "Operaciones sobre las preguntas dentro de la aplicación",
        },
        {
            "name": "Materias",
            "description": "Operaciones sobre las materias dentro de la aplicación",
        },
        {
            "name": "Resultados",
            "description": "Operaciones sobre los resultados dentro de la aplicación",
        },
        {
            "name": "Usuarios",
            "description": "Operaciones sobre los usuarios dentro de la aplicación",
        },
        {
            "name": "Examenes",
            "description": "Operaciones sobre los examenes dentro de la aplicación",
        },
        {
            "name": "Carreras",
            "description": "Operaciones sobre las carreras dentro de la aplicación",
        },
        {
            "name": "Respuestas",
            "description": "Operaciones sobre las respuestas dentro de la aplicación",
        },
        {     
            "name": "Imagenes",
            "description": "Operaciones sobre las imagenes dentro de la aplicación",
        },
        {  
            "name": "Alumnos",
            "description": "Operaciones sobre los alumnos dentro de la aplicación",
        },
        {
            "name": "Grupos",
            "description": "Operaciones sobre los grupos dentro de la aplicación",
        },
        {
            "name": "Tipos de usuarios",
            "description": "Operaciones sobre los tipos de usuarios dentro de la aplicación",
        },
        {
            "name": "Configuracion Examen",
            "description": "Operaciones sobre la configuracion de examen dentro de la aplicación",
        },
        {
            "name": "Nombre Materias",
            "description": "Operaciones sobre los nombres de materias dentro de la aplicación",
        },
        {
            "name": "Preguntas Con Imagenes",
            "description": "Operaciones sobre las preguntas con imagenes dentro de la aplicación"
        }
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs")

app.include_router(login)
app.include_router(preguntas)
app.include_router(materias)
app.include_router(resultados)
app.include_router(usuarios)
app.include_router(groups)
app.include_router(examenes)
app.include_router(carreras)
app.include_router(examenOnline)
app.include_router(dashboard)
