import os
import json

from typing import Any

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




