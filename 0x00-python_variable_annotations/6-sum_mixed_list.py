"""a type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_List(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of the list Union"""
    return sum(mxd_lst)