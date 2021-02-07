import pytest

from tasks.lesson7.task702 import solution, create_matrix, sum_elem_matrix, max_elem_matrix, min_elem_matrix


@pytest.mark.unit
def test_happy():
    matrix, sum_elem, max_elem, min_elem = solution("2", "2")
    for i in matrix:
        for j in i:
            assert 1 <= j <= 9
    int_results = sum_elem, max_elem, min_elem
    for result in int_results:
        assert type(result) == int


@pytest.mark.unit
def test_unhappy():
    result = solution("Ford", "Mustang")
    assert result == ("Wrong input!", "", "", "")


@pytest.mark.unit
def test_create_matrix_happy():
    result = create_matrix("2", "2")
    for i in result:
        for j in i:
            assert 1 <= j <= 9


@pytest.mark.unit
def test_create_matrix_unhappy():
    result = create_matrix("Ford", "VI")
    assert result == "Wrong input!"


@pytest.mark.unit
def test_sum_elements_happy():
    result = sum_elem_matrix([[3, 2, 3], [5, 7, 6], [3, 4, 7]])
    assert result == 40


@pytest.mark.unit
def test_sum_elements_unhappy():
    result = sum_elem_matrix(["Ford"])
    assert result == ""


@pytest.mark.unit
def test_sum_elements_unhappy1():
    result = sum_elem_matrix([["Ford"], ["Mustang"]])
    assert result == ""


@pytest.mark.unit
def test_max_element_happy():
    result = max_elem_matrix([[8, 7, 3], [5, 9, 6], [1, 4, 7]])
    assert result == 9


@pytest.mark.unit
def test_max_element_unhappy():
    result = max_elem_matrix(["Ford"])
    assert result == ""


@pytest.mark.unit
def test_max_element_unhappy1():
    result = max_elem_matrix([["Ford"], ["Mustang"]])
    assert result == ""


@pytest.mark.unit
def test_min_element_happy():
    result = min_elem_matrix([[8, 7, 3], [5, 9, 6], [1, 4, 7]])
    assert result == 1


@pytest.mark.unit
def test_min_element_unhappy():
    result = min_elem_matrix(["Ford"])
    assert result == ""


@pytest.mark.unit
def test_min_element_unhappy1():
    result = min_elem_matrix([["Ford"], ["Mustang"]])
    assert result == ""
