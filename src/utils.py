import json
import logging
import os
from typing import Any

from src.external_api import currency_converter

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: $(message)s")
file_handler.setFormatter(file_formatter)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_list_transactions(way_json: str) -> list[dict[str, Any]]:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    logger.info("Получение пути до json-файла")
    file_path = os.path.join(BASE_DIR, "data", way_json)
    try:
        logger.info("Запись транзакций в файл")
        with open(file_path, "r", encoding="utf-8") as file_transactions:
            try:
                logger.info("Чтение транзакций")
                transaction_data = json.load(file_transactions)
                if not isinstance(transaction_data, list):
                    return []
                logger.info("Вывод списка транзакций")
                return transaction_data
            except json.JSONDecodeError:
                logger.error('Произошла ошибка "JSONDEcodeError"')
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        logger.error('Ошибка "FileNotFoundError"')
        print("Файл не найден")
        return []


def get_transaction(data_trans: dict[str, Any]) -> float:
    """Принимает транзакцию и возвращает сумму транзакции в рублях."""
    logger.info("Принимаем транзакцию")
    get_amount = data_trans.get("operationAmount", {})
    get_currency = get_amount.get("currency", {})
    amount_transaction = get_amount.get("amount")

    if isinstance(data_trans, dict):
        logger.info("Получаем валюту транзакции")
        currency = get_currency.get("code", "").upper()
    else:
        currency = str(get_currency).upper()

    if not amount_transaction:
        logger.warning("В транзакции нет суммы транзакции")
        return 0.0

    try:
        logger.info("Получаем сумму транзакции")
        amount = float(amount_transaction)
    except ValueError, TypeError:
        logger.error("Не верный формат суммы транзакции")
        return 0.0

    if currency == "RUB":
        logger.info("Вывод суммы транзакции")
        return amount

    if currency in ("EUR", "USD"):
        logger.info("Конвертация валюты в рубли и вывод суммы транзакции")
        return currency_converter(currency, amount)

    return currency_converter(currency, amount)
