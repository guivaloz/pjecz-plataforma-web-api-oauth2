"""
Edictos v1, CRUD (create, read, update, and delete)
"""
from datetime import date, datetime
from typing import Any

from sqlalchemy.orm import Session

from config.settings import SERVIDOR_HUSO_HORARIO
from lib.exceptions import IsDeletedException, NotExistsException

from .models import Edicto
from ..autoridades.crud import get_autoridad


def get_edictos(
    db: Session,
    autoridad_id: int = None,
    creado: date = None,
    creado_desde: date = None,
    creado_hasta: date = None,
    fecha: date = None,
    fecha_desde: date = None,
    fecha_hasta: date = None,
) -> Any:
    """Consultar los edictos activos"""
    consulta = db.query(Edicto)
    if autoridad_id:
        autoridad = get_autoridad(db, autoridad_id)
        consulta = consulta.filter(Edicto.autoridad == autoridad)
    if creado:
        desde_dt = datetime(year=creado.year, month=creado.month, day=creado.day, hour=0, minute=0, second=0).astimezone(SERVIDOR_HUSO_HORARIO)
        hasta_dt = datetime(year=creado.year, month=creado.month, day=creado.day, hour=23, minute=59, second=59).astimezone(SERVIDOR_HUSO_HORARIO)
        consulta = consulta.filter(Edicto.creado >= desde_dt).filter(Edicto.creado <= hasta_dt)
    else:
        if creado_desde:
            desde_dt = datetime(year=creado.year, month=creado.month, day=creado.day, hour=0, minute=0, second=0).astimezone(SERVIDOR_HUSO_HORARIO)
            consulta = consulta.filter(Edicto.creado >= desde_dt)
        if creado_hasta:
            hasta_dt = datetime(year=creado.year, month=creado.month, day=creado.day, hour=23, minute=59, second=59).astimezone(SERVIDOR_HUSO_HORARIO)
            consulta = consulta.filter(Edicto.creado <= hasta_dt)
    if fecha:
        consulta = consulta.filter_by(fecha=fecha)
    else:
        if fecha_desde:
            consulta = consulta.filter(Edicto.fecha >= fecha_desde)
        if fecha_hasta:
            consulta = consulta.filter(Edicto.fecha <= fecha_hasta)
    return consulta.filter_by(estatus="A").order_by(Edicto.id)


def get_edicto(db: Session, edicto_id: int) -> Edicto:
    """Consultar un edicto por su id"""
    edicto = db.query(Edicto).get(edicto_id)
    if edicto is None:
        raise NotExistsException("No existe ese edicto")
    if edicto.estatus != "A":
        raise IsDeletedException("No es activo ese edicto, está eliminado")
    return edicto
