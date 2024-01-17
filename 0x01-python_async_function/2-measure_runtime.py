#!/usr/bin/env python3

"""measure run time"""
import time
import asyncio
module = __import__("1-concurrent_coroutines")
wait_n = module.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time"""
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    return (end_time - start_time) / n
