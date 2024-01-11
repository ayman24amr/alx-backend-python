#!/usr/bin/env python3
"""
0. Basic annotations - add
"""
from typing import Any, Union, Mapping, T


def safely_get_value(
                     dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None
    ) -> Union[Any, T]:
    """
    function
    """
    if key in dct:
        return dct[key]
    else:
        return default