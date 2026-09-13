import logging
from typing import Any

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: $(message)s")
file_handler.setFormatter(file_formatter)


def get_mask_card_number(number: Any) -> str:
    """Принимает номер карты, разбивает номер по 4 цифры и маскирует номер"""
    logger.info("Получаем номер карты")
    num_card = str(number)
    mask_card_number = ""
    if len(num_card) == 16:
        logger.info("Маскируем номер карты")
        mask_card_number = f"{num_card[0:4]} {num_card[4:6]}** **** {num_card[-4:]}"
    else:
        logger.error("Введен неправильный номер карты")
        raise TypeError("Введите 16-ти значный номер карты")

    return mask_card_number


def get_mask_account(account: int) -> str:
    """Принимает номер счета, возвращает его маску"""
    logger.info("Принимаем номер счета")

    num_account = str(account)
    if len(num_account) == 20:
        logger.info("Маскируем номер счета")
        mask_account = f"** {num_account[-4:]}"
    else:
        logger.error("Введен неправильный номер счета")
        raise TypeError("Введите 20-ти значный номер счета")

    return mask_account
