# py-timeout

[![Actions Status](https://github.com/YADRO-KNS/py-timeout/workflows/Test%20py-timeout%20Library/badge.svg)](https://github.com/YADRO-KNS/py-timeout/actions)
![PyPI - Status](https://img.shields.io/pypi/status/py-timeout.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/py-timeout.svg)
![PyPI](https://img.shields.io/pypi/v/py-timeout.svg)
![PyPI - License](https://img.shields.io/pypi/l/py-timeout)

----
py-timeout - pure Python process based decorator that provides execution timeout for Python functions and methods. Since it is not based on signals, py-timeout works fine outside the main thread.

### Prerequisites

py-timeout requires python 3.6 or newer versions to run.

### Installing

Cloning project from git repository

```bash
git clone https://github.com/YADRO-KNS/py-timeout.git
```

Installing from PyPi

```bash
pip3 install py-timeout
```

## Examples

```python
import timeout

@timeout.timeout(duration=0.5)
def foo(value: int) -> None:
    ...

...

@timeout.timeout(duration=0.5)
def bar(self, value: str) -> str:
    ...

```

Decorated function or method will be executed as a sub-process with expected life-time of passed duration value.

```python
import timeout
import time

@timeout.timeout(duration=5)
def foo() -> None:
    while True:
        time.sleep(1)
    
try:
    foo()
except timeout.TimeoutException:
    pass
```

In case if for some reason execution will take longer than expected the process will be terminated and TimeoutException will be raised.

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Authors

* **[Andrey Abramenko](https://github.com/Strady)**
* **[Sergey Parshin](https://github.com/shooshp)**

See also the list of [contributors](https://github.com/YADRO-KNS/py-timeout/graphs/contributors) who participated in this project.

## License

The code is available as open source under the terms of the [MIT License](LICENSE).