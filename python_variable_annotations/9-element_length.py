#!/usr/bin/env python3
"""
This module provides a function that returns a list of tuples.
Each tuple contains an element from the input list and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples.
    Each tuple contains a sequence from the input iterable and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing
        sequences (e.g., lists, strings).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each
        tuple contains a sequence and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
