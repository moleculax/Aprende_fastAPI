# =========================================================================
# CLASE DE RESPUESTA (CONSTRUCTOR)
# =========================================================================

from fastapi.responses import JSONResponse
from typing import Any, Optional


# Class para respuestas
class ApiResponse:
    def __init__(self, status: bool, data: Any = None, message: str = "", status_code: int = 200):
        self.status = status
        self.data = data
        self.message = message
        self.status_code = status_code
        self.query: Optional[str] = None
        self.total: Optional[int] = None
        self.limit: Optional[int] = None

    def send(self):
        # Construir contenido base
        content = {
            "status": self.status,
            "data": self.data,
            "message": self.message
        }

        # Solo agregar si no son None
        if self.query is not None:
            content["query"] = self.query
        if self.total is not None:
            content["total"] = self.total
        if self.limit is not None:
            content["limit"] = self.limit

        return JSONResponse(
            status_code=self.status_code,
            content=content
        )