#!/usr/bin/env python3

"""duck type"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing
    the elements from lst and their lengths."""

    return [(i, len(i)) for i in lst]
