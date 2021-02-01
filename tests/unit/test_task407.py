import pytest

from tasks.lesson4.task407 import solution


@pytest.mark.unit
def test_happy():
    result = solution("2", "4")
    assert result == ([2, 3, 4], 3)


@pytest.mark.unit
def test_unhappy():
    result = solution("Ford", "5")
    assert result == ("Wrong data!", "")


@pytest.mark.unit
def test_frs_greater_scd():
    result = solution("3", "2")
    assert result == ("first integer(A) should be less than second integer(B)...", "")
