from fastapi import APIRouter
from fastapi import Depends, FastAPI, HTTPException, status,  Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import pyrebase

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

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
db = firebase.database()

login = APIRouter()

segurityBasic = HTTPBasic()
segurityBearer = HTTPBearer()


@login.route(
    "/login/validate", 
    methods=['GET'],
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

"""

@login.get(
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

@login.get(
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

@login.get(
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
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e)"""