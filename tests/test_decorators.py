import os
from pathlib import Path
from typing import Any

import pytest

from src.decorators import log


def test_log(capsys: Any) -> None:
    @log()
    def wrap(x: int, y: int) -> int:
        return x + y

    result = wrap(2, 4)
    assert result == 6

    out, err = capsys.readouterr()
    assert "wrap ok" in err
    assert out == ""


def test_log_file() -> None:
    log_file = "mylog.txt"
    if os.path.exists(log_file):
        os.remove(log_file)

    @log(filename=log_file)
    def wrap(x: int, y: int) -> int:
        return x + y

    result = wrap(2, 5)
    assert result == 7

    # проверяем что файл создан
    assert Path(log_file).exists()

    # читаем файл и проверяем содержимое
    content = Path(log_file).read_text()
    assert "wrap ok" in content

    with pytest.raises(TypeError):
        wrap(1, "1")  # type: ignore[arg-type]
