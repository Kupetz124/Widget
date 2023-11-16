from typing import Generator


def filter_by_currency(data: list[dict] | Generator, currency: str) -> Generator:
    """
    Принимает список словарей (или объект, выдающий по одному словари с транзакциями),
    и возвращает итератор с банковскими операциями, в которых указана заданная валюта
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
    for item in data:
        yield item["description"]


def card_number_generator(start: int, end: int) -> Generator:
    """
    Генерирует номера банковских карт в заданном диапазоне
    :param start:начало диапазона
    :param end:конец диапазона
    :return:generator object с номерами банковских карт
    """

    # создаём строку с номером карты
    for item in range(start, end + 1):
        number = "0" * (16 - len(str(item))) + str(item)

        # разбиваем строку пробелами через 4 символа
        yield f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:]}"
