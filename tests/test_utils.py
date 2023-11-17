import os

import pytest

from src.utils import get_sum_transaction, get_transactions_data


@pytest.fixture
def data():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]


# Получение пути к текущему исполняемому файлу
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = current_dir[: -(len(current_dir.split("\\")[-1]) + 1)]

# Создание относительного пути к файлу от текущего файла
file_path_1 = os.path.join(base_dir, "data", "operations.json")
file_path_2 = os.path.join(base_dir, "tests", "for_tests.json")


def test_get_transactions_data(data):
    assert get_transactions_data(file_path_1)[:2] == data
    assert get_transactions_data("file") == []
    assert get_transactions_data(file_path_2) == []


def test_get_sum_transaction(data):
    assert get_sum_transaction(data[0]) == 31957.58
    assert get_sum_transaction(data[1]) == "ValueError: Транзакция выполнена не в рублях. Укажите транзакцию в рублях."
