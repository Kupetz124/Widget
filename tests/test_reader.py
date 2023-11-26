from unittest.mock import patch

from src.reader import read_csv, read_excel

path = "../data/transactions_excel.xlsx"
path_csv = "../data/transactions.csv"


@patch("pandas.read_csv")
def test_read_csv(mock_get):
    mock_get.return_value = ["name", "price", "quantity"]
    assert read_csv(path_csv) == ["name", "price", "quantity"]


@patch("pandas.read_excel")
def test_read_excel(mock_get):
    mock_get.return_value = ["name", "price", "quantity"]
    assert read_excel(path) == ["name", "price", "quantity"]
