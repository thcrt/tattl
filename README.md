# TATTL: a Totally Awesome Type-aware TOML Loader

[<img alt="UV Badge" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fastral-sh%2Fuv%2Frefs%2Fheads%2Fmain%2Fassets%2Fbadge%2Fv0.json&style=for-the-badge">](https://docs.astral.sh/uv/)
[<img alt="Python Version Badge" src="https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fthcrt%2Ftattl%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&style=for-the-badge">](#)
[<img alt="PyPI Downloads Badge" src="https://img.shields.io/pypi/dm/tattl?style=for-the-badge&color=blue">](https://pypi.org/project/tattl/)
[<img alt="License Badge" src="https://img.shields.io/pypi/l/tattl?style=for-the-badge&color=blue">](./LICENSE)

[<img alt="Build Status Badge" src="https://img.shields.io/github/actions/workflow/status/thcrt/tattl/publish.yml?event=release&style=for-the-badge">](https://github.com/thcrt/tattl/actions/workflows/publish.yml)
[<img alt="Maintenance Status Badge" src="https://img.shields.io/maintenance/yes/2024?style=for-the-badge">](https://github.com/thcrt/tattl/pulse)
[<img alt="Free Palestine Badge" src="https://img.shields.io/badge/Free%20-%20Palestine%20-%20red?style=for-the-badge">](https://bdsmovement.net/)

TATTL is a library that deserializes arbitrary data and validates that it conforms to a type
structure you define. It will either return an instance of a `dataclass` that you give it, or it
will throw an exception indicating that the data's types don't fit. TATTL supports nesting and
modern type annotations.

<a href="https://thcrt.github.io/tattl/latest/">
    <img alt="Static Badge" src="https://img.shields.io/badge/Read the - Documentation%20-%20blue?style=for-the-badge">
</a>

## Installation

Install TATTL with your favourite Python package manager. We recommend
[`uv`](https://docs.astral.sh/uv/), but `pip` works too.

```sh
pip install tattl
```

```sh
uv add tattl
```

## Get started

TATTL will take some TOML-structured data and transform it into an instance of a dataclass while
validating type annotations. As a basic example:

```python
import tattl
import tomllib
from dataclasses import dataclass

data = """
foo = "Hello, world!"
bar = 3.14
"""

@dataclass
class Structure:
    foo: str
    bar: float

loaded_data = tattl.unpack_dict(
    tomllib.loads(data),
    Structure
)
```

For advanced usage and an API reference, see the [documentation](https://thcrt.github.io/tattl).

## License

This work is available under the terms of the [BSD 3-Clause License](LICENSE).
