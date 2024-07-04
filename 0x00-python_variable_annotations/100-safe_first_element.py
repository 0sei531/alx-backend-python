#!/usr/bin/env python3
"""
Module 100-safe_first_element
Defines a function safe_first_element that safely returns the first
    element of a sequence or None if the sequence is empty.
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of lst if lst is not empty, otherwise return None.

    Args:
        lst (Sequence[Any]): A sequence of elements of any type.

    Returns:
        Union[Any, None]: The first element of lst if not empty, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
