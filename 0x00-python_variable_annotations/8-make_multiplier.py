#!/usr/bin/env python3

"""make multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies its argument
    by the given multiplier."""
    def multiplier_func(value: float) -> float:
        return value * multiplier

    return multiplier_func
