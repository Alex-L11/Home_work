from masks import get_mask_card_number, get_mask_account


def mask_account_card(card_number: str) -> str:
    """Фуекция маскирует номер карты или счета"""

    number_card = ""
    account_card = ""
    for num in card_number:
        if num.isdigit():
            number_card += num
        else:
            account_card += num
    if len(number_card) == 16:
        masked_num = get_mask_card_number(number_card)
    else:
        masked_num = get_mask_account(number_card)

    return account_card + masked_num


def get_date(date: str) -> str:
    """Функция выводит дату в формате дд.мм.гггг"""

    date_filter = date[8:10] + "." + date[5:7] + "." + date[0:4]

    return date_filter


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(get_date("2024-03-11T02:26:18.671407"))
