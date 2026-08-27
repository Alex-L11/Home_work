from src.masks import get_mask_card_number, get_mask_account
import pytest
from typing import Any

def test_get_mask_card_number() -> Any:
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'

    with pytest.raises(TypeError):
        get_mask_card_number('7000792289606361233')

    with pytest.raises(TypeError):
        get_mask_card_number('2334567676')

    with pytest.raises(TypeError):
        get_mask_card_number('')

    with pytest.raises(TypeError):
        get_mask_card_number('qwerrtyty')


def test_get_mask_account() -> None:
    assert get_mask_account(73654108430135874305) == '** 4305'

    with pytest.raises(TypeError):
        get_mask_account(3445666778778)

    with pytest.raises(TypeError):
        get_mask_account(324376677345676788888454654)

    with pytest.raises(TypeError):
        get_mask_account('asd')
