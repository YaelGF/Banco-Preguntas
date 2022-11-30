#import os
#Conexion = os.path.join("SQL/preguntas.sqlite") # Path to the database file

import databases
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "sqlite:///SQL/preguntas.sqlite"

#DATABASE_URL = "mysql+pymysql://doadmin:AVNS_f8yQweDA6eJAhuF0ywf@bancopreguntas-do-user-12761369-0.b.db.ondigitalocean.com:25060/BancoPreguntas"

database = databases.Database(DATABASE_URL)

engine =create_engine(DATABASE_URL)

meta = MetaData()
