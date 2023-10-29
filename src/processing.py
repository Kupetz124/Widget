def select_by_key(data: list[dict], key: str = "EXECUTED") -> list[dict]:
    """
    Возвращает список словарей, в которых значение ключа "state"
    соответствует второму аргументу функции (по умолчанию "EXECUTED").

    :param data:Список словарей с данными.
    :param key:Значение ключа "state", по умолчанию "EXECUTED"
    :return:Список словарей, содержащих второй аргумент функции по ключу "state".
    """
    return [item for item in data if item["state"] == key]
