from typing import List, Any, Iterable

import pytest


@pytest.fixture
def card_number() -> str:
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def account_number() -> str:
    return "Счет **4305"


@pytest.fixture
def date() -> str:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def dict_list_1() -> list[dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def dict_list_2() -> list[dict[str, Any]]:
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def dict_list_2_a() -> list[dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def dict_list_2_b() -> list[dict[str, Any]]:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def dict_list_3() -> list[dict[str, Any]]:
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def dict_list_4() -> list[dict[str, Any]]:
    return [
        {"id": 939719570, "state": "EXECUTED"},
        {"id": 41428829, "state": "canceled"},
        {"id": 345242, "state": "executed"},
        {"id": 345242, "state": "random"},
    ]


@pytest.fixture
def dict_list_4_a() -> list[dict[str, Any]]:
    return [
        {"id": 939719570, "state": "EXECUTED"},
        {"id": 41428829, "state": "CANCELED"},
        {"id": 345242, "state": "EXECUTED"},
        {"id": 345242, "state": "RANDOM"},
    ]


@pytest.fixture
def dict_list_5() -> list[dict[str, int]]:
    return [{"id": 4432232}]


@pytest.fixture
def dict_list_date() -> list[dict[str, Any]]:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def dict_list_date_reverse() -> list[dict[str, Any]]:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def transactions_all() -> List[dict[str, Any]]:
    return  [
            {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


@pytest.fixture
def transactions_usd() -> List[dict[str, Any]]:
   return [{
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229"
        }]


@pytest.fixture
def transactions_usd_one_operation() -> List[dict[str, Any]]:
   return [{
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }]


@pytest.fixture
def transactions_no_dict() -> List[dict[str,Any]]:
   return [{
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": "no"},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
       {
           "id": 939719570,
           "state": "EXECUTED",
           "date": "2018-06-30T02:08:58.425572",
           "operationAmount": {},
           "description": "Перевод организации",
           "from": "Счет 75106830613657916952",
           "to": "Счет 11776614605963066702"
       },
       {},
       {
           "id": 1,
           "state": "EXECUTED",
           "date": "2018-06-30T02:08:58.425572",
           "operationAmount": {
               "amount": "9824.07",
               "currency": {"name": "USD", "code": "USD"}},
           "description": "Перевод организации",
           "from": "Счет 75106830613657916952",
           "to": "Счет 11776614605963066702"
       },
   ]

@pytest.fixture
def trans_descrip_1():
    return ["Перевод организации",
    "Перевод со счета на счет",
    "Перевод со счета на счет",
    "Перевод с карты на карту",
    "Перевод организации"]


@pytest.fixture
def transactions_no_correct_description() -> List[dict[str, Any]]:
   return [{
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}},
            "description": "assdd",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"}},
            "description": "",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"}},
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229"
        },
       {
           "id": 895315941,
           "state": "EXECUTED",
           "date": "2018-08-19T04:27:37.904916",
           "operationAmount": {
               "amount": "56883.54",
               "currency": {"name": "USD", "code": "USD"}},
           "description": "123",
           "from": "Visa Classic 6831982476737658",
           "to": "Visa Platinum 8990922113665229"
       }
   ]
