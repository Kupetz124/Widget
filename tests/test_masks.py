import pytest

from src.masks import mask_the_card, mask_the_score


@pytest.mark.parametrize(
    "data_card, result_card",
    [("7158300734726758", "7158 30** **** 6758"), ("6831982476737658", "6831 98** **** 7658")],
)
def test_mask_the_card(data_card, result_card):
    assert mask_the_card(data_card) == result_card


@pytest.mark.parametrize(
    "data_score, result_score",
    [("48894435694657014368", "**4368"), ("72082042523231456215", "**6215"), ("90424923579946435907", "**5907")],
)
def test_mask_the_score(data_score, result_score):
    assert mask_the_score(data_score) == result_score
