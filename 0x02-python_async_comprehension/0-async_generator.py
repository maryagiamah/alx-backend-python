#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments"""
from random import uniform
import asyncio


async def async_generator() -> float:
    for i in range(10):
        asyncio.sleep(1)
        yield uniform(0, 10)
