#!/usr/bin/env python3

"""measure runtime"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measure the async operation of all async comnprehension call"""
    task = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    start_time = time.time()

    await asyncio.gather(*task)

    end_time = time.time()

    return end_time - start_time
