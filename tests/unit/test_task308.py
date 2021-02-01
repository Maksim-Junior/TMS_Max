import pytest

from tasks.lesson3.task308 import solution


@pytest.mark.unit
def test_happy():
    result = solution("4")
    assert result == 64.0


@pytest.mark.unit
def test_unhappy():
    result = solution("Ford")
    assert result == "Wrong input!"

