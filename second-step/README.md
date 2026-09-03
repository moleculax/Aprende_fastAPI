# First Step EN FastAPI Ejemplo para testear

Una API REST simple construida con FastAPI . Este proyecto demuestra operaciones CRUD básicas (Crear, Leer, Actualizar, Eliminar) con FastAPI.


| Tecnología | Badge |
|------------|-------|
| **FastAPI** | [![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/) |
| **Python** | [![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) |
| **Pydantic** | [![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/) |
| **Pandas** | [![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/) |
| **PostgreSQL** | [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/) |
| **SQLAlchemy** | [![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-FF7F50?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/) |
| **OpenAPI** | [![OpenAPI](https://img.shields.io/badge/OpenAPI-3.1.0-6BA539?style=for-the-badge&logo=openapiinitiative&logoColor=white)](https://www.openapis.org/) |
| **JSON Schema** | [![JSON Schema](https://img.shields.io/badge/JSON%20Schema-Draft%2007-6BA539?style=for-the-badge&logo=jsonschema&logoColor=white)](https://json-schema.org/) |
## Características

- **CRUD completo**: Crear, leer, actualizar y eliminar Datos
- **Búsqueda**: Filtrar resultados por parámetros de consulta
- **Documentación automática**: Swagger UI y ReDoc
- **Validación de datos**: Validación de campos requeridos y vacíos
- **Manejo de errores**: Respuestas HTTP con códigos de estado apropiados
- **Usa al inicio datos por defecto**: Cuando el DataFrame no tiene datos
- **Crea DataFrame usando Pandas**: Para Almacenar datos
- **Crea archivo CSV/JSON/HTML**: Cuando se tratan los datos  en el CRUD

## Requisitos Previos

- Python 3.7+
- pip (gestor de paquetes de Python)

## 🔧 Instalación

### 1. Clonar el repositorio


2. Crear y activar entorno virtual
```
# Crear entorno virtual
python -m venv venv

# Activar en Linux/Mac
source venv/bin/activate

# Activar en Windows
venv\Scripts\activate

# Instala fastapi
pip install "fastapi[standard]"
```

3. Instalar dependencias
````
pip install -r requirements.txt

Ejecutamos:
fastapi dev main.py

El servidor se iniciará en: 

http://localhost:8000
````
Documentación de la API

Una vez que el servidor esté en ejecución, puedes acceder a la documentación automática:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc




