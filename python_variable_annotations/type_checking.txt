#!/usr/bin/env python3
from typing import List, Tuple, Union


def zoom_array(
    lst: Tuple[Union[int, float], ...], factor: int = 2
        ) -> List[Union[int, float]]:
    """
    Returns a list where each element from the input tuple is repeated
    'factor' number of times.

    Args:
        lst (Tuple[Union[int, float], ...]): A tuple of integers or floats.
        factor (int, optional): The number of times each element should be
        repeated. Defaults to 2.

    Returns:
        List[Union[int, float]]: A list where each element is
        repeated 'factor' times.
    """
    zoomed_in: List[Union[int, float]] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Updated to tuple

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
