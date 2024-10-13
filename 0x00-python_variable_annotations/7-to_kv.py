#!/usr/bin/env python3
"""Write a type-annotated function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function to_kv that takes a string k and v as arguments"""

    return (k, v ** 2)
