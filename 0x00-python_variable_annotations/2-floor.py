#!/usr/bin/env python3
"""
Description: A module that defines a function floor which takes a float n
             as an argument and returns the floor of the float.
"""


import math


def floor(n: float) -> int:
    """
    Return the largest int value less than or equal to n.

    Args:
        n (float): The float number to floor.

    Returns:
        int: The floor value of the float number.
    """
    return math.floor(n)
