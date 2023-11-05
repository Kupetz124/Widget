# импорт функций из модуля 'masks.py'
from src import masks


def mask_user_data(data_user: str) -> str:
    """
    Маскирует данные карты или счёта.
    :param data_user: Строка с данными карты или счёта пользователя.
    :return: Строки с замаскированными данными карты или счёта пользователя.
    """
    data_list = data_user.split()

    if data_list[0] == "Счет":
        return f"Счет {masks.mask_the_score(data_list[-1])}"
    else:
        return f'{" ".join(data_list[:-1])} {masks.mask_the_card(data_list[-1])}'


def format_the_date(data: str) -> str:
    """
    Возвращает удобный для чтения формат даты.
    :param data: Строка с данными о дате транзакции.
    :return: Строка с датой в удобном для чтения формате.
    """
    new_data = data.split("-")

    return f"{new_data[2][:2]}.{new_data[1]}.{new_data[0]}"
