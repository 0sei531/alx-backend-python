#!/usr/bin/env python3
"""
Module 101-safely_get_value
Defines a function safely_get_value that retrieves a value from
    a dictionary (dct) based on a key,
returning the value if found or a default value if not.
"""


from typing import Mapping, Any, Union, TypeVar

# Define a generic type variable
T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: T = None) -> Union[T, None]:
    """
    Return the value from dct corresponding to key, or default if key is not present.

    Args:
        dct (Mapping[Any, T]): A mapping (dictionary-like object) where keys
            are of type Any and values of type T.
        key (Any): The key to search for in dct.
        default (T, optional): The default value to return if key is
            not found in dct. Defaults to None.

    Returns:
        Union[T, None]: The value from dct corresponding to key,
             or default if key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
