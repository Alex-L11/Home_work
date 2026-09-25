from typing import Any, List

import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


def test_filter_by_currency_exactly_one_valid(transactions_all: List[dict[str, Any]]) -> Any:
    gen = filter_by_currency(transactions_all, "usd")

    # Проверка первого элемента, что он не None
    first = next(gen, None)
    assert first is not None

    # Проверяем что валюта именно USD и что регистр написания не важен
    currency_code = first.get("operationAmount", {}).get("currency", {}).get("code")
    assert currency_code == "USD"


# проверка кода на continue
def test_filter_by_currency_no_dict(transactions_no_dict: List[dict[str, Any]]) -> Any:
    result = list(filter_by_currency(transactions_no_dict, "usd"))
    assert len(result) == 1
    assert result[0]["id"] == 1
    assert result[0]["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_no_dictionary_nothing() -> None:
    with pytest.raises(TypeError):
        list(filter_by_currency([], ""))


@pytest.mark.parametrize(
    "currency, expected_count",
    [
        ("USD", 3),
        ("RUB", 2),
    ],
)
def test_filter_by_currency_currency_count(
    transactions_all: list[dict[str, Any]], currency: str, expected_count: int
) -> Any:
    count = sum(1 for _ in filter_by_currency(transactions_all, currency))
    assert count == expected_count


def test_transaction_descriptions_actual(transactions_all: list[dict[str, Any]], trans_descrip_1: list) -> None:
    result = list(transaction_descriptions(transactions_all))
    assert result == trans_descrip_1


def test_transaction_no_descriptions(transactions_no_correct_description: list) -> None:
    result = list(transaction_descriptions(transactions_no_correct_description))
    assert result == []


@pytest.mark.parametrize(
    "start_num, end_num, expected_num",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        )
    ],
)
def test_card_number_generator_norm(start_num: int, end_num: int, expected_num: str) -> None:
    result = card_number_generator(1, 5)
    assert list(result) == expected_num


def test_card_number_generator_no_num() -> None:
    with pytest.raises(ValueError):
        list(card_number_generator(0, 0))
