from typing import List


def knapsack(capacity: int, weights: List[int], values: List[int]) -> int:
    """
    Solve the 0/1 Knapsack problem using dynamic programming.

    Args:
        capacity (int): The maximum weight capacity of the knapsack.
        weights (List[int]): A list of weights for each item.
        values (List[int]): A list of values for each item.

    Returns:
        int: The maximum value that can be achieved without exceeding the capacity.

    Raises:
        ValueError: If capacity is negative, if weights and values have different lengths,
                    or if any weight or value is negative.
    """
    if capacity < 0:
        raise ValueError("Capacity must be non-negative")
    if len(weights) != len(values):
        raise ValueError("Weights and values must have the same length")
    if any(w < 0 for w in weights):
        raise ValueError("All weights must be non-negative")
    if any(v < 0 for v in values):
        raise ValueError("All values must be non-negative")

    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]


def get_selected_items(
    capacity: int, weights: List[int], values: List[int]
) -> List[int]:
    """
    Get the indices of items selected in the optimal solution of the 0/1 Knapsack problem.

    Args:
        capacity (int): The maximum weight capacity of the knapsack.
        weights (List[int]): A list of weights for each item.
        values (List[int]): A list of values for each item.

    Returns:
        List[int]: A list of indices of the selected items.

    Raises:
        ValueError: If capacity is negative, if weights and values have different lengths,
                    or if any weight or value is negative.
    """
    if capacity < 0:
        raise ValueError("Capacity must be non-negative")
    if len(weights) != len(values):
        raise ValueError("Weights and values must have the same length")
    if any(w < 0 for w in weights):
        raise ValueError("All weights must be non-negative")
    if any(v < 0 for v in values):
        raise ValueError("All values must be non-negative")

    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            w -= weights[i - 1]
        i -= 1

    return selected_items[::-1]
