import pytest

from tasks.lesson3.task310 import solution


@pytest.mark.unit
def test():
    result = solution("34.65")
    assert result == ('34 rubles and 65 penny!', ['💸 20 rubles --> 1', '💸 10 rubles --> 1', '💰 2 rubles --> 2'],
                      ['💰 50 penny --> 1', '💰 10 penny --> 1', '💰 5 penny --> 1'])
