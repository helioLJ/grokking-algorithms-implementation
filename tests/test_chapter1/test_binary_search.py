import pytest
from src.chapter1.binary_search import binary_search


@pytest.mark.parametrize(
    "sorted_list, target, expected",
    [
        ([1, 3, 5, 7, 9], 3, 1),
        ([1, 3, 5, 7, 9], 9, 4),
        ([1, 3, 5, 7, 9], 1, 0),
        ([1, 3, 5, 7, 9], 6, -1),
        ([], 1, -1),
        ([1], 1, 0),
        ([1], 2, -1),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 0, -1),
        ([1, 2, 3, 4, 5], 6, -1),
        ([1, 1, 2, 2, 3, 3], 2, 2),
        ([1, 3, 5, 7, 9, 11], 10, -1),
    ],
)
def test_binary_search(sorted_list: list[int], target: int, expected: int) -> None:
    assert binary_search(sorted_list, target) == expected


def test_binary_search_large_list() -> None:
    large_list = list(range(0, 10000, 2))
    assert binary_search(large_list, 5000) == 2500
    assert binary_search(large_list, 9998) == 4999
    assert binary_search(large_list, 9999) == -1
    assert binary_search(large_list, 0) == 0
    assert binary_search(large_list, 9996) == 4998
    assert binary_search(large_list, -2) == -1
    assert binary_search(large_list, 10000) == -1
