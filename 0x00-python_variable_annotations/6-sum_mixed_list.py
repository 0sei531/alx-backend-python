#!/usr/bin/env python3
"""
Description: Takes a list mxd_lst of floats and integers
    and returns their sum as a float.
Arguments:
    mxd_lst (List[Union[int, float]]): A list of integers and
    float numbers to sum up.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of elements in mxd_lst.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers
        and float numbers.

    Returns:
        float: The sum of all numbers in the mxd_lst.
    """
    return sum(mxd_lst)
