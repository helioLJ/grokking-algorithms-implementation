import pytest
from typing import List
from src.chapter9.knapsack_problem import knapsack, get_selected_items


@pytest.mark.parametrize(
    "capacity, weights, values, expected_value, expected_items",
    [
        (50, [10, 20, 30], [60, 100, 120], 220, [2, 3]),
        (10, [5, 4, 6, 3], [10, 40, 30, 50], 90, [2, 4]),
        (6, [1, 2, 3, 5], [1, 6, 10, 16], 17, [1, 2, 3]),
        (0, [1, 2, 3], [10, 20, 30], 0, []),
        (100, [], [], 0, []),
    ],
)
def test_knapsack_and_selected_items(
    capacity: int,
    weights: List[int],
    values: List[int],
    expected_value: int,
    expected_items: List[int],
) -> None:
    """
    Test both knapsack and get_selected_items functions with various inputs.
    """
    assert knapsack(capacity, weights, values) == expected_value
    assert get_selected_items(capacity, weights, values) == expected_items


def test_knapsack_large_input() -> None:
    """
    Test knapsack function with a larger input to ensure it can handle more complex cases.
    """
    capacity = 100
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 10
    values = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30] * 10
    assert knapsack(capacity, weights, values) == 300


def test_get_selected_items_large_input() -> None:
    """
    Test get_selected_items function with a larger input to ensure it can handle more complex cases.
    """
    capacity = 50
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 5
    values = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30] * 5
    selected_items = get_selected_items(capacity, weights, values)
    assert len(selected_items) > 0
    assert sum(weights[i - 1] for i in selected_items) <= capacity


def test_invalid_inputs() -> None:
    """
    Test both functions with invalid inputs to ensure they raise appropriate exceptions.
    """
    with pytest.raises(ValueError):
        knapsack(-1, [1, 2, 3], [10, 20, 30])

    with pytest.raises(ValueError):
        get_selected_items(10, [1, 2, 3], [10, 20])

    with pytest.raises(ValueError):
        knapsack(10, [-1, 2, 3], [10, 20, 30])

    with pytest.raises(ValueError):
        get_selected_items(10, [1, 2, 3], [-10, 20, 30])
