#!/usr/bin/env python3
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a list where each element from the input tuple is repeated
    'factor' number of times.

    Args:
        lst (Tuple): A tuple of elements.
        factor (int, optional): The number of times each element
        should be repeated. Defaults to 2.

    Returns:
        List: A list where each element is repeated 'factor' times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
