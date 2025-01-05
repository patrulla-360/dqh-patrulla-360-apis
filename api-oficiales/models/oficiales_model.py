from pydantic import BaseModel, ConfigDict
from typing import Optional

class Oficial(BaseModel):
    oficial_id: int
    usuario_id: Optional[int]
    nombre: str
    apellido: str
    rango: Optional[str]
    dni: Optional[str]
    estado: Optional[str]
    sexo: Optional[str]

    model_config = ConfigDict(from_attributes=True)
