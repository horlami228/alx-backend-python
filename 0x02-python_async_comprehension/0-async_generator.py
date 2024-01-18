#!/usr/bin/env python3

"""async generator"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """async generator that loops 10 times
    wait 1 second and yeild a random number"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
