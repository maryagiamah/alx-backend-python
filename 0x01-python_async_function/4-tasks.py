#!/usr/bin/env python3
"""Take the code from wait_n into a new function task_wait_n"""
from typing import List
import asyncio
task_wait_random = __import__(3-tasks).task_wait_random


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """async routine called task_wait_n"""
    tasks = [
            asyncio.create_task(task_wait_random(max_delay))
            for _ in range(n)
        ]
    result = await asyncio.gather(*tasks)
    return sorted(result, key=float)
