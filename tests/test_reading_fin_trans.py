from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from src.reading_fin_trans import get_fin_oper_csv, get_fin_oper_xlsx


def test_get_fin_oper_csv_trans(trans_1: list[dict[str, Any]]) -> None:
    mock_trans = MagicMock()
    mock_trans.to_dict.return_value = trans_1
    with (
        patch("src.reading_fin_trans.pd.read_csv", return_value=mock_trans),
        patch("src.reading_fin_trans.os.path.exists", return_value=True),
    ):
        result = get_fin_oper_csv("mock_file")
        assert result == trans_1


def test_get_fin_oper_csv_trans_no_file() -> None:
    with patch("src.reading_fin_trans.os.path.exists", return_value=False):
        with pytest.raises(FileNotFoundError, match="Файл не найден"):
            get_fin_oper_csv("mock_file")


def test_get_fin_oper_xlsx_trans(trans_1: list[dict[str, Any]]) -> None:
    mock_trans = MagicMock()
    mock_trans.to_dict.return_value = trans_1
    with (
        patch("src.reading_fin_trans.pd.read_excel", return_value=mock_trans),
        patch("src.reading_fin_trans.os.path.exists", return_value=True),
    ):
        result = get_fin_oper_xlsx("mock_file")
        assert result == trans_1


def test_get_fin_oper_xlsx_trans_no_file() -> None:
    with patch("src.reading_fin_trans.os.path.exists", return_value=False):
        with pytest.raises(FileNotFoundError, match="Файл не найден"):
            get_fin_oper_xlsx("mock_file")
