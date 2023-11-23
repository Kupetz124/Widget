# модуль с функциями для маскировки номеров карт и счетов

import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"{__name__}.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(funcName)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

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
