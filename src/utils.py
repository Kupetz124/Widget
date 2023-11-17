import json
from typing import Any


def get_transactions_data(file_path: str) -> Any:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список.

    :param file_path: Путь к файлу с данными.
    :return: Список со словарями данных, либо пустой словарь.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []


def get_sum_transaction(data: dict) -> float | str:
    """
    Принимает на вход одну транзакцию и возвращает сумму транзакции в рублях
    :param data: словарь с данными одной транзакции
    :return: сумма транзакции или сообщение об ошибке
    """
    if data["operationAmount"]["currency"]["code"] == "RUB":
        return float(data["operationAmount"]["amount"])
    else:
        return "ValueError: Транзакция выполнена не в рублях. Укажите транзакцию в рублях."
