# Виджет банковских операций клиента

## Описание:

Данный виджет находится в стадии разработки, пишется на языке Python.  
На данный момент работают 7 блоков:
* маскирует номер карты
* маскирует номер счета
* фильтрация выполненных операций по статусу
* фильтрация выполненных операций по дате
* итератор для возвращения операций по уазанной валюте
* генератор описания по каждой операции
* генератор номеров банковских карт

## Установка:

1. Клонируйте репозиторий:  

```shell  
   git clone https://github.com/Alex-L11/Home_work.git
```

2. Установка зависимости:
```
pip install -r requiremenys.txt
```
## Использование: 

1. Откройте PyCharm
2. В окне нажмите New project
3. В терминале введите команды из "Установка", пункты 1 и 2

### Пример использования блоков виджета:

#### *1) Блок маскировки номера карты*

код блока:
~~~python
def get_mask_card_number(number: Any) -> str:
    """Принимает номер карты, разбивает номер по 4 цифры и маскирует номер"""
    num_card = str(number)
    mask_card_number = ""
    if len(num_card) == 16:
        mask_card_number = f"{num_card[0:4]} {num_card[4:6]}** **** {num_card[-4:]}"
    else:
        raise TypeError("Введите 16-ти значный номер карты")

    return mask_card_number
   ~~~

*пример вывода данных:*

Пример для карты

Visa Platinum 7000792289606361  # входной аргумент

Visa Platinum 7000 79** **** 6361  # выход функции


#### *2) Блок маскировки номера счета*   
код блока:
~~~python
def get_mask_account(account: int) -> str:
    """Принимает номер счета, возвращает его маску"""

    num_account = str(account)
    if len(num_account) == 20:
        mask_account = f"** {num_account[-4:]}"
    else:
        raise TypeError("Введите 20-ти значный номер счета")

    return mask_account
~~~

*пример вывода данных:*

Счет 73654108430135874305  # входной аргумент

Счет **4305  # выход функции
#### *3) Вывод выполненных операций по статусу*
код блока:
~~~python
def filter_by_state(dict_list: List[dict[str, Any]], state: str = "EXECUTED") -> List[dict[str, Any]]:
    """Функция возвращает новый список словарей и только те словари у которых ключ state соответствует указанному
    значению"""

    # проверяем на пустую строку
    if dict_list == []:
        raise TypeError("Нет данных, повторите ввод данных")

    # проверяем что 'state' строчное значение, если нет выдае ошибку
    if not isinstance(state, str):
        raise TypeError("Неправильное значение 'state'")

    state_up = state.upper()
    # создаем пустой список для отфильтрованных словарей
    dict_list_filter = []

    # проверяем словари на значение 'state', если нет выдает ошибку.
    for dictionary in dict_list:
        if "state" not in dictionary:
            raise TypeError("Нет значения 'state'")
        # создаем переменную значения 'state' и проверяем на условие стррочности и регистра.
        # если условия выполнены, то такой словарь добавляется в новый список
        value = dictionary["state"]
        if isinstance(value, str) and value.upper() == state_up:
            dict_list_filter.append(dictionary)

    return dict_list_filter

~~~
*пример вывода данных:*
Выход функции со статусом по умолчанию 'EXECUTED'

[{'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

Выход функции, если вторым аргументом передано 'CANCELED'

[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

#### *4) Фильтрация выполненных операций по дате*
код блока:
~~~python
def sort_by_date(dict_list: List[dict[str, int | str]], reverse: bool = True) -> List[dict[str, int | str]]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки по дате. По умолчанию
    сортировка по убыванию"""

    # проверяем на пустую строку
    if dict_list == []:
        raise TypeError("Не ввели данные")

    # проверка на формат ввода даты
    for diction in dict_list:
        if len(str(diction["date"])) == 26:
            continue
        else:
            raise TypeError("Введите значения в параметр 'date' в формате: гггг-мм-ддTчч:мм:сс.сссссс")

    dict_list_sorted = sorted(dict_list, key=lambda x: (x["date"], x["id"]), reverse=reverse)

    return dict_list_sorted
~~~

*пример вывода данных:*
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

#### *5) Итератор для возвращения операций по уазанной валюте*
код блока:
~~~python
def filter_by_currency(transactions: List[dict[str, Any]], currency: str) -> Iterator[dict[str, Any]]:
    """Функция принимает на вход список словарей с транзакциями, возвращает по очередно транзакции, где валюта
    операции соответсвует заданной (например USD)"""

    # проверка, что это словарь, если нет пропускаем
    for trans in transactions:
        if not isinstance(trans, dict):
            continue

        operation_amount = trans.get('operationAmount')

        if not isinstance(operation_amount, dict):
            continue

        currency_info = operation_amount.get('currency')

        if isinstance(currency_info, dict) and currency_info.get('code') == currency.upper():
            yield trans
~~~
*пример вывода данных:*

{
"id": 939719570,

"state": "EXECUTED",

"date": "2018-06-30T02:08:58.425572",

"operationAmount": {"amount": "9824.07",

"currency": {"name": "USD","code": "USD"
}

},

"description": "Перевод организации",

"from": "Счет 75106830613657916952",

"to": "Счет 11776614605963066702"

  }

  {
"id": 142264268,

"state": "EXECUTED",

"date": "2019-04-04T23:20:05.206878",

"operationAmount": {"amount": "79114.93", 

"currency": {"name": "USD", "code": "USD"}},

"description": "Перевод со счета на счет",

"from": "Счет 19708645243227258542",

"to": "Счет 75651667383060284188"

   }

#### *6) Генератор описания по каждой операции*
код блока:
~~~python
def transaction_descriptions(description_transaction: List[dict[str, Any]]) -> Iterator[str]:
    """Функкция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    # вводим переменную с кириллицей, для дальнейшего сравнения
    russian_letters = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    for trans in description_transaction:
        descript = trans.get("description")
        if isinstance(descript, str) and bool(russian_letters.intersection(descript)):
            yield descript
~~~
*пример вывода данных:*

    Перевод организации

    Перевод со счета на счет

    Перевод со счета на счет

    Перевод с карты на карту

    Перевод организации

#### *6) Генератор номеров банковских карт*
код блока:
~~~python
def card_number_generator(start_number: int, end_number: int) -> Iterator[str]:
    """Функция принимает начальное и конечное значения номеров, а возвращает номера банковских карт в формате
       ХХХХ ХХХХ ХХХХ ХХХХ, где Х - цифра номера карты. Генератор генерирует номера карт в диапозоне от
       0000 0000 0000 0001 до 9999 9999 9999 9999."""
    # проверка на значения вне диапозона
    if not (1 <= start_number <= end_number <= 9999_9999_9999_9999):
        raise ValueError("Диапозон вне допустимых значений")

    for num in range(start_number, end_number + 1):
        # преобразуем число в строку из 16 символов, заданного формата
        card_number = f"{num:016d}"
        # разделяем по 4 символа, вида 0000 0000 0000 0000
        format_num = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield format_num
~~~
*пример вывода данных:*

    0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005


## Тестирование:

Все модули виджета протестированы, ошибок нет.  
Покрытие тестов 96%

## Документация:

Для получения дополнительной информации о структуре проекта и API можно   
будет найти в [документации](docs/REDME.md)

## Лицензия:

Проект в стадии разработки, лицензия временно отсутсвует.





