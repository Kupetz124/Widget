from src.decorators import log
import pytest

path_file = "test.txt"


def read_from_file(file):
    with open(file) as f:
        return f.readlines()


@pytest.mark.parametrize(
    "path, x, y, rez",
    [
        (None, 10, 5, 2),
        (None, 10, 0, "\nУпс... Ошибочка вышла! Проверьте данные!"),
        (path_file, 10, 5, 2),
        (path_file, 10, 0, "\nУпс... Ошибочка вышла! Проверьте данные!"),
    ],
)
def test_log(path, x, y, rez):
    @log(path)
    def divide_numbers(a, b):
        return a // b

    assert divide_numbers(x, y) == rez


def test_writing_to_file():
    assert (
            read_from_file(path_file)[-1][-82:]
            == "<divide_numbers> error: integer division or modulo by zero. Inputs: ((10, 0), {})\n"
    )
