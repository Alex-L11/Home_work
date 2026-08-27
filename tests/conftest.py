import pytest


@pytest.fixture
def card_number():
    return 'Visa Platinum 7000 79** **** 6361'


@pytest.fixture
def account_number():
    return 'Счет **4305'


@pytest.fixture
def date():
    return '2024-03-11T02:26:18.671407'

@pytest.fixture
def dict_list_1():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            ]


@pytest.fixture
def dict_list_2():
    return [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            ]

@pytest.fixture
def dict_list_2_a():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            ]
@pytest.fixture
def dict_list_2_b():
    return [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            ]


@pytest.fixture
def dict_list_3():
    return [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},]


@pytest.fixture
def dict_list_4():
    return [{'id': 939719570, 'state': 'EXECUTED'},
            {'id': 41428829, 'state': 'canceled'},
            {'id': 345242, 'state': 'executed'},
            {'id': 345242, 'state': 'random'},
            ]


@pytest.fixture
def dict_list_4_a():
    return [{'id': 939719570, 'state': 'EXECUTED'},
            {'id': 41428829, 'state': 'CANCELED'},
            {'id': 345242, 'state': 'EXECUTED'},
            {'id': 345242, 'state': 'RANDOM'},
            ]


@pytest.fixture
def dict_list_5():
    return [{'id': 4432232}]


@pytest.fixture
def dict_list_date():
    return [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            ]


@pytest.fixture
def dict_list_date_reverse():
    return [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            ]
