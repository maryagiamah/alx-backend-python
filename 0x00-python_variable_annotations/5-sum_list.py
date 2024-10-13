#!/usr/bin/env python3
"""Write a type-annotated function sum_list which takes a list"""
from typing import List
float_list = List[float]


def sum_list(input_list: float_list) -> float:
    """function sum_list which takes a list input_list of floats"""

    sum = 0.0
    for flt in input_list:
        sum += flt
    return sum
