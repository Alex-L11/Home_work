from typing import List, Any, Iterable
import pytest
from src.generators import filter_by_currency


def test_filter_by_currency_exactly_one_valid(transactions_all):
    gen = filter_by_currency(transactions_all, "usd")

    #Проверка первого элемента, что он не None
    first = next(gen, None)
    assert first is not None

    #Проверяем что валюта именно USD и что регистр написания не важен
    currency_code = (
        first.get("operationAmount", {})
        .get("currency", {})
        .get("code")
    )
    assert currency_code == "USD"

# проверка кода на continue
def test_filter_by_currency_no_dict(transactions_no_dict):
    result = list(filter_by_currency(transactions_no_dict, "usd"))
    assert len(result) == 1
    assert result[0]["id"] == 1
    assert (result[0]["operationAmount"]["currency"]["code"] == "USD")


def test_filter_by_currency_no_dictionary_nothing():
    with pytest.raises(TypeError):
        filter_by_currency()


@pytest.mark.parametrize("currency, expected_count", [
    ("USD", 3),
    ("RUB", 2),
])
def test_filter_by_currency_currency_count(transactions_all, currency, expected_count):
    count = sum(1 for _ in filter_by_currency(transactions_all, currency))
    assert count == expected_count
