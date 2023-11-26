import re
from collections import Counter


def filter_operations_by_string(data: list[dict], required_string: str) -> list[dict]:
    """
    Возвращать список словарей, у которых в описании есть заданная строка.
    :param data: Список словарей с операциями.
    :param required_string: Строка, которую ищем в описании операции.
    :return:Список словарей с операциями, содержащих заданную строку в описании.
    """
    pattern = re.compile(required_string)
    return [item for item in data if pattern.search(item["description"])]


def count_categories_of_transactions(transactions: list[dict], categories: dict) -> dict:
    """
    Считает количество операций по выбранным категориям.
    :param transactions: Список со словарями транзакций.
    :param categories: Словарь с выбранными категориями.
    :return: Словарь с количеством выбранных категорий.
    """
    count_dict = Counter(item["description"] for item in transactions)

    new_dict = {}
    for item in categories:
        new_dict[item] = count_dict[item]

    return new_dict
