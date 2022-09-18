"""
Inventarios Modelos v1, esquemas de pydantic
"""
from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class InvModeloOut(BaseModel):
    """Esquema para entregar modelos"""

    id: int
    inv_marca_id: int
    inv_marca_nombre: str
    descripcion: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneInvModeloOut(InvModeloOut, OneBaseOut):
    """Esquema para entregar un modelo"""
