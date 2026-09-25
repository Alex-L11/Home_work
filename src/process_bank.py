import re

from typing import Any
from collections import Counter


def process_bank_search(data: list[dict[str, Any]], search: str) -> list[dict[str, Any]]:
    """Принимает список словарей с данными о банковских операциях и строку поиска, возвращает список словарей, у
    которых в описании есть данная строка."""

    # задаем шаблон поиска независимо от регистра
    pattern = re.compile(search, flags=re.IGNORECASE)
    bank_trans = []
    if search == "":
        raise TypeError("Пустая строка для поиска")
    for item in data:
        # получаем ключ, где будет происходить поиск по строке
        description = item.get('description')
        if description is None:
            continue
        if pattern.search(str(description)):
            bank_trans.append(item)

    return bank_trans


def process_bank_operations(data: list[dict[str, Any]], categories: list) -> dict[str, int]:
    """Принимает список словарей с данными о банковских операциях и список категорий операций, возвращает словарь,
    в котором ключи - это названия категорий, значения - это количетсво операций в каждой категории."""

    if not categories:
        raise TypeError("Пустой список категорий")
    # Объединяем все категории в один паттерн через ИЛИ
    pattern = re.compile("|".join(categories), re.IGNORECASE)

    cat = []

    for item in data:
        # ищем ключ "description"
        description = item.get("description", "")
        # возвращаем список всех найденных значений, которые совпали с шаблоном и добавляем все в общий список
        cat.extend(pattern.findall(description))
    # создаем счетчик по каждой категории
    result = Counter(cat)

    return dict(result)
