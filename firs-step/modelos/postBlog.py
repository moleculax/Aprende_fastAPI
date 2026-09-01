
from pydantic import BaseModel, Field, field_validator
from typing import Optional

"""
    Pydantic es la biblioteca de validación de datos. 
    Su función principal es garantizar que los datos 
    cumplan estrictamente con una estructura definida 
    en tiempo de ejecución.
"""

# Modelo Pydantic para crear posts
class PostBase(BaseModel):
    title: str = Field(..., min_length=10, max_length=100,
                       description="El título del post debe tener entre 3 y 100 caracteres",
                       examples= ["El titulo tiene que tener minimo 10 caracteres"]
                       )
    Content: Optional[str] = Field("Contenido por defecto", description="El contenido del post")  # para cuando no se envie contenido, le pongo un valor por defecto
    # Aqui agrego validacion personalizada para el titulo
    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        # Por ejemplo para evitar la palabra porn en el title
        for palabra in PALABRAS_NO_PERMITIDAS:
            if palabra in value.lower():
                raise ValueError(f"El titulo no puede contener la palabra {palabra}")
        return value

class UpdatePost(BaseModel):
    title: str
    Content: Optional[str] = None  # para cuando actualice solo el titulo y no el contenido, lo pongo como opcional


PALABRAS_NO_PERMITIDAS = ["porn","violencia", "droga", "racismo","spam","pornografia","sexo"]
