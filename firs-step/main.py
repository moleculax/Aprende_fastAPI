from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from typing import Optional

from pydantic import BaseModel

from core.conexionDB import ConectaPostgres
from data.datablog import BlogData, CreoDataFrame
from modelos.ApiRespuestas.ApiResponse import ApiResponse
from modelos.ApiRespuestas.ApiException import  ApiException
from modelos.ModelopostBlog import PostBase, UpdatePost, Etiquetas
from repositories.ListAutoresRepositories import Autores
"""
https://www.linkedin.com/in/moleculax/
http://moleculaxapp.vercel.app
"""
"""
Este es un ejemplo basico sobre fastAPI
"""
app = FastAPI(
    title="First Step",
    description="API simple de fastAPI",
    version="1.0.0"
)

# Crear instancia para trae los datos que se mostraran
losDatos = BlogData()
BLOG_POST = losDatos.objetoDatos()
# ========================================================



# Aqui heredo de PostBase que esta en modelos
class PostCreate(PostBase):
    pass

class ActualizaPost(UpdatePost):
    pass

# Heredo de PostBase los datos y solo agrego lo que me falta (id)
class PostPublic(PostBase):
    id: int

class PostSummary(BaseModel):
    id: int
    title: str

class Tab(Etiquetas):
    pass
# =============================================

@app.get("/")
def home():
    # Obtener versión
    versioPG = ConectaPostgres.VersionPostgres()

    contenido = {
        "message": "Bienvenido esta es una prueba en fastAPI SE USA POSTGRES COMO BASE DE DATOS ...",
        "versionAPP": "1.0.0",
         "endpoints": ["/", "/posts", "/posts/{id}", "/autores", "/docs"],
        "POSTGRES_VERSION": versioPG,
    }
    return contenido

# ======================================================
# Path parameters
@app.get("/posts/{post_id}")
def get_post_by_id(post_id: int):
    """Obtener un post por su ID"""
    try:
        for post in BLOG_POST:
            if post["id"] == post_id:
                # return {
                #     "status": True,
                #     "data": post
                # }
                return ApiResponse(
                    status=True,
                    data=post,
                    message="Post encontrado"
                ).send()

        return ApiResponse(
            status=False,
            message=f"Post con ID {post_id} no encontrado",
            status_code=404
        ).send()
    except Exception as e:
        return ApiException(
            status=False,
            message=str(e),
            status_code=500
        ).send()
# ======================================================

# AQUI USARE QUERY PARAM
@app.get("/posts")
def list_post(
        query: Optional[str] = Query(
            None,
            description="Texto del titulo a buscar",
            min_length=1,
            max_length=50,
            example=""
        ),
        limit: Optional[int] = Query(
            50,
            description="Limite de resultados",
            ge=1,
            le=100
        )
):
    try:
        if query:
            # Buscar posts que coincidan con la query (separado)
            result = []
            query_lower = query.lower()

            for post in BLOG_POST:
                if query_lower in post["title"].lower() or query_lower in post["Content"].lower():
                    result.append(post)

            # Aplicar límite
            result = result[:limit]

            return {
                "status": True,
                "data": result,
                "query": query,
                "total": len(result),
                "limit": limit
            }

        # Si no hay query, devolver todos con límite
        return {
            "status": True,
            "data": BLOG_POST,
            "query": None,
            "total": len(BLOG_POST[:limit]),
            "limit": limit
        }
    except Exception as e:
        return ApiException(
            status=False,
            message=str(e),
            status_code=500
        ).send()
# ======================================================

# Implento metodo post
@app.post("/posts")
# Body(...) indica que es obligatorio enviar contenido
# Los tres puntos se llaman elipsi
# Body(None) no es obligatorio
def create_post(post: PostCreate):

    try:
        # Verificar que title no esté vacío
        if not post.title.strip():
            return JSONResponse(
                status_code=400,
                content={"error": "Title no puede estar vacio"}
            )

        # Verificar que Content no esté vacío
        if not post.Content.strip():
            return JSONResponse(
                status_code=400,
                content={"error": "Content no puede estar vacio"}
            )

        # Generar nuevo ID porque no tengo base de datos
        new_id = (BLOG_POST[-1]["id"]+1) if BLOG_POST else 1
        new_post = {"id": new_id,
                    "title": post.title,
                    "Content": post.Content,
                    "Tags": post.Tags
                    }
        # Agrego a la lista
        BLOG_POST.append(new_post)
        # Aqui Instancio para almacenar datos en el DataFrame que crea el csv
        CreoDataFrame().agregarEnDataFrame(post.title, post.Content)

        # Retornar respuesta
        return {
            "status": True,
            "message": "Post creado exitosamente",
            "data": new_post
        }
    except Exception as e:
        return ApiException(
            status=False,
            message=str(e),
            status_code=500
        ).send()


@app.put("/posts/{post_id}")
def update_post(post_id: int, data: ActualizaPost):
    """Actualizar completamente un post existente"""
    try:
        for post in BLOG_POST:
            if post["id"] == post_id:
                if not data.title.strip():
                    return JSONResponse(
                        status_code=400,
                        content={"error": "Title no puede estar vacio"}
                    )
                if not data.Content.strip():
                    return JSONResponse(
                        status_code=400,
                        content={"error": "Content no puede estar vacio"}
                    )

                post["title"] = data.title
                post["Content"] = data.Content
                # Actualizo el DataFrame y el CSV
                CreoDataFrame().actualizarEnDataFrame(post_id, data.title, data.Content)
                # ======================================================================

                return {
                    "status": True,
                    "message": "Post Actualizado Completamente",
                    "data": post
                }

        return JSONResponse(
            status_code=404,
            content={"error": f"Post con ID {post_id} no encontrado"}
        )
    except Exception as e:
        return ApiException(
            status=False,
            message=str(e),
            status_code=500
        ).send()



@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    try:
        for index, post in enumerate(BLOG_POST):
            if post["id"] == post_id:
                post_eliminado = BLOG_POST.pop(index)  #  Elimino datos por el  índice
                return {
                    "status": True,
                    "message": "Post eliminado exitosamente",
                    "data": post_eliminado
                }
        # Aqui Instancio para eliminar dato del DataFrame que crea el csv
        CreoDataFrame().eliminarEnDataFrame(post_id)
        # ================================================================
        return JSONResponse(
            status_code=404,
            content={"error": f"Post con ID {post_id} no encontrado"}
        )
    except Exception as e:
        return ApiException(
            status=False,
            message=str(e),
            status_code=500
        ).send()

# ============== DESDE AQUI USO POSTGRES =========================
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