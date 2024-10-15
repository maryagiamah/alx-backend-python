#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments"""
import random


async def async_generator() -> int:
    for i in range(10):
        yield i
