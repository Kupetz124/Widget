import os

import pytest

from src.decorators import log

path_file = os.path.join(r"D:\python_project\bank_widget_\tests\test.txt")


@pytest.fixture
def test_str():
    return "<divide_numbers> error: integer division or modulo by zero. Inputs: ((10, 0), {})\n"


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


def test_writing_to_file(test_str):
    assert read_from_file(path_file)[-1][-82:] == test_str
