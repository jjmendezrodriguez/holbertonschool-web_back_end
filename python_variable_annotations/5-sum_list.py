#!/usr/bin/env python3
"""
This module provides a function to calculate the sum
of a list of floating-point numbers.
The function returns the sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): A list of floating-point numbers to sum.

    Returns:
        float: The sum of all the numbers in the list.
    """
    return sum(input_list)
