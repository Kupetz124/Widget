# импорт функций из модуля 'masks.py'
from src import masks


def mask_user_data(card_details: str, score_details: str) -> str:
    """
    Маскирует данные карты и счёта.
    :param card_details: Строка с данными карты пользователя.
    :param score_details: Строка с данными счёта пользователя.
    :return: Строки с замаскированными данными карты и счёта пользователя.
    """
    data_card = card_details.split()
    data_score = score_details.split()

    return (
        f'{" ".join(data_card[:-1])} {masks.mask_the_card(data_card[-1])}'
        f'\n{" ".join(data_score[:-1])} {masks.mask_the_score(data_score[-1])}'
    )


def format_the_date(data: str) -> str:
    """
    Возвращает удобный для чтения формат даты.
    :param data: Строка с данными о дате транзакции.
    :return: Строка с датой в удобном для чтения формате.
    """
    new_data = data.split("-")

    return f"{new_data[2][:2]}.{new_data[1]}.{new_data[0]}"
