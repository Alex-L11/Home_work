import pytest

from src.process_bank import process_bank_search, process_bank_operations


def test_process_bank_search_data_test(transactions_all: list[dict], transactions_usd: list[dict]) -> None:
    result = process_bank_search(transactions_all, "usd")
    assert result == transactions_usd


def test_process_bank_search_no_search(transactions_all: list[dict]) -> None:
    with pytest.raises(TypeError):
        process_bank_search(transactions_all, "")


def test_process_bank_operations_test(transactions_all: list[dict]) -> None:
    result = process_bank_operations(transactions_all, [
        'Перевод на счет', 'Перевод организации', 'Перевод со счета на счет'
    ])
    assert result == {'Перевод организации': 2, 'Перевод со счета на счет': 2}


def test_process_bank_operations_no_categories(transactions_all: list[dict]) -> None:
    with pytest.raises(TypeError):
        process_bank_operations(transactions_all, [])
