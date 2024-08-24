#!/usr/bin/env python3
""" four parallel task 2 """
import asyncio
import time
from typing import List

task_1_async = __import__('1-async_comprehension').async_comprehension

"""
This module defines a coroutine to measure the runtime of executing
async_comprehension four times in parallel.
"""


async def measure_runtime() -> float:
    """
    Measure the total runtime of running async_comprehension four
    times in parallel.

    This coroutine uses asyncio.gather to run async_comprehension four times
    concurrently. It measures and returns the total time taken for the
    concurrent execution.

    Returns:
        The total runtime in seconds as a float.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in 4))
    end_time = time.perf_counter()
    return end_time - start_time
