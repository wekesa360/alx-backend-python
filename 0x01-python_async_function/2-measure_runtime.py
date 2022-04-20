#!/usr/bin/python3
"""measure time module
"""
import asyncio
import random
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int,  max_delay: int) -> float:
    """ Measures time of async functions

    Args:
        n (int): number of times 
        max_delay (int): max number of delays

    Returns:
        float: result
    """
    s = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = (perf_counter() - s) / n
    return total_time

print(asyncio.run(measure_time(2, 2)))
print(asyncio.run(measure_time(5, 2)))
print(asyncio.run(measure_time(15, 2)))