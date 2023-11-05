import pytest

from src.widget import format_the_date, mask_user_data


@pytest.mark.parametrize(
    "data, result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_user_data(data, result):
    assert mask_user_data(data) == result


def test_format_the_date():
    assert format_the_date("2018-07-11T02:26:18.671407") == "11.07.2018"
