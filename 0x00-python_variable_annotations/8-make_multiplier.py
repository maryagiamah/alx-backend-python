#!/usr/bin/env python3
"""Write a function make_multiplier that takes a float"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ function make_multiplier that takes a float multiplier"""
    def multiply(num):
        return multiplier * num
    return multiply
