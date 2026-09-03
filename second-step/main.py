from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse


from core.conexionDB import ConectaPostgres

from modelos.ApiRespuestas.ApiException import  ApiException
from repositories.ListAutoresRepositories import Autores
from repositories.BookRepositories import LibrosDeAutores

"""
https://www.linkedin.com/in/moleculax/
http://moleculaxapp.vercel.app
"""
"""
Este es un ejemplo basico sobre fastAPI
"""
app = FastAPI(
    title="second Step",
    description="API simple de fastAPI/POSTGRES",
    version="1.0.0"
)






@app.get("/")
def home():
    # Obtener versión
    versioPG = ConectaPostgres.VersionPostgres()

    contenido = {
        "message": "SE USA POSTGRES COMO BASE DE DATOS ...",
        "versionAPP": "1.0.0",
         "endpoints": ["/",  "/docs"],
        "POSTGRES_VERSION": versioPG,
    }
    return contenido



# ============== DESDE AQUI USO POSTGRES =========================
# ============== AUTORES =========================================
@app.get("/autores")
def getAutoresAll():
    try:

        autores_repo = Autores()
        autores = autores_repo.obtener_todos()
        return {
            "status": True,
            "data": [autor.__dict__ for autor in autores],
            "message": "Autores obtenidos exitosamente"
        }
    except Exception as e:
        return ApiException(
            status=False,
            message=str(e),
            status_code=500
        ).send()

@app.get("/autores/{id_autor}")
def getautorID(id_autor: int):
    try:
        autoresDatos = Autores()
        autor = autoresDatos.obtener_por_id(id_autor)
        if autor:
            return {
                "status": True,
                "data": autor,
                "message": "Autor obtenido exitosamente"
            }
    except Exception as e:
        return ApiException(
            status=False,
            message=str(e),
            status_code=500
        ).send()

# ============== LIBROS DE AUTORES ======================
# __dict__ es un atributo de Python que almacena todos los atributos de un objeto en forma de diccionario.
@app.get("/libros")
def getTodosLosLibros():
    try:
        libros_repo = LibrosDeAutores()
        librosDatos = libros_repo.obtener_todos()
        losLibros = []
        for libros in librosDatos:
            losDatos = libros.__dict__
            losLibros.append(losDatos)
        return {
            "status": True,
            "data": losLibros,
            "message": "Libros obtenidos exitosamente"
        }
    except Exception as e:
        return ApiException(
            status=False,
            message=str(e),
            status_code=500
        ).send()