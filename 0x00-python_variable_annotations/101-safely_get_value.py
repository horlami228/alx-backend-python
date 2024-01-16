#!/usr/bin/env python3

"""TypeVar"""
from typing import TypeVar, Dict, Any, Mapping, Union, Optional
T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Get a value from the dictionary if it exists.
    Otherwise return the provided default."""
    if key in dict:
        return dct[key]
    else:
        return default
