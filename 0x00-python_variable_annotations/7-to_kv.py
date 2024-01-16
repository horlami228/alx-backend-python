#!/usr/bin/env python3

"""returning a tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of (key, value) from input arguments."""
    return k, v ** 2
