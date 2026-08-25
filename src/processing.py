from typing import Any
from typing import List


def filter_by_state(dict_list: List[dict[str, Any]], state: str = 'EXECUTED') -> List[dict[str, Any]]:
    """Функция возвращает новый список словарей, только у которых ключ state соответствует указанному значению"""

    return [item for item in dict_list if item.get('state') == state]


def sort_by_date(dict_list: List[dict[str, Any]], reverse: bool = True) -> List[dict[str, Any]]:
    """Фунция принимает список словарей и необязательный параметр, задающий порядок сортировки по дате. По умолчанию
     сортировка по убыванию"""
    dict_list_sorted = sorted(dict_list, key=lambda x: x['date'], reverse = True)

    return dict_list_sorted
