def select_by_key(data: list[dict], key: str = "EXECUTED") -> list[dict]:
    """
    Возвращает список словарей, в которых значение ключа "state"
    соответствует второму аргументу функции (по умолчанию "EXECUTED").

    :param data:Список словарей с данными.
    :param key:Значение ключа "state", по умолчанию "EXECUTED"
    :return:Список словарей, содержащих второй аргумент функции по ключу "state".
    """
    return [item for item in data if item["state"] == key]


def sort_by_date(data: list[dict], reversal: bool = True) -> list[dict]:
    """
    Сортирует список словарей по дате (ключ "date").
    Если reversal == True, то идёт сортировка по убыванию.

    :param data:Список словарей с данными.
    :param reversal:Тип (bool), по умолчанию "True" для направления сортировки.
    :return:Список словарей, отсортированный по дате (ключ "date").
    """
    return sorted(data, key=lambda x: x["date"], reverse=reversal)
