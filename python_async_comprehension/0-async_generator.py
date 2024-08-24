#!/usr/bin/env python3
"""async generator task 0"""
import asyncio
import random
from typing import Generator

"""
This module defines a coroutine that generates random numbers asynchronously.

The coroutine `async_generator` yields random float numbers between 0 and 10,
waiting for 1 second asynchronously before each yield.
"""


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates a sequence of 10 random numbers.

    This coroutine loops 10 times. In each iteration, it asynchronously waits
    for 1 second and then yields a random float number between 0 and 10.

    Returns:
        A generator that yields random float numbers between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
