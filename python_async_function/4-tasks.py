#!/usr/bin/env python3
"""
This module provides a function to create and execute multiple asyncio tasks
using task_wait_random and return the results in ascending order.
"""

import asyncio
from typing import List

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
    # Create a list of tasks by calling task_wait_random n times with max_delay
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Wait for all tasks to complete and gather their results
    delays = await asyncio.gather(*tasks)

    # Return the delays sorted in ascending order
    return sorted(delays)
