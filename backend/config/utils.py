import os
from typing import Any


def get_env_value(key: str, expected_type: Any = None, env: 'os._Environ[str]' = None):
    env = os.environ if env is None else env

    """get & cast a given value from os.environ, or return the default"""
    value = env[key]

    supported_types = (str, bool, int, float, list)
    assert expected_type in supported_types, (
        f'Tried to set unsupported environemnt variable {key} to {expected_type}')

    def raise_typerror():
        raise TypeError(f'Got bad environment variable {key}={value}'
                        f' (expected {expected_type})')

    if expected_type is str:
        return value
    elif expected_type is bool:
        if value.lower() == 'true':
            return True
        elif value.lower() == 'false':
            return False
        else:
            raise_typerror()
    elif expected_type is int:
        if value.isdigit():
            return int(value)
        else:
            raise_typerror()
    elif expected_type is float:
        try:
            return float(value)
        except ValueError:
            raise_typerror()
    elif expected_type is list:
        return value.split(',')
