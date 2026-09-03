import logging
from functools import wraps
from typing import Any, Callable, Optional, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """
    Декоратор для логирования начала и конца выполнения фунции, ее результатов или возникших ошибок.
    Принимает необязательный аргумент "filename", который определяет, куда будут записываться логи:
    - Если filename задан, логи записываются в указанный файл
    - Если filename не задан, логи выводятся в консоль
    """

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # получаем логгер по имени модуля, где определена фукнция (func.__module__)
            logger = logging.getLogger(f"{func.__module__}.{func.__name__}")
            logger.setLevel(logging.INFO)
            # определяем куда записывать лог
            if filename:
                # если filename указан, создаем хендлер, который пишет логи в файл
                handler: logging.Handler = logging.FileHandler(filename, encoding="utf-8")
                # задаем формат строки: время, имя логгера, сообщение
            else:
                # если filename нет, используем StreamHandler для консоли
                handler = logging.StreamHandler()
                # привязываем форматтер к хендлеру и добавляем хендлер к логгеру, чтобы логгер знал как форматировать
            # сообщения и куда их отправлять

            handler.setFormatter(logging.Formatter("%(message)s"))
            logger.handlers.clear()
            logger.addHandler(handler)

            try:
                # выдает сообщение о начале выполнения функции, подставляя ее имя
                logger.info("Начало выполнения %s", func.__name__)
                result = func(*args, **kwargs)
                logger.info("Конец выполнения %s ok", func.__name__)
                return result
            except Exception as e:
                # логгируем тип ошибки
                logger.info(
                    "%s error: %s. Inputs: %r, %r",
                    func.__name__,
                    type(e).__name__,
                    args,
                    kwargs,
                )
                raise

        return wrapper  # type: ignore[return-value]

    return decorator
