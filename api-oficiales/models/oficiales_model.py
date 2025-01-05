from pydantic import BaseModel
from typing import Optional

class Oficial(BaseModel):
    ID_OFICIAL: int
    ID_USUARIO: Optional[int]
    NOMBRE: str
    APELLIDO: str
    RANGO: Optional[str]
    DNI: Optional[str]
    ESTADO: Optional[str]
    SEXO: Optional[str]

    class Config:
        orm_mode = True
