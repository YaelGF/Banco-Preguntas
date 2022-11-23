#import os
#Conexion = os.path.join("SQL/preguntas.sqlite") # Path to the database file

import databases
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "sqlite:///SQL/preguntas.sqlite"

database = databases.Database(DATABASE_URL)

engine =create_engine(DATABASE_URL)

meta = MetaData()
