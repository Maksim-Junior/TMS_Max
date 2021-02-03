import pytest

from tasks.lesson3.task311 import solution


@pytest.mark.unit
def test_done_adress():
    result = solution("aaa@gmail.com")
    assert result == "aaa@gmail.com"


@pytest.mark.unit
def test_notDone_adress():
    result = solution("Ford")
    assert result == "DOMAIN NAME is not supported"



