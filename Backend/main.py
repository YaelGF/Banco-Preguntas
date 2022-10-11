from fastapi import Depends, FastAPI, HTTPException, status,  Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from typing import Union
from typing import List
from .Schemas import Schemas
import pyrebase
import sqlite3
import hashlib
import os 

DATABASE_URL = os.path.join("Backend/SQL/preguntas.sqlite") # Path to the database file

firebaseConfig = {
  "apiKey": "AIzaSyBPmbcSj2xTLHDhrt4uTJiJOgIUyrjU0CM",
  "authDomain": "banco-de-preguntas-3f964.firebaseapp.com",
  "databaseURL": "https://banco-de-preguntas-3f964-default-rtdb.firebaseio.com",
  "projectId": "banco-de-preguntas-3f964",
  "storageBucket": "banco-de-preguntas-3f964.appspot.com",
  "messagingSenderId": "718216060964",
  "appId": "1:718216060964:web:10190eb3cb95eeaaa5f8b1",
  "measurementId": "G-BMJZZM42NF"
};

origins = [
    "http://127.0.0.1:8000",
    "http://0.0.0.0:8080",
    "http://localhost:8080",
    "*"
]

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
db = firebase.database()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


segurityBasic = HTTPBasic()
segurityBearer = HTTPBearer()

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

@app.get(
    "/login/validate", 
    status_code=status.HTTP_202_ACCEPTED,
    summary="Get token for a user",
    description="Get a token for user",
    tags=["login"]
    )
async def login(credentials: HTTPBasicCredentials = Depends(segurityBasic)):
    try:
      user = credentials.username
      password = credentials.password
      user = auth.sign_in_with_email_and_password(user, password)
      response = {
        "token": user['idToken'],
      }
      return response
    except Exception as e:
      print(f"Error: {e}")
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e)

@app.get(
    "/login/info",
    #response_model=Schemas.Usuario,
    status_code = status.HTTP_202_ACCEPTED,
    summary="Get user info",
    description="Get user info",
    tags=["login"],
)
async def get_user_info(credentials: HTTPAuthorizationCredentials = Depends(segurityBearer)):
    try:
      user = auth.get_account_info(credentials.credentials)
      uid = user['users'][0]['localId']
      users_data = db.child("users").child(uid).get().val()
      response = {
        "user": users_data,
      }
      return response
    except Exception as e:
      print(f"Error: {e}")
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e)

@app.get(
    "/login/logout",
    status_code = status.HTTP_202_ACCEPTED,
    summary="Logout user",
    description="Logout user",
    tags=["login"],
)
async def logout(credentials: HTTPAuthorizationCredentials = Depends(segurityBearer)):
    try:
      user = auth.get_account_info(credentials.credentials)
      uid = user['users'][0]['localId']
      auth.current_user = None
      response = {
        "user": uid,
      }
      return response
    except Exception as e:
      print(f"Error: {e}")
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e)

@app.get(
    "/login/register",
    status_code = status.HTTP_202_ACCEPTED,
    summary="Register user",
    description="Register user",
    tags=["login"],
)
async def register(matricula:str,rol:str,credentials: HTTPBasicCredentials = Depends(segurityBasic)):
    try:
      user = credentials.username
      password = credentials.password
      user = auth.create_user_with_email_and_password(user, password)
      uid = user['localId']
      response = {
        "Email": user["email"],
        "Rol": rol,
        "Mensaje": "Usuario registrado correctamente",
      }
      data= {
      "matricula": matricula,
      "rol": rol,
      }
      userData = db.child("users").child(uid).set(data)
      return response
    except Exception as e:
      print(f"Error: {e}")
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e)







#Obtiene las preguntas de la base de datos
@app.get(
    "/preguntas/", 
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una lista de preguntas",
    description ="Regresa una lista de preguntas",
    tags        =["Preguntas"]
)
#async def get_preguntas(credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
async def get_preguntas():
    try:
        with sqlite3.connect(DATABASE_URL) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM preguntas')
            response = cursor.fetchall()
            return response
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener las preguntas"}

#Obtiene una pregunta por medio del id
@app.get(
    "/preguntas/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una pregunta",
    description ="Regresa una pregunta",
    tags=["Preguntas"]
)
async def get_pregunta(id: int):
    try:
        with sqlite3.connect(DATABASE_URL) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM preguntas WHERE id_preg = ?', (id,))
            response = cursor.fetchone()
            return response
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener la pregunta"}


#Inserta una nueva pregunta a la base de datos
@app.post("/preguntas/", 
    status_code=status.HTTP_202_ACCEPTED,
    summary="Inserta una nueva pregunta",
    description="Inserta una nueva pregunta",
    tags=["Preguntas"]
)
async def post_preguntas(pregunta: Schemas.Pregunta):
    try:
        with sqlite3.connect(DATABASE_URL) as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO preguntas (pregunta, opcion1, opcion2, opcion3, opcionc, id_materia) VALUES (?, ?, ?, ?, ?, ?)', (pregunta.pregunta, pregunta.opcion1, pregunta.opcion2, pregunta.opcion3, pregunta.opcionc, pregunta.materia))
            connection.commit()
            response = cursor.fetchone()
            message = "Pregunta insertada correctamente"
            return {"message": message}
        
    except Exception as error:
        print(f"Error: {error}")
        return(f"Error: {error}")


#Obtiene las preguntas de la base de datos
@app.get(
    "/materias/",
    status_code=status.HTTP_202_ACCEPTED,
    summary     ="Regresa una lista de materias",
    description ="Regresa una lista de materias",
    tags=["Materias"]
)
async def get_materias():
    try:
        with sqlite3.connect(DATABASE_URL) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM materias')
            response = cursor.fetchall()
            return response
    except Exception as error:
        print(f"Error: {error}")
        return {"message": "Error al obtener las materias"}