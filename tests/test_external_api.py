import os
from unittest.mock import patch

import pytest

from src.external_api import currency_converter


def test_currency_converter_no_api_key() -> None:
    # проверка на отсутсвие ключа
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError, match="Переменная окружения API_KEY не задана"):
            currency_converter("USD", 100.0)


def test_currency_converter_success() -> None:
    # проверка на вывод актуальных данных
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"result": 90.5}

        with patch.dict("os.environ", {"API_KEY": "test_key"}, clear=True):
            result = currency_converter("EUR", 5.5)

        assert result == 90.5
