from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import get_db
from models.oficiales_model import Oficial
from sqlalchemy import text

router = APIRouter()

@router.get("/oficiales", response_model=list[Oficial])
async def get_oficiales(db: AsyncSession = Depends(get_db)):
    """Obtiene todos los oficiales de la tabla MAE_OFICIAL."""
    try:
        query = text("SELECT * FROM USR_P360.MAE_OFICIAL")
        result = await db.execute(query)
        oficiales = result.fetchall()
        return [Oficial(**dict(oficial)) for oficial in oficiales]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener oficiales: {e}")
