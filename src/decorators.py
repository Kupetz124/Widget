from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(conclusion: str | None = None) -> Any:
    """
    Пишет логи о вызове функции в файл или в консоль
    :param conclusion: Путь к файлу с логами, если не указан, то идёт вывод сообщения в консоль.
    :return: Логи о вызове и работе функции
    """

    def wrapper(func: Callable) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            # При запуске без ошибок:
            try:
                result = func(*args, **kwargs)

                # Если путь к файлу не указан, выводим сообщение в консоль.
                if conclusion is None:
                    print(f'{datetime.now().strftime("%Y-%M-%d %H:%M:%S")} <{func.__name__}> ok.')

                # Если путь к файлу указан, записываем логи туда.
                else:
                    with open(conclusion, "a", encoding="utf-8") as file:
                        file.write(f'{datetime.now().strftime("%Y-%M-%d %H:%M:%S")} <{func.__name__}>' f" ok.\n")

                # Выводим результат работы декорируемой функции
                return result

            # При возникновении ошибки:
            except Exception as err:
                # Если путь к файлу не указан, выводим сообщение об ошибке и введённые данные в консоль.
                if conclusion is None:
                    print(
                        f'\n{datetime.now().strftime("%Y-%M-%d %H:%M:%S")} <{func.__name__}> '
                        f"error: {err}. Inputs: {args, kwargs}"
                    )
                else:
                    # Если путь к файлу указан, записываем туда сообщение об ошибке и введённые данные.
                    with open(conclusion, "a", encoding="utf-8") as file:
                        file.write(
                            f'{datetime.now().strftime("%Y-%M-%d %H:%M:%S")}'
                            f" <{func.__name__}> error: {err}. Inputs: {args, kwargs}\n"
                        )
                return "\nУпс... Ошибочка вышла! Проверьте данные!"

        return inner

    return wrapper
