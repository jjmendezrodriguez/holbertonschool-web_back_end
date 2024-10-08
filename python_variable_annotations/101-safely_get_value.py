#!/usr/bin/env python3
"""
This module provides a function to safely retrieve a value from a dictionary.
If the key is not present in the dictionary, a default value is returned.
"""

from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any, default: Optional[T] = None
        ) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary. If the key is not found,
    returns a default value.

    Args:
        dct (Mapping): The dictionary from which to retrieve the value.
        key (Any): The key to look up in the dictionary.
        default (Optional[T]): The default value to return if the key is
        not found. Defaults to None.

    Returns:
        Union[Any, T]: The value from the dictionary if the key is found,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
