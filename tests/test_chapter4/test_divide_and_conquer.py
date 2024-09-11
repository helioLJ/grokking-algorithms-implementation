import pytest
from src.chapter4.divide_and_conquer import (
    recursive_sum,
    recursive_count,
    recursive_max,
    recursive_binary_search,
)


def test_recursive_sum() -> None:
    assert recursive_sum([]) == 0
    assert recursive_sum([1, 2, 3, 4, 5]) == 15
    assert recursive_sum([-1, 0, 1]) == 0


def test_recursive_count() -> None:
    assert recursive_count([]) == 0
    assert recursive_count([1, 2, 3, 4, 5]) == 5
    assert recursive_count([0]) == 1


def test_recursive_max() -> None:
    with pytest.raises(ValueError):
        recursive_max([])
    assert recursive_max([1]) == 1
    assert recursive_max([1, 3, 2, 5, 4]) == 5
    assert recursive_max([-1, -5, -2]) == -1


def test_recursive_binary_search() -> None:
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
    assert recursive_binary_search(sorted_list, 7) == 3
    assert recursive_binary_search(sorted_list, 1) == 0
    assert recursive_binary_search(sorted_list, 15) == 7
    assert recursive_binary_search(sorted_list, 0) == -1
    assert recursive_binary_search(sorted_list, 16) == -1
    assert recursive_binary_search([], 5) == -1
