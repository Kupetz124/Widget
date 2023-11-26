from typing import Any

import pandas as pd


def read_csv(path: str) -> Any:
    """
    Считывает данные из csv файла
    :param path: путь к файлу
    :return: объект DataFrame
    """
    return pd.read_csv(path)


def read_excel(path: str) -> Any:
    """
    Считывает данные из excel файла
    :param path: путь к файлу
    :return: объект DataFrame
    """
    return pd.read_excel(path)
