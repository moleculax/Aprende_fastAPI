from pydantic import BaseModel

# Modelo Pydantic para crear posts
class PostBase(BaseModel):
    title: str
    Content: str

