#!/usr/bin/env python3
"""
This module provides an asynchronous routine to spawn multiple
task_wait_random tasks and collect their results in ascending
order without using sort().
"""

from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay time for task_wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
