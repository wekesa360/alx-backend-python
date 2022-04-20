#!/usr/env python3
"""wait random module
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """wait random number
    
    Args:
        max_delay (int, optional): max_number. Defaults to 10.
    
    Returns:
        float: random float number 
    """
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
