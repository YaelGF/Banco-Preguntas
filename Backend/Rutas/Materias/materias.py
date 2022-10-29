


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