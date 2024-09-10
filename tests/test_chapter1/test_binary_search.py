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
    ],
)
def test_binary_search(sorted_list: list[int], target: int, expected: int) -> None:
    assert binary_search(sorted_list, target) == expected


def test_binary_search_large_list() -> None:
    large_list = list(range(0, 10000, 2))  # Even numbers from 0 to 9998
    assert binary_search(large_list, 5000) == 2500
    assert binary_search(large_list, 9998) == 4999
    assert binary_search(large_list, 9999) == -1
