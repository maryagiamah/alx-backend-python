#!/usr/bin/env python3
"""Write a function sum_mixed_list which takes a list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function sum_list which takes a list input_list of floats"""

    sum = 0.0
    for fl_int in mxd_lst:
        sum += fl_int
    return sum
