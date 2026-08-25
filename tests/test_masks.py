from src.masks import get_mask_card_number
import pytest

def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'

    with pytest.raises(TypeError):
        get_mask_card_number('7000792289606361233')

    with pytest.raises(TypeError):
        get_mask_card_number(122334444556667)



