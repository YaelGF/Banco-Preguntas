from fastapi import Depends, FastAPI, HTTPException, status,  Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from Rutas.Materias.materias import materias
from Rutas.Preguntas.preguntas import preguntas
from Rutas.Login.login import login
from Schemas import Schemas
from typing import Union
from typing import List
import pyrebase

import hashlib
import os 


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
    redoc_url=None,
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