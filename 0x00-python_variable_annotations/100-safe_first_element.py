#!/usr/bin/evn python3
""" iterable object any"""
from typing import Any, Union, Sequence

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns first element of list or None"""
    if lst:
        return[0]
    else:
        return None
