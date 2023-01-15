from typing import Tuple

from flask import Request

from piip.command.exceptions import UnauthorizedException


def mentor_only(request: Request) -> Tuple[str, int]:
    user_type = request.headers.get("User-Type", None)
    user_id = request.headers.get("User-Id", None)
    if not user_id or not user_type or user_type == "user":
        raise UnauthorizedException
    return user_type, user_id


def super_only(request: Request) -> Tuple[str, int]:
    user_type = request.headers.get("User-Type", None)
    user_id = request.headers.get("User-Id", None)
    if not user_id or not user_type or user_type == "user" or user_type == "mentor":
        raise UnauthorizedException
    return user_type, user_id


def user_only(request: Request) -> Tuple[str, int]:
    user_type = request.headers.get("User-Type", None)
    user_id = request.headers.get("User-Id", None)
    if not user_id or not user_type or not user_type == "user":
        raise UnauthorizedException
    return user_type, user_id
