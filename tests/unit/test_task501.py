import pytest

from tasks.lesson5.task501 import solution


@pytest.mark.unit
def test_happy():
    result = solution("4")
    for i in result:
        for j in i:
            assert 1 <= j <= 9


@pytest.mark.unit
def test_unhappy():
    result = solution("Ford")
    assert result == "Wrong input!"
