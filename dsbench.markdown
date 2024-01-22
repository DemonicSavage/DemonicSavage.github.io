---
layout: page
title: DSBench
permalink: /projects/dsbench/
comment: Small Python library that provides a decorator function which benchmarks functions.
made: true
---

This small library provides a decorator function that benchmarks functions.

# Installation

```bash
pip install dsbench
```

# Usage

```python
import dsbench

@dsbench.benchmark(name="Some Function")
def some_function():
    return 98

my_function()

# prints:
# Some Function:
#   Time: 0:00:00.000002
#   Result: 98
```

# API

### dsbench.benchmark(\*, name: str, cumulative: bool = False, range_start: int = 0, range_end: int = None)

Decorator function for benchmarking other functions.

* **Parameters:**
  * **name** (*str*) – The name of the benchmark.
  * **cumulative** (*bool* *,* *optionals*) – Whether to benchmark a function a number of times with different inputs. If the decorated function returns a result, the sum of the total results is displayed. Defaults to False.
  * **range_start** (*int* *,* *optional*) – The start value of the range for cumulative benchmarking. Defaults to 0.
  * **range_end** (*int* *,* *optional*) – The end value of the range for cumulative benchmarking. Defaults to the decorated function’s first argument.
* **Returns:**
  The decorated function.
* **Return type:**
  function

## License

This software is released under the Apache 2.0 license.

# Links

- [PyPI](https://pypi.org/project/dsbench/)
- [GitHub](https://github.com/DemonicSavage/dsbench)
