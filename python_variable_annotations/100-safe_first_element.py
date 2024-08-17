#!/usr/bin/env python3
"""
This module provides a function to safely retrieve
the first element of a sequence.
If the sequence is empty, it returns None.
"""

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Safely retrieves the first element of a sequence.
    If the sequence is empty, returns None.

    Args:
        lst (Sequence[Any]): A sequence of elements.

    Returns:
        Optional[Any]: The first element of the sequence,
        or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
