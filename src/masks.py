from typing import Any


def get_mask_card_number(number: Any) -> str:
    """Принимает номер карты, разбивает номер по 4 цифры и маскирует номер"""
    num_card = str(number)
    mask_card_number = ""
    if len(num_card) == 16:
        mask_card_number = f"{num_card[0:4]} {num_card[4:6]}** **** {num_card[-4:]}"
    else:
        raise TypeError("Введите 16-ти значный номер карты")

    return mask_card_number


def get_mask_account(account: int) -> str:
    """Принимает номер счета, возвращает его маску"""

    num_account = str(account)
    if len(num_account) == 20:
        mask_account = f'** {num_account[-4:]}'
    else:
        raise TypeError("Введите 20-ти значный номер счета")

    return mask_account
