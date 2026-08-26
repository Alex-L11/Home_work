from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_number: str) -> str:
    """Функция маскирует номер карты или счета"""

    number_card = ""
    account_card = ""

    for num in card_number:
        if num.isdigit():
            number_card += num
        else:
            account_card += num
    if len(number_card) == 16:
        masked_num = get_mask_card_number(number_card)
    elif len(number_card) == 20:
        masked_num = get_mask_account(number_card)
    else:
        raise TypeError("Введите имя и номер карты или счета")

    return account_card + masked_num


def get_date(date: str) -> str:
    """Функция выводит дату в формате дд.мм.гггг"""
    for arg in date:
        if isinstance(arg, (int | float)):
            raise TypeError("Ошибка типа данных")

    if len(date) == 26:
        date_filter = f'{date[8:10]}.{date[5:7]}.{date[0:4]}'
    else:
        raise TypeError("Введите дату формата: гггг-мм-ддTчч:мм:сс.сссссс")

    return date_filter



