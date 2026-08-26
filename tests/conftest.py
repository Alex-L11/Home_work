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