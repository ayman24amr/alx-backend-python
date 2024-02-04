#!/usr/bin/env python3
"""
to practice the methods
"""
from utils import access_nested_map


print(access_nested_map({}, ("a",)))
print(access_nested_map({"a": 1}, ("a", "b")))