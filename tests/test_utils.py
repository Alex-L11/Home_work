import json
from unittest.mock import patch, mock_open
from src.utils import get_list_transactions

def test_get_list_transactions():
    mock_transactions = [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    }
  }
]
    json_str = json.dumps(mock_transactions)
    with patch("builtins.open", mock_open(read_data=json_str)) as m_open:
        result = get_list_transactions("mock/path")
        assert result == mock_transactions
        m_open.assert_called_once()


def test_get_list_transactions_empty_file():
    json_str = json.dumps([])
    with patch("builtins.open", mock_open(read_data=json_str)) as m_open:
        result = get_list_transactions(("mock/path"))
        assert result == []
        m_open.assert_called_once()