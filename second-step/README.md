```
second-step/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py      # Configuración de SQLAlchemy
│   │   └── security.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/               # Versión 1 de la API
│   │   │   ├── __init__.py
│   │   │   ├── router.py     # Registro de rutas v1
│   │   │   └── endpoints/
│   │   │       ├── __init__.py
│   │   │       ├── posts.py
│   │   │       └── users.py
│   │   └── v2/               # Versión 2 de la API
│   │       ├── __init__.py
│   │       └── router.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── post.py           # Modelo SQLAlchemy
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── post.py           # Esquemas Pydantic
│   ├── crud/
│   │   ├── __init__.py
│   │   └── post.py           # CRUD para posts
│   └── dependencies/
│       ├── __init__.py
│       └── auth.py
├── migrations/               # Migraciones de Alembic
│   ├── versions/
│   └── alembic.ini
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_api/
│       └── test_posts.py
├── .env
├── .gitignore
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
└── README.md
```