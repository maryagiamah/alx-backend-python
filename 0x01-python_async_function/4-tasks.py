#!/usr/bin/env python3
"""Take the code from wait_n into a new function task_wait_n"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """async routine called task_wait_n"""
    task = [task_wait_random(max_delay) for _ in range(n)]
    return [await complete for complete in asyncio.as_completed(task)]
