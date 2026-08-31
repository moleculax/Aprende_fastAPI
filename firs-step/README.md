# First Step EN FastAPI

Una API REST simple construida con FastAPI . Este proyecto demuestra operaciones CRUD básicas (Crear, Leer, Actualizar, Eliminar) con FastAPI.

## Características

- **CRUD completo**: Crear, leer, actualizar y eliminar posts
- **Búsqueda**: Filtrar posts por título o contenido
- **Paginación**: Limitar resultados con parámetros de consulta
- **Documentación automática**: Swagger UI y ReDoc
- **Validación de datos**: Validación de campos requeridos y vacíos
- **Manejo de errores**: Respuestas HTTP con códigos de estado apropiados

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
El servidor se iniciará en 
http://localhost:8000
````
Documentación de la API

Una vez que el servidor esté en ejecución, puedes acceder a la documentación automática:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

## Estructura del Proyecto
```
first-step-mini-blog/
├── main.py                 # Código principal de la API
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Este archivo
└── venv/                  # Entorno virtual (no incluido)
```


