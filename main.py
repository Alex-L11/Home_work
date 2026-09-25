import os
from typing import Hashable, Any

from src.generators import filter_by_currency
from src.widget import format_transactions
from src.utils import get_list_transactions
from src.processing import filter_by_state, sort_by_date
from src.reading_fin_trans import get_fin_oper_csv, get_fin_oper_xlsx
from src.process_bank import process_bank_search


BASE_PATH = os.path.dirname(os.path.abspath(__file__))

transactions: list[dict[Hashable, Any]] = []


def main() -> None:
    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
            Выберите необходимый пункт меню:
            1. Получить информацию о транзакциях из JSON-файла
            2. Получить информацию о транзакциях из CSV-файла
            3. Получить информацию о транзакциях из XLSX-файла""")
    while True:
        try:
            number = int(input("Введите номер пункта (1-3): "))
            if 1 <= number <= 3:
                break
            else:
                print("Введите число от 1 до 3.")
        except ValueError:
            print("Это не число, Пожалуйста введите 1, 2 или 3.")
    if number == 1:
        print("Для обработки выбран JSON-файл")
        transactions = get_list_transactions("operations.json")
    elif number == 2:
        print("Для обработки выбран CSV-файл")
        transactions = get_fin_oper_csv("transactions.csv")  # type: ignore[assignment]
    elif number == 3:
        print("Для обработки выбран XLSX-файл")
        transactions = get_fin_oper_xlsx("transactions_excel.xlsx")  # type: ignore[assignment]

    while True:
        status_operation = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n "
            "Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING \n"
        ).upper()
        if status_operation in {"EXECUTED", "CANCELED", "PENDING"}:
            break
        else:
            print(f'Статус операции "{status_operation}" не доступен. \n')
    try:
        filter_operations = filter_by_state(transactions, status_operation)
    except TypeError as e:
        print(f'Ошибка: {e}')
        filter_operations = []
    print(f'Операции отфильтрованы по статусу "{status_operation}"\n')

    while True:
        answer_sort = input("Отсртировать операции по дате? Да/Нет \n").strip().lower()
        if answer_sort in {"да", "нет"}:
            break
        else:
            print('Введите "да" или "нет".')

    if answer_sort == "да":
        while True:
            sorted_ascend = input("Отсортировать по возрастанию или по убыванию? \n").strip().lower()
            if sorted_ascend in {"по возрастанию"}:
                filter_operations = sort_by_date(filter_operations, reverse=False)
                break
            elif sorted_ascend in {"по убыванию"}:
                filter_operations = sort_by_date(filter_operations, reverse=True)
                break
            else:
                print('Введите "по возрастанию" или "по убыванию"\n')
    while True:
        answer_rub = input("Выводить только рублевые транзакции? Да/Нет \n").strip().lower()
        if answer_rub in {"да", "нет"}:
            break
        else:
            print('Введите "да" или "нет"')
    if answer_rub == "да":
        filter_operations = list(filter_by_currency(filter_operations, "RUB"))

    while True:
        answer_word = (
            input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет \n").strip().lower()
        )
        if answer_word in {"да", "нет"}:
            break
        else:
            print('Введите "да" или "нет"')

    if answer_word == 'да':
        search_word = input('Введите слово для поиска: \n').strip().lower()
        filter_operations = process_bank_search(filter_operations, search_word)

    print('Распечатываю итоговый список транзакций...')

    print(f'Всего банковских операций в выборке: {len(filter_operations)}')

    for operation in filter_operations:
        print(format_transactions(operation))
        print()
