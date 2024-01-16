#!/usr/bin/env python3
'''
1. Async Comprehensions
'''
from importlib import import_module as using
from typing import List


gen = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
    '''
    return [d async for d in gen()]
