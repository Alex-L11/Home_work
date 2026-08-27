from typing import List, Any


def filter_by_state(dict_list: List[dict[str, Any]], state: str = "EXECUTED") -> List[dict[str, Any]]:
    """Функция возвращает новый список словарей и только те словари у которых ключ state соответствует указанному значению"""
    #проверяем на пустую строку
    if dict_list == '':
        raise TypeError("Нет данных, повторите ввод данных")
    #проверяем что 'state' строчное значение, если нет выдае ошибку
    if not isinstance(state, str):
        raise TypeError("Неправильное значение 'state'")

    state_up = state.upper()
    #создаем пустой список для отфильтрованных словарей
    dict_list_filter = []

    #проверяем словари на значение 'state', если нет выдает ошибку.
    for dictionary in dict_list:
        if "state" not in dictionary:
            raise TypeError("Нет значения 'state'")
    #создаем переменную значения 'state' и проверяем на условие стррочности и регистра.
    # Если условия выполнены, то такой словарь добавляется в новый список
        value = dictionary["state"]
        if isinstance(value, str) and value.upper() == state_up:
            dict_list_filter.append(dictionary)

    return dict_list_filter


def sort_by_date(dict_list: List[dict[str, int | str]], reverse: bool = True) -> List[dict[str, int | str]]:
    """Фунция принимает список словарей и необязательный параметр, задающий порядок сортировки по дате. По умолчанию
     сортировка по убыванию"""
    dict_list_sorted = sorted(dict_list, key=lambda x: x['date'], reverse = True)

    return dict_list_sorted



if __name__ == '__main__':
    print(filter_by_state([{'id': 594226727, 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'date': '2018-10-14T08:21:33.419441'}]))