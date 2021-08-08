"""
Distritos v1.0, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from .models import Distrito


def get_distritos(db: Session, solo_distritos: bool = False) -> Any:
    """Consultar los distritos judiciales activos"""
    consulta = db.query(Distrito).filter(Distrito.es_distrito_judicial == True)
    if solo_distritos:
        consulta = consulta.filter(Distrito.nombre.like("Distrito%"))
    return consulta.filter_by(estatus="A").order_by(Distrito.nombre)


def get_distrito(db: Session, distrito_id: int) -> Distrito:
    """Consultar un distrito por su id"""
    return db.query(Distrito).get(distrito_id)
