 #!/usr/bin/env python3
"""
This module contains a coroutine that generates random numbers asynchronously.
"""

from asyncio import sleep
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Generator that yields a random value between 0 and 10 every second, 10 times."""
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
