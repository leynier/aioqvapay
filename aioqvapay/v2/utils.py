from httpx import Response

from .exceptions import QvaPayException


def validate_response(response: Response) -> None:
    if response.status_code != 200:
        raise QvaPayException(response.status_code)
