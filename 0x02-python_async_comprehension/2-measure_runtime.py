#!/usr/bin/env python3
'''
2. Run time for four parallel comprehensions
'''
import asyncio
import time
from importlib import import_module as using


comp = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    execute async_comprehension four times in parallel using asyncio.gather
    measure the total runtime and return it
    '''
    t = time.time()
    await asyncio.gather(*(comp() for _ in range(4)))
    return time.time() - t
