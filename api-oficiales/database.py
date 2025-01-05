from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import os

# URL de conexión a PostgreSQL
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:cente110@A@34.39.130.83:5432/postgres"
)

# Crear el motor de la base de datos
engine = create_async_engine(DATABASE_URL, echo=True)

# Crear la fábrica de sesiones
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependencia para obtener la sesión
async def get_db():
    async with async_session() as session:
        yield session