
from fastapi.responses import JSONResponse

# Class para las exepciones
class ApiException:
    def __init__(self, status: bool, message: str = "", status_code: int = 400):
        self.status = status
        self.message = message
        self.status_code = status_code
    def send(self):
        return JSONResponse(
            status_code=self.status_code,
            content={
                "status": self.status,
                "message": self.message,
                "status_code": self.status_code
            }
        )