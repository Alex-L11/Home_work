import json
from unittest.mock import MagicMock, mock_open, patch

from src.utils import get_list_transactions, get_transaction


def test_get_list_transactions() -> None:
    mock_transactions = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        },
    ]
    json_str = json.dumps(mock_transactions)
    with patch("builtins.open", mock_open(read_data=json_str)) as m_open:
        result = get_list_transactions("mock/path")
        assert result == mock_transactions
        m_open.assert_called_once()


def test_get_list_transactions_empty_file() -> None:
    json_str = json.dumps([])
    with patch("builtins.open", mock_open(read_data=json_str)) as m_open:
        result = get_list_transactions(("mock"))
        assert result == []
        m_open.assert_called_once()


def test_get_list_transactions_file_not_found() -> None:
    with patch("builtins.open", side_effect=FileNotFoundError("Файд не найден")):
        result = get_list_transactions(("mock"))
        assert result == []


def test_get_list_transactions_not_a_list() -> None:
    json_str = json.dumps({})
    with patch("builtins.open", mock_open(read_data=json_str)):
        result = get_list_transactions(("mock"))
        assert result == []


@patch("src.utils.json.load")
def test_get_list_transactions_no_json_format(mock_load: MagicMock, capsys: int) -> None:
    mock_load.side_effect = json.JSONDecodeError("Ошибка декодирования файла", "", 0)
    result = get_list_transactions("mock")
    assert result == []


def test_get_transactions(dict_transaction: dict) -> None:
    assert get_transaction(dict_transaction) == 31957.58


def test_get_transactions_usd(dict_transaction_usd: dict) -> None:
    fix_rate = 80.25
    expected_amount = float(dict_transaction_usd["operationAmount"]["amount"]) * fix_rate

    with patch("src.utils.currency_converter", return_value=expected_amount):
        result = get_transaction(dict_transaction_usd)
        assert result == 2564595.795


def test_get_transactions_none() -> None:
    assert get_transaction({}) == 0.0


def test_get_transactions_amount_str(dict_trans_1: dict) -> None:
    assert get_transaction(dict_trans_1) == 0.0
