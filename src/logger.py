import logging
from datetime import datetime
from typing import Any


def record_logs(mod_name: Any) -> Any:
    """
    Выполняет запись лог информации в файл
    :param mod_name: переменная '__name__'
    :return: объект "Логгер".
    """
    date = datetime.now().strftime("%d.%m.%Y")
    my_logger = logging.getLogger(mod_name)
    file_handler = logging.FileHandler(f"data/logs/{date}.log", encoding="utf-8")
    file_formatter = logging.Formatter("%(asctime)s %(name)s %(funcName)s %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    my_logger.addHandler(file_handler)
    return my_logger
