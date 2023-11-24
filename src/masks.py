# модуль с функциями для маскировки номеров карт и счетов
import logging

from src.logger import record_logs

logger = record_logs(__name__)
logger.setLevel(logging.INFO)


def mask_the_card(number_card: str) -> str:
    """
    Маскирует номер карты.
    :param number_card: Строка с номером карты.
    :return: Строка с замаскированным номером карты.
    """
    logger.info("Номер карты замаскирован.")
    return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[12:]}"


def mask_the_score(number_score: str) -> str:
    """
    Маскирует номер счёта.
    :param number_score: Строка с номером счёта.
    :return:Строка с замаскированным номером счёта.
    """
    logger.info("Номер счёта замаскирован.")
    return "**" + number_score[-4:]
