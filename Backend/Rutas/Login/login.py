from fastapi import APIRouter
from Config.ConexionFirebase import auth
from Config.ConexionFirebase import db
from typing import List
from Modelos.BasedeDatos import usuarios as usuariosModel
from Schemas.Usuarios import S_Usuarios
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


login = APIRouter()

segurityBasic = HTTPBasic()
segurityBearer = HTTPBearer()


@login.get(
    "/login/validate", 
    status_code=status.HTTP_202_ACCEPTED,
    summary="Obtener un token de acceso para el usuario mediante credenciales basicas", 
    description="Obtener un token de acceso para el ususario mediante credenciales basicas usando el correo y contraseña del usuario",
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
    summary="Validacion del token",
    description="Valida el token sigue siendo valido y que rol pose el usuario el cual se encuentra logueado",
    tags=["Login"]
    )
async def validateToken(credentials: HTTPAuthorizationCredentials = Depends(segurityBearer)):
    try:
        user = auth.get_account_info(credentials.credentials)
        uid = user['users'][0]['localId']
        user_data = db.child("users").child(uid).get().val()
        return { "user": user_data, "uid": uid }
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

@login.post(
  "/login/singup",
  status_code=status.HTTP_202_ACCEPTED,
  summary="Agrega un nuevo usuario",
  description="Agrega un usuario a l sistema paraa que pueda loguearse posteriormente",
  tags=["Login"]
  )
async def singup(newUser: List[S_Usuarios.Login]):
  try:
    for i in newUser:
      user = auth.create_user_with_email_and_password(i.email, i.password)
      data = {"rol":i.rol}
      db.child("users").child(user['localId']).set(data)
    return {"mensaje": "Usuarios agregado correctamente"}
  except:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid username or password",
      headers={"WWW-Authenticate": "Basic"},
    )