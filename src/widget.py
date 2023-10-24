# импорт функций из модуля 'masks.py'
from src import masks


def mask_user_data(card_details: str, score_details: str) -> str:
    """Маскирует данные карты и счёта."""
    data_card = card_details.split()
    data_score = score_details.split()

    return (
        f'{" ".join(data_card[:-1])} {masks.mask_the_card(data_card[-1])}'
        f'\n{" ".join(data_score[:-1])} {masks.mask_the_score(data_score[-1])}'
    )
