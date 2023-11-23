import json
import logging
from typing import Any

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"{__name__}.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(funcName)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

logger.setLevel(logging.INFO)


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
            logger.info("'json' файл прочитан.")
            return json.load(file)
    except json.JSONDecodeError:
        logger.info("Ошибка 'json.JSONDecodeError'")
        return []
    except FileNotFoundError:
        logger.info("Ошибка 'FileNotFoundError'")
        return []


def get_sum_transaction(data: dict) -> float | str:
    """
    Принимает на вход одну транзакцию и возвращает сумму транзакции в рублях
    :param data: словарь с данными одной транзакции
    :return: сумма транзакции или сообщение об ошибке
    """
    if data["operationAmount"]["currency"]["code"] == "RUB":
        logger.info("Получена транзакция в 'RUB'.")
        return float(data["operationAmount"]["amount"])
    else:
        logger.info("Валюта транзакции не в рублях.")
        return "ValueError: Транзакция выполнена не в рублях. Укажите транзакцию в рублях."
