#!/usr/bin/env python3
"""
This module contains a coroutine that collects random numbers using an async comprehension.
"""

from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """Return a list of values yielded by async_generator."""
    return [value async for value in async_generator()]
