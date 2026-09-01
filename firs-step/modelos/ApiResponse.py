# =========================================================================
# CLASE DE RESPUESTA (CONSTRUCTOR)
# =========================================================================

from fastapi.responses import JSONResponse

class ApiResponse:
    def __init__(self, status: bool, data: any = None, message: str = "", status_code: int = 200):
        self.status = status
        self.data = data
        self.message = message
        self.status_code = status_code
        self.query = None
        self.total = None
        self.limit = None

    def send(self):
        return JSONResponse(
            status_code=self.status_code,
            content={
                "status": self.status,
                "data": self.data,
                "message": self.message,
                "query": self.query,
                "total": self.total,
                "limit": self.limit
            }
        )