import pytest

from tasks.lesson3.task307 import solution


@pytest.mark.unit
def test_more():
    result = solution("FordMustang")
    assert result == "FordMustang"


@pytest.mark.unit
def test_less():
    result = solution("Ford")
    assert result == "Need more!"


@pytest.mark.unit
def test_five():
    result = solution("Fords")
    assert result == "It is five"



