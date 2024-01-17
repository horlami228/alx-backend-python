#!/usr/bin/env python3

"""returns an asyncio.Task"""

import asyncio
module = __import__("0-basic_async_syntax")
wait_random = module.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returning an async task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
