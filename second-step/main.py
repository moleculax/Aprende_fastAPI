from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from app.core.database import ConectaSQLLITE, ConectaPOSTGRES, ConectaMYSQL

app = FastAPI(
    title="Test SQLite",
    description="Test de conexión a SQLite",
    version="1.0.0"
)

# Para servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")
# =========================================================================
# Configurar templates para html
templates = Jinja2Templates(directory="templates")
# =========================================================================

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return FileResponse("templates/home/index.html")

@app.get("/conn")
def conexion_sqlite():
    conn = ConectaSQLLITE.create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT sqlite_version();")
        version = cursor.fetchone()
        conn.close()
        return {
            "status": "success",
            "message": "Conexión exitosa a SQLite",
            "version_sqlite": version[0],
            "database": ConectaSQLLITE.DATABASE_URL
        }
    else:
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": "Error al conectar con la base de datos"
            }
        )