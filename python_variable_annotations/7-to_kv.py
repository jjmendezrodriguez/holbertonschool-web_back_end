#!/usr/bin/env python3
"""
This module provides a function that takes a string and
a number (int or float), and returns a tuple.
The first element is the string, and the second element
is the square of the number, represented as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the given string,
    and the second element is the square of the given number (int or float),
    represented as a float.

    Args:
        k (str): The string value.
        v (Union[int, float]): The number to be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element
        is the string k, and the second element is the
        square of v as a float.
    """
    return (k, float(v ** 2))
