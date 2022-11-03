from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
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


@login.get(
    "/login/validate", 
    status_code=status.HTTP_202_ACCEPTED,
    summary="Get token for a user",
    description="Get a token for user",
    tags=["Login"]
    )
async def validate(credentials: HTTPBasicCredentials = Depends(segurityBasic)):
    try:
        user = auth.sign_in_with_email_and_password(credentials.username, credentials.password)
        return {"token": user['idToken']}
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

@login.get(
    "/login/validateToken",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Validate token",
    description="Validate token",
    tags=["Login"]
    )
async def validateToken(credentials: HTTPAuthorizationCredentials = Depends(segurityBearer)):
    try:
        user = auth.get_account_info(credentials.credentials)
        uid = user['users'][0]['localId']
        user_data = db.child("users").child(uid).get().val()
        return { "user": user_data}
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

@login.get(
  "/login/singup",
  status_code=status.HTTP_202_ACCEPTED,
  summary="Singup",
  description="Singup",
  tags=["Login"]
  )
async def singup(matricula:str,rol:str,credentials: HTTPBasicCredentials = Depends(segurityBasic)):
  try:
    user = auth.create_user_with_email_and_password(credentials.username, credentials.password)
    data = {"matricula":matricula,"rol":rol}
    db.child("users").child(user['localId']).set(data)
    return {"token": user['idToken']}
  except:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid username or password",
      headers={"WWW-Authenticate": "Basic"},
    )