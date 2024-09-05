#!/usr/bin/env python3
"""
This module provides a function to measure the execution time of wait_n
and calculate the average time per coroutine.
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return the average time per coroutine.

    Args:
        n (int): The number of coroutines to spawn in wait_n.
        max_delay (int): The maximum delay time for each coroutine.

    Returns:
        float: The average time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    end_time: float = time.time()
    return (end_time - start_time) / n