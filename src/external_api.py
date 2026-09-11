import os

import requests
from dotenv import load_dotenv

load_dotenv()


def currency_converter(currency: str, amount: float) -> float:
    """Принимает наименование валюты (USD, EUR) и конвертирует валюту в рубли."""
    from_currency = currency.upper()
    to_currency = "RUB"

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("Переменная окружения API_KEY не задана")

    headers = {"apikey": api_key}

    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {
        "to": to_currency,
        "from": from_currency,
        "amount": amount,
    }

    response = requests.get(url, headers=headers, params=params)  # type: ignore

    data = response.json()

    result = data.get("result")
    if result is None:
        raise ValueError("Отсутствует поле 'результат'")

    return float(round(result, 2))
