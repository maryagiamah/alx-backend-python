#!/usr/bin/env python3
"""Annotate the below functions parameters and return values"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate function"""
    return [(i, len(i)) for i in lst]
