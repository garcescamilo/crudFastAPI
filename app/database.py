from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

# Usar aiosqlite para operaciones asíncronas
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./test.db"

Base = declarative_base()

# Crear motor asíncrono para SQLite
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

# Crear sesión asíncrona
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Función para obtener la sesión de la base de datos
async def get_db():
    async with async_session() as session:
        yield session
