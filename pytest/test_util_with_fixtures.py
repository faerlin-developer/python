import pytest

from util import Calculator


@pytest.fixture(scope="function")
def calculator():
    calc = Calculator()
    calc.setup()
    yield calc
    calc.teardown()


@pytest.fixture(scope="class")
def calculator_per_instance():
    calc = Calculator()
    calc.setup()
    yield calc
    calc.teardown()


@pytest.fixture(scope="module")
def calculator_per_module():
    # Called once per file
    pass


@pytest.fixture(scope="session")
def calculator_per_session():
    # Called once per test session (all files)
    pass


def test_add(calculator):
    assert calculator.add(1, 2) == 3


def test_divide(calculator):
    assert calculator.divide(6, 2) == 3


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (2.5, 2.5, 5.0)
    ]
)
def test_divide_parameterized(calculator, a, b, expected):
    assert calculator.add(a, b) == expected


class TestCalculator:

    def test_add(self, calculator_per_instance):
        assert calculator_per_instance.add(1, 2) == 3

    def test_divide(self, calculator_per_instance):
        assert calculator_per_instance.divide(6, 2) == 3
