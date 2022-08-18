"""
Inv Modelos CRUD (create, read, update, and delete)
"""
from typing import Any

import requests

from config.settings import BASE_URL, LIMIT, TIMEOUT
import lib.exceptions


def get_inv_modelos(
    authorization_header: dict,
    limit: int = LIMIT,
    inv_marca_id: int = None,
) -> Any:
    """Solicitar modelos"""
    parametros = {"limit": limit}
    if inv_marca_id is not None:
        parametros["inv_marca_id"] = inv_marca_id
    try:
        response = requests.get(
            f"{BASE_URL}/inv_modelos",
            headers=authorization_header,
            params=parametros,
            timeout=TIMEOUT,
        )
        response.raise_for_status()
    except requests.exceptions.ConnectionError as error:
        raise lib.exceptions.CLIStatusCodeError("No hubo respuesta al solicitar modelos") from error
    except requests.exceptions.HTTPError as error:
        raise lib.exceptions.CLIStatusCodeError("Error Status Code al solicitar modelos: " + str(error)) from error
    except requests.exceptions.RequestException as error:
        raise lib.exceptions.CLIConnectionError("Error inesperado al solicitar modelos") from error
    data_json = response.json()
    if "items" not in data_json or "total" not in data_json:
        raise lib.exceptions.CLIResponseError("No se recibio items o total en la respuesta al solicitar modelos")
    return data_json
