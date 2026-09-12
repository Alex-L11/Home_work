import json
import os
from typing import Any

from src.external_api import currency_converter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_list_transactions(way_json: str) -> list[dict[str, Any]]:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    file_path = os.path.join(BASE_DIR, "data", way_json)
    try:
        with open(file_path, "r", encoding="utf-8") as file_transactions:
            try:
                transaction_data = json.load(file_transactions)
                if not isinstance(transaction_data, list):
                    return []
                return transaction_data
            except json.JSONDecodeError:
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []


def get_transaction(data_trans: dict[str, Any]) -> float:
    """Принимает транзакцию и возвращает сумму транзакции в рублях."""
    get_amount = data_trans.get("operationAmount", {})
    get_currency = get_amount.get("currency", {})
    amount_transaction = get_amount.get("amount")

    if isinstance(data_trans, dict):
        currency = get_currency.get("code", "").upper()
    else:
        currency = str(get_currency).upper()

    if not amount_transaction:
        return 0.0

    try:
        amount = float(amount_transaction)
    except (ValueError, TypeError):
        return 0.0

    if currency == "RUB":
        return amount

    if currency in ("EUR", "USD"):
        return currency_converter(currency, amount)

    return currency_converter(currency, amount)
