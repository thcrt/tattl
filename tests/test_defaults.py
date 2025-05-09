from dataclasses import dataclass, field


def my_float_factory():
    return {"spam": 1.23, "ham": 4.56, "eggs": 7.89}


@dataclass
class Structure:
    foo: str = "AAA"
    bar: int = 123
    baz: bool = field(default=True)
    qux: list[str] = field(default_factory=list)
    cor: dict[str, float] = field(default_factory=my_float_factory)


EXAMPLE_TOML = """
# There's nothing here! Hopefully we see our defaults in use.
"""


def test_example():
    import tattl
    import tomllib

    data = tattl.unpack_dict(tomllib.loads(EXAMPLE_TOML), Structure)
    print(data)
    assert data == Structure(
        foo="AAA",
        bar=123,
        baz=True,
        qux=[],
        cor={"spam": 1.23, "ham": 4.56, "eggs": 7.89},
    )
