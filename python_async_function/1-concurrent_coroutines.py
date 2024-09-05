#!/usr/bin/env python3
"""
This module provides an asynchronous routine to spawn multiple
wait_random coroutines and collect their results in ascending
order without using sort().
"""

import asyncio
from typing import List, Any

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay time for wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    # We build a new list in ascending order manually
    ordered_delays = []
    while delays:
        min_delay = min(delays)
        ordered_delays.append(min_delay)
        delays.remove(min_delay)

    return ordered_delays
