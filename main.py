from src import masks
from src import utils


def main() -> None:
    num_card = input("Введите номер карты\n")
    num_score = input("Введите номер счёта\n")

    print(masks.mask_the_card(num_card))
    print(masks.mask_the_score(num_score))

    file_path = "ddata/operations.json"
    test_data = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }

    utils.get_transactions_data(file_path)
    utils.get_sum_transaction(test_data)


if __name__ == "__main__":
    main()
