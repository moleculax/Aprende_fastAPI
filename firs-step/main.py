
from fastapi import FastAPI, Query, Body
from fastapi.responses import JSONResponse
from typing import Optional

from pydantic import BaseModel

from data.datablog import BlogData
from modelos.ApiResponse import ApiResponse
from modelos.postBlog import PostBase, UpdatePost

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
# =============================================

@app.get("/")
def home():
    contenido = {
        "message": "Bienvenido esta es una prueba en fastAPI ...",
        "version": "1.0.0",
        "endpoints": ["/", "/posts", "/posts/{id}"]
    }

    return contenido



# ======================================================
# Path parameters
@app.get("/posts/{post_id}")
def get_post_by_id(post_id: int):
    """Obtener un post por su ID"""
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

    return JSONResponse(
        status = False,
        status_code=404,
        content={"error": f"Post con ID {post_id} no encontrado"}
    )
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
                    "Content": post.Content
                    }
        # Agrego a la lista
        BLOG_POST.append(new_post)

        # Retornar respuesta
        return {
            "status": True,
            "message": "Post creado exitosamente",
            "data": new_post
        }
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )


@app.put("/posts/{post_id}")
def update_post(post_id: int, data: ActualizaPost):
    """Actualizar completamente un post existente"""

    for post in BLOG_POST:
        if post["id"] == post_id:
            if  not  data.Content not in data:
                return JSONResponse(
                    status_code=400,
                    content={"error": "Title y Content son requeridos"}
                )

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
            # Esto agrega nueva clave valor temporal solo prueba
            # post["autor"] = "Autor Desconocido"

            return {
                "status": True,
                "message": "Post Actualizado Completamente",
                "data": post
            }

    return JSONResponse(
        status_code=404,
        content={"error": f"Post con ID {post_id} no encontrado"}
    )


@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    for index, post in enumerate(BLOG_POST):
        if post["id"] == post_id:
            post_eliminado = BLOG_POST.pop(index)  #  Elimino por índice
            return {
                "status": True,
                "message": "Post eliminado exitosamente",
                "data": post_eliminado
            }

    return JSONResponse(
        status_code=404,
        content={"error": f"Post con ID {post_id} no encontrado"}
    )


# =========================================================================
# curl -X POST http://localhost:8000/posts \
#   -H "Content-Type: application/json" \
#   -d '{"title": "Nuevo Post", "Content": "Contenido del nuevo post"}'