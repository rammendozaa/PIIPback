from functools import wraps

from piip.command.exceptions import get_error_info


def error_handling(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs), 200
        except Exception as e:
            return get_error_info(e)

    return wrapper
