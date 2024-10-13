#!/usr/bin/env python3
"""Given the parameters and the return values, add type annotations"""
from typing import Mapping, Any, TypeVar, Union
T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None]
) -> Union[Any, T]:
    """Annotate Function"""
    if key in dct:
        return dct[key]
    else:
        return default
