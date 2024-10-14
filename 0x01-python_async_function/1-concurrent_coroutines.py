#!/usr/bin/env python3
""" write an async routine called wait_n that takes in 2 ints"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """async routine called wait_n that takes in 2 int arguments"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    result = await asyncio.gather(*tasks)
    return result
