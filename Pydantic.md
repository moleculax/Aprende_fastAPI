# Pydantic en FastAPI: Validación de Datos y POO

**Pydantic** es la librería de validación de datos y gestión de configuraciones más utilizada en el ecosistema de Python moderno. Es la columna vertebral de **FastAPI**, encargándose de transformar los datos que viajan en tus peticiones web en objetos estructurados y seguros.

---

## La relación entre Pydantic y la POO

Pydantic aprovecha los conceptos de la **Programación Orientada a Objetos (POO)** pero con un enfoque centrado en los datos:
* **Clase (Modelo):** Defines la estructura y las reglas que deben cumplir tus datos heredando de `BaseModel`.
* **Atributos:** Utilizas los *Type Hints* (tipados de Python) para definir qué tipo de dato debe almacenar cada propiedad.
* **Instancia (Objeto):** Cuando FastAPI recibe un JSON, Pydantic lo valida y lo transforma automáticamente en un objeto de Python sobre el que puedes operar.

---

##  Conceptos Básicos y Sintaxis

Para usar Pydantic, primero debes importar `BaseModel` y definir tu esquema de datos.

### 1. Definición de un Modelo Básico
```python
from pydantic import BaseModel, EmailStr, Field

class Usuario(BaseModel):
    id: int
    nombre: str
    email: str
    edad: int | None = None  # Atributo opcional con valor por defecto
```

### 2. Validaciones Avanzadas con `Field`
Pydantic permite añadir restricciones matemáticas, de longitud o expresiones regulares directamente en la declaración de los atributos:

```python
class Producto(BaseModel):
    nombre: str = Field(min_length=3, max_length=50)
    precio: float = Field(gt=0, description="El precio debe ser mayor a cero")
    stock: int = Field(default=0, ge=0)
```

---

##  Integración de Pydantic en FastAPI

La magia de Pydantic se potencia cuando lo conectas con los endpoints de FastAPI. El framework lee tus modelos para tres tareas cruciales:
1. **Validación Automática:** Si el cliente envía datos incorrectos (ej. un texto en lugar de un número), FastAPI responde inmediatamente con un error `422 Unprocessable Entity`.
2. **Serialización (JSON Parsing):** Convierte el JSON entrante a un objeto Python de forma transparente.
3. **Documentación:** Genera automáticamente los esquemas interactivos en la ruta `/docs` (Swagger UI).

### Ejemplo Completo de un Endpoint

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# 1. Definimos el modelo de datos (POO + Pydantic)
class Item(BaseModel):
    nombre: str
    precio: float = Field(gt=0)
    en_oferta: bool | None = None

# 2. Usamos el modelo como parámetro en la ruta
@app.post("/items/")
def crear_item(item: Item):
    # 'item' ya es un objeto validado. Podemos acceder a sus atributos con la notación de punto.
    precio_final = item.precio
    if item.en_oferta:
        precio_final = item.precio * 0.9
        
    return {
        "mensaje": f"Producto '{item.nombre}' procesado",
        "precio_calculado": precio_final
    }
```

---

##  Ventajas Principales

* **Tipado Seguro (Type Hinting):** Tu editor de código (como PyCharm) te ofrecerá autocompletado para todos los atributos del modelo.
* **Velocidad:** El núcleo de Pydantic (V2) está escrito en Rust, lo que lo hace extremadamente rápido en la validación de grandes volúmenes de datos.
* **Limpieza de Código:** Separa por completo la lógica de negocio de la lógica de validación de peticiones HTTP.
