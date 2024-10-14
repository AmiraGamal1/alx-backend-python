#!/usr/bin/env python3
'''basic async programming
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''random wait async coroutine
    '''
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return (wait)

print(asyncio.run(wait_random()))