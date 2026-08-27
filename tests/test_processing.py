import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state():
    with pytest.raises(TypeError):
        filter_by_state()


def test_filter_by_state_no_state(dict_list_5):
    with pytest.raises(TypeError):
        filter_by_state(dict_list_5)


@pytest.mark.parametrize('idx', [0, 1, 2, 3])
def test_filter_by_state(dict_list_4, idx):
    item = dict_list_4[idx]
    assert 'state' in item


@pytest.mark.parametrize("state_filter, expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 1),
    ("RANDOM", 1),
])
def test_filter_by_state(dict_list_4, state_filter, expected_count):
    result = filter_by_state(dict_list_4, state=state_filter)
    assert len(result) == expected_count


def test_sort_by_date(dict_list_2, dict_list_2_a):
    assert sort_by_date(dict_list_2) == dict_list_2_a

def test_sort_by_date_reverse(dict_list_2, dict_list_2_b):
    assert sort_by_date(dict_list_2, reverse=False) == dict_list_2_b


def test_sort_by_date_empty():
    with pytest.raises(TypeError):
        sort_by_date()

    with pytest.raises(TypeError):
        sort_by_date([{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T:08:58.425572'},
                      {'id': 615064591, 'state': 'CANCELED', 'date': '2016-30T2:08:58.425572'},])


def test_sort_by_date_repeat(dict_list_date, dict_list_date_reverse):
    assert sort_by_date(dict_list_date) == dict_list_date_reverse


