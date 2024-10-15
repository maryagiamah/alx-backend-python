#!/usr/bin/env python3
"""Import async_comprehension from the previous file"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """write a measure_runtime coroutine"""
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    start_time = time.perf_counter()
    await asyncio.gather(*tasks)
    return time.perf_counter() - start_time
