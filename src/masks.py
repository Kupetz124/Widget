# модуль с функциями для маскировки номеров карт и счетов


def mask_the_card(number_card: str) -> str:
    """
    Маскирует номер карты.
    :param number_card: Строка с номером карты.
    :return: Строка с замаскированным номером карты.
    """
    return f"{number_card[:3]} {number_card[3:5]}** **** {number_card[12:]}"


def mask_the_score(number_score: str) -> str:
    """
    Маскирует номер счёта.
    :param number_score: Строка с номером счёта.
    :return:Строка с замаскированным номером счёта.
    """
    return "**" + number_score[-4:]
