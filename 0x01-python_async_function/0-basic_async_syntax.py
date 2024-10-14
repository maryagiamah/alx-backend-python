#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an integer"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """wait for a random delay between 0 and max_delay"""
    x = uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
