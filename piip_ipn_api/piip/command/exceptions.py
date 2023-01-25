from typing import Dict, Tuple

from jwt.exceptions import ExpiredSignatureError


def get_error_structure(e: Exception, error_code: int) -> Tuple[Dict, int]:
    if hasattr(e, "default"):
        return {"error": e.default}, error_code
    return {"error": str(e)}, error_code


class UnauthorizedException(Exception):
    default = "Unauthorized to consume resource"


class InvalidCredentials(Exception):
    default = "Invalid email or password"


class UserNotFound(Exception):
    default = "This user does not exist"


def get_error_info(e: Exception) -> Tuple[Dict, int]:
    if isinstance(e, UnauthorizedException):
        return get_error_structure(e, 401)
    elif isinstance(e, InvalidCredentials):
        return get_error_structure(e, 401)
    elif isinstance(e, ExpiredSignatureError):
        return get_error_structure(e, 401)
    elif isinstance(e, UserNotFound):
        return get_error_structure(e, 401)
    else:
        return {"error": str(e)}, 500
