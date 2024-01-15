#!/usr/bin/env python3
"""
0. The basics of async
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay seconds
    and eventually returns it
    """
    ran = random.random() * max_delay
    await asyncio.sleep(ran)
    return ran
