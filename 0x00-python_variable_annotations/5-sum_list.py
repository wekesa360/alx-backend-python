#!/usr/bin/env python3
"""a type-annotated function list 
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns sum of of the list items float"""
    return sum(input_list)