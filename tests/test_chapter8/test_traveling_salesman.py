import pytest
from src.chapter8.traveling_salesman import traveling_salesman
from typing import List


def test_traveling_salesman_small_case() -> None:
    distances = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    expected_route: List[int] = [0, 1, 3, 2, 0]
    expected_distance = 80

    result_route, result_distance = traveling_salesman(distances)
    assert result_route == expected_route
    assert result_distance == expected_distance


def test_traveling_salesman_symmetric() -> None:
    distances = [[0, 10, 15], [10, 0, 20], [15, 20, 0]]
    expected_route: List[int] = [0, 1, 2, 0]
    expected_distance = 45

    result_route, result_distance = traveling_salesman(distances)
    assert result_route == expected_route
    assert result_distance == expected_distance


def test_traveling_salesman_asymmetric() -> None:
    distances = [[0, 10, 15], [5, 0, 20], [15, 10, 0]]
    expected_route: List[int] = [0, 2, 1, 0]
    expected_distance = 30

    result_route, result_distance = traveling_salesman(distances)
    assert result_route == expected_route
    assert result_distance == expected_distance


def test_traveling_salesman_single_city() -> None:
    distances = [[0]]
    expected_route: List[int] = [0, 0]
    expected_distance = 0

    result_route, result_distance = traveling_salesman(distances)
    assert result_route == expected_route
    assert result_distance == expected_distance


def test_traveling_salesman_invalid_input() -> None:
    with pytest.raises(ValueError):
        traveling_salesman([])

    with pytest.raises(ValueError):
        traveling_salesman([[0], [0]])
