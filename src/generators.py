from typing import Generator


def filter_by_currency(data: list[dict] | Generator, currency: str) -> Generator:
    """
    Принимает список словарей (или объект, выдающий по одному словари с транзакциями),
    и возвращает итератор с id банковских операций, в которых указана заданная валюта
    :param data: список словарей или generator object
    :param currency:выбранная валюта
    :return:generator object со списком банковских операций в выбранной валюте.
    """

    return (item for item in data if item["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(data: list[dict]) -> Generator:
    """
    Принимает список словарей и возвращает описание каждой операции по очереди
    :param data:список словарей
    :return:описание банковской операции
    """
    return (item["description"] for item in data)
