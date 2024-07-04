#!/usr/bin/env python3
"""
Description: Takes a list input_list of floats as argument and returns
     their sum as a float.
Arguments:
    input_list (List[float]): A list of float numbers to sum up.
"""


from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of all elements in input_list.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of all float numbers in the input_list.
    """
    return sum(input_list)
