from aiohttp import ClientResponse

from .exceptions import QvaPayException


def validate_response(response: ClientResponse) -> None:
    if response.status != 200:
        raise QvaPayException(response.status)
