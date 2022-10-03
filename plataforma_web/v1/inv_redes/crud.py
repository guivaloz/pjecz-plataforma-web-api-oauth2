"""
Inventarios Redes v1, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import PWIsDeletedError, PWNotExistsError

from .models import InvRed


def get_inv_redes(
    db: Session,
    estatus: str = None,
) -> Any:
    """Consultar las redes activas"""
    consulta = db.query(InvRed)
    if estatus is None:
        consulta = consulta.filter_by(estatus="A")  # Si no se da el estatus, solo activos
    else:
        consulta = consulta.filter_by(estatus=estatus)
    return consulta.order_by(InvRed.id)


def get_inv_red(
    db: Session,
    inv_red_id: int,
) -> InvRed:
    """Consultar una red por su id"""
    inv_red = db.query(InvRed).get(inv_red_id)
    if inv_red is None:
        raise PWNotExistsError("No existe ese red")
    if inv_red.estatus != "A":
        raise PWIsDeletedError("No es activo ese red, está eliminado")
    return inv_red
