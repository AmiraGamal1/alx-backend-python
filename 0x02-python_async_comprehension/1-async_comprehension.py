#!/usr/bin/env python3
'''python Async
'''
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''list of 10 random number generator
    '''
    return [num async for num in async_generator()]
