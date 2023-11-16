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
