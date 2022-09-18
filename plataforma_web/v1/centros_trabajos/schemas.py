"""
Centros de Trabajo v1, esquemas de pydantic
"""
from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class CentroTrabajoOut(BaseModel):
    """Esquema para entregar centro de trabajo"""

    id: int
    distrito_id: int
    distrito_nombre: str
    distrito_nombre_corto: str
    domicilio_id: int
    domicilio_completo: str
    clave: str
    nombre: str
    telefono: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneCentroTrabajoOut(CentroTrabajoOut, OneBaseOut):
    """Esquema para entregar un centro de trabajo"""
