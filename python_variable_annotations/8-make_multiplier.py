#!/usr/bin/env python3
"""
This module provides a function that generates a multiplier function.
The generated function takes a float and multiplies it by a predefined
multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to apply to the float.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        it multiplied by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiplies the input value by the predefined multiplier.

        Args:
            value (float): The float to be multiplied.

        Returns:
            float: The result of value multiplied by the multiplier.
        """
        return value * multiplier

    return multiplier_function
