from typing import Any

import pytest

from src.widget import get_date, mask_account_card, return_mask_account_card, format_transactions


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет ** 4305"),
        ("", TypeError),
        ("Mas 233435", TypeError),
    ],
)
def test_mask_account_card(value: str, expected: str) -> Any:
    if value == "" or None or len(value) < 16:
        with pytest.raises(TypeError):
            mask_account_card(value)
    else:
        assert mask_account_card(value) == expected


def test_get_date(date: str) -> Any:
    assert get_date(date) == "11.03.2024"

    with pytest.raises(TypeError):
        get_date("23234.334.23.asw.22")

    with pytest.raises(TypeError):
        get_date("1234566548")

    with pytest.raises(TypeError):
        get_date("")


def test_return_mask_account_card() -> None:
    result = return_mask_account_card("Mastercard 1234567890123456")
    assert result == "Mastercard 1234 56** **** 3456"


def test_return_mask_account_card_no_card() -> None:
    assert return_mask_account_card(None) == ""


def test_return_mask_account_card_no_card_1() -> None:
    assert return_mask_account_card(0.0) == ""


def test_format_transactions(dict_for_test) -> None:
    result = format_transactions(dict_for_test)
    assert result == ("06.12.2020 Перевод с карты на карту\n"
                      "Discover 3172 60** **** 0065 -> Discover 0720 42** **** 4643\n"
                      "Сумма: 29740 COP")

