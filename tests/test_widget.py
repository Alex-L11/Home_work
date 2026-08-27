import pytest
from typing import Any

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('value, expected', [
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
    ('Счет 73654108430135874305', 'Счет ** 4305'),
    ('', TypeError),
    ('Mas 233435', TypeError)
    ])
def test_mask_account_card(value: str, expected: str) -> Any:
    if value == '' or None or len(value) < 16:
        with pytest.raises(TypeError):
            mask_account_card(value)
    else:
        assert mask_account_card(value) == expected


def test_get_date(date: str) -> Any:
    assert get_date(date) == "11.03.2024"

    with pytest.raises(TypeError):
        get_date('23234.334.23.asw.22')

    with pytest.raises(TypeError):
        get_date('1234566548')

    with pytest.raises(TypeError):
        get_date('')
