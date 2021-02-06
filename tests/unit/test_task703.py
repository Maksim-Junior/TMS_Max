import pytest
from tasks.lesson7.task703 import solution


@pytest.mark.unit
def test_factorial_happy():
    result = solution("0")
    assert result == 1


@pytest.mark.unit
def test_factorial_happy1():
    result = solution("5")
    assert result == 120


@pytest.mark.unit
def test_factorial_unhappy():
    result = solution("-3")
    assert result == "Wrong input!"


@pytest.mark.unit
def test_factorial_unhappy1():
    result = solution("Ford")
    assert result == "Wrong input!"
