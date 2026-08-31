from pydantic import BaseModel

# Modelo Pydantic para crear posts
class PostBase(BaseModel):
    title: str
    Content: str

class UpdatePost(BaseModel):
    title: str
    Content: str

