
from fastapi import FastAPI, Query, Body
from fastapi.responses import JSONResponse
from typing import Optional

from pydantic import BaseModel

app = FastAPI(
    title="First Step Mini Blog",
    description="API simple para un mini blog",
    version="1.0.0"
)

# Modelo Pydantic para crear posts
class PostCreate(BaseModel):
    title: str
    Content: str

BLOG_POST = [
            {"id": 1,
             "title": "Desde FastAPI",
             "Content": "Contenido 01"
             },
            {"id": 2,
             "title": "Titulo Python",
             "Content": "Contenido 02"
             },
            {"id": 3,
             "title": "Titulo Django",
             "Content": "Contenido 03"
             }
        ]

@app.get("/")
def home():
    contenido = {
        "message": "Bienvenido esta es una prueba en fastAPI ...",
        "version": "1.0.0",
        "endpoints": ["/", "/posts", "/posts/{id}"]
    }

    return contenido

# @app.get("/posts")
# def post():
#     response = {
#         "data": BLOG_POST
#     }
#     return response

# ======================================================
# Path parameters
@app.get("/posts/{post_id}")
def get_post_by_id(post_id: int):
    """Obtener un post por su ID"""
    for post in BLOG_POST:
        if post["id"] == post_id:
            return {"data": post}

    return JSONResponse(
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
                example="FastAPI"
            ),
            limit: Optional[int] = Query(
                10,
                description="Limite de resultados",
                ge=1,
                le=100
            )
        ):
    if query:
        # Buscar posts que coincidan con la query
        result = [
            post for post in BLOG_POST
            if query.lower() in post["title"].lower()
               or query.lower() in post["Content"].lower()
        ]

        # Aplicar límite
        result = result[:limit]

        return {
            "data": result,
            "query": query,
            "total": len(result),
            "limit": limit
        }

        # Si no hay query, devolver todos con límite
    return {
        "data": BLOG_POST[:limit],
        "query": None,
        "total": len(BLOG_POST[:limit]),
        "limit": limit
    }
# ======================================================

# Implemto metodo post
@app.post("/posts")
# Body(...) indica que es obligatorio enviar contenido
# Los tres puntos se llaman elipsi
# Body(None) no es obligatorio
def create_post(post: PostCreate = Body(...)):
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
        # Agregar a la lista
        BLOG_POST.append(new_post)

        # Retornar respuesta
        return {
            "message": "Post creado exitosamente",
            "data": new_post
        }
    except Exception as e:
        return e


@app.put("/posts/{post_id}")
def update_post(post_id: int, data: dict = Body(...)):
    """Actualizar completamente un post existente"""

    for post in BLOG_POST:
        if post["id"] == post_id:  # ✅ Cambiar post.id → post["id"]
            if "title" not in data or "Content" not in data:
                return JSONResponse(
                    status_code=400,
                    content={"error": "Title y Content son requeridos"}
                )

            if not data["title"].strip():
                return JSONResponse(
                    status_code=400,
                    content={"error": "Title no puede estar vacio"}
                )
            if not data["Content"].strip():
                return JSONResponse(
                    status_code=400,
                    content={"error": "Content no puede estar vacio"}
                )

            post["title"] = data["title"]  #  Cambiar post.title → post["title"]
            post["Content"] = data["Content"]  #  Cambiar post.Content → post["Content"]

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