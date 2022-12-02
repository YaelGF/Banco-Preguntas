from Config.ConexionFirebase import db
from Config.ConexionFirebase import auth

def get_level(token: str):
    user = auth.get_account_info(token)
    uid = user['users'][0]['localId']
    user_data = db.child("users").child(uid).get().val()
    return { "user": user_data, "uid": uid }

