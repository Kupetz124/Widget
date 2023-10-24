from src import masks


def main() -> None:
    num_card = input("Введите номер карты\n")
    num_score = input("Введите номер счёта\n")

    print(masks.mask_the_card(num_card))
    print(masks.mask_the_score(num_score))


if __name__ == "__main__":
    main()
