import pytest

from tasks.lesson5.task503 import solution, count_of_seven


@pytest.mark.unit
def test_happy():
    result1, result2 = solution("2", "2")
    for i in result1:
        for j in i:
            assert 1 <= j <= 9
    assert type(result2) == int


@pytest.mark.unit
def test_unhappy():
    result = solution("Ford", "Mustang")
    assert result == ("Wrong input!", "")


@pytest.mark.unit
def test_sum_elements_happy():
    result = count_of_seven([[3, 2, 3], [5, 7, 6], [3, 4, 7]])
    assert result == 2


@pytest.mark.unit
def test_sum_elements_unhappy1():
    result = count_of_seven(["Ford"])
    assert result == ""


@pytest.mark.unit
def test_sum_elements_unhappy1():
    result = count_of_seven([["Ford"], ["Mustang"]])
    assert result == ""
