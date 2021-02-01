import pytest

from tasks.lesson4.task404 import solution


@pytest.mark.unit
def test_happy():
    result = solution("5")
    assert result == 225


@pytest.mark.unit
def test_unhappy():
    result = solution("Ford")
    assert result == "Wrong data"
