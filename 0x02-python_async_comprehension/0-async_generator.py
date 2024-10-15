#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments"""
from typing import Generator
from random import uniform
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """Async Generator"""
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
