#!/usr/bin/env python3
"""
0. The basics of async
"""
import random
import time


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay seconds
    and eventually returns it
    """
    ran = random.random() * max_delay
    time.sleep(ran)
    return ran
