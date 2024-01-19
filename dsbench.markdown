---
layout: page
title: DSBench
permalink: /projects/dsbench/
---

# DSBench

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

- **Parameters:**
  - **name** (_str_) – The name of the benchmark.
  - **cumulative** (_bool_ _,_ _optionals_) – Whether to benchmark a function a number of times with different inputs. If the decorated function returns a result, the sum of the total results is displayed. Defaults to False.
  - **range_start** (_int_ _,_ _optional_) – The start value of the range for cumulative benchmarking. Defaults to 0.
  - **range_end** (_int_ _,_ _optional_) – The end value of the range for cumulative benchmarking. Defaults to the decorated function’s first argument.
- **Returns:**
  The decorated function.
- **Return type:**
  function

# Links

[PyPI](https://pypi.org/project/dsbench/) | [GitHub](https://github.com/DemonicSavage/dsbench)
