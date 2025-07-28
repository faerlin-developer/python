import pytest

from util import add, divide


# Standard tests

def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(6, 2) == 3


def test_divide_exception():
    with pytest.raises(ValueError) as exception_info:
        divide(6, 0)

    e = exception_info.value
    assert str(e) == "divide by zero"


# Parameterized test

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (2.5, 2.5, 5.0)
    ]
)
def test_divide_parameterized(a, b, expected):
    assert add(a, b) == expected


# Tests in class
# - The class name must start with the word test
# - Useful to group conceptually related tests
# - Enables dependency injection using scope="class"

class TestUtil:

    def test_add(self):
        assert add(2, 3) == 5

    def test_divide(self):
        assert divide(6, 2) == 3
