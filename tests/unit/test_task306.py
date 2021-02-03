import pytest

from tasks.lesson3.task306 import solution


@pytest.mark.unit
def test_wrong_age():
    result = solution("-1")
    assert result == "Wrong input"


@pytest.mark.unit
def test_baby():
    result = solution("1")
    assert result == "CocaCola"


@pytest.mark.unit
def test_old():
    result = solution("20")
    assert result == "Beer"


@pytest.mark.unit
def test_unhappy():
    result = solution("twenty")
    assert result == "Wrong input"
