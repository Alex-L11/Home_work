from src.masks import get_mask_account, get_mask_card_number


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
        masked_num = get_mask_account(int(number_card))
    else:
        raise TypeError("Введите имя и номер карты или счета")

    return account_card + masked_num


def get_date(date: str) -> str:
    """Функция выводит дату в формате дд.мм.гггг"""
    for arg in date:
        if isinstance(arg, (int | float)):
            raise TypeError("Ошибка типа данных")

    if len(date) == 26:
        date_filter = f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
    elif len(date) == 20:
        date_filter = f'{date[8:10]}.{date[5:7]}.{date[0:4]}'
    else:
        raise TypeError("Введите дату формата: гггг-мм-ддTчч:мм:сс.сссссс")

    return date_filter


def return_mask_account_card(card_value: str) -> str:
    """Определяет тип "карта" или "счет" и маскирует нужной функцией"""
    if not isinstance(card_value, str):
        return ""

    if not card_value.strip():
        return ""

    # Извлекаем только цифры
    number_digit = "". join(nc for nc in card_value if nc.isdigit())

    if len(number_digit) == 16:
        name_card = card_value.replace(number_digit, "").strip()
        masked = get_mask_card_number(number_digit)
        return f'{name_card} {masked}'

    elif len(number_digit) == 20:
        masked = get_mask_account(number_digit)
        return f'Счет {masked}'

    else:
        return card_value


def format_transactions(operation: dict) -> str:
    """Форматирует одну транзакцию в виде дата, наименование транакции\n счет или номер карты\n cумма"""
    # вывод даты
    formatted_date = get_date(operation.get('date', ''))
    description = operation.get('description')

    # вывод суммы
    amount = operation.get('amount', 0)
    if isinstance(amount, float) and amount == int(amount):
        amount = int(amount)

    currency_code = operation.get('currency_code')
    if not currency_code:
        cur_info = (operation.get('operationAmount') or {}).get('currency') or {}
        currency_code = cur_info.get('code')

    if currency_code == 'RUB':
        currency_str = 'руб.'
    elif currency_code:
        currency_str = currency_code.upper()
    else:
        currency_str = 'Валюта не указана'

    # откуда/куда
    from_raw = operation.get('from', '')
    to_raw = operation.get('to', '')

    from_str = return_mask_account_card(from_raw) if from_raw else ''
    to_str = return_mask_account_card(to_raw) if to_raw else ''

    # сборка строк
    lines = [f'{formatted_date} {description}']

    if from_str and to_str:
        lines.append(f'{from_str} -> {to_str}')
    elif to_str:
        lines.append(to_str)

    lines.append(f'Сумма: {amount} {currency_str}')

    return '\n'.join(lines)
