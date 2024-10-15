#!/usr/bin/env python3
'''run time
'''
from time import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure time
    '''
    start = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time() - start
