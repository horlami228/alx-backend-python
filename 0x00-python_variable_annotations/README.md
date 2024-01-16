# PYTHON VARIABLE ANNOTATIONS

```PY
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

```

```PY
#!/usr/bin/env python3

"""make multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies its argument
    by the given multiplier."""
    def multiplier_func(value: float) -> float:
        return value * multiplier

    return multiplier_func

```
