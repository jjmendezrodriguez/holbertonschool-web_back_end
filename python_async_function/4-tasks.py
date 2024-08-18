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
    Spawn task_wait_random n times with the specified max_delay and return
    a list of the delays in ascending order.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay time for each task.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    
    # Return the delays sorted in ascending order without using sort()
    ordered_delays = []
    while delays:
        min_delay = min(delays)
        ordered_delays.append(min_delay)
        delays.remove(min_delay)

    return ordered_delays
