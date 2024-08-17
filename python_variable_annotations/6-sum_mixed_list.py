#!/usr/bin/env python3
"""
This module provides a function to calculate the sum of
a list containing both integers and floats.
The function returns the sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing both integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of
        integers and floats to sum.

    Returns:
        float: The sum of all the numbers in the list.
    """
    return sum(mxd_lst)
