# PYTHON ASYNCIO PACKAGE

```py
#!/usr/bin/env python3

"""running concurrent async"""

import asyncio
from typing import List
module = __import__('0-basic_async_syntax')
wait_random = module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times"""

    async def get_waited_random():
        """helper function"""
        return await wait_random(max_delay)

    tasks = [get_waited_random() for _ in range(n)]

    return [await task for task in asyncio.as_completed(tasks)]
```

```py
#!/usr/bin/env python3

"""basic async syntax"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait random"""
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num

```
