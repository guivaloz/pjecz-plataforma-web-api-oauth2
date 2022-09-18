"""
Inventarios Marcas v1, esquemas de pydantic
"""
from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class InvMarcaOut(BaseModel):
    """Esquema para entregar marcas"""

    id: int
    nombre: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneInvMarcaOut(InvMarcaOut, OneBaseOut):
    """Esquema para entregar una marca"""
