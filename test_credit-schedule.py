import pytest

from credit_schedule import credit_schedule

@pytest.mark.parametrize("amount, percent, time, date, expected", [
    ()
])
def test_0(amount, percent, time, date, expected):
    assert credit_schedule(amount, percent, time, date) == expected
