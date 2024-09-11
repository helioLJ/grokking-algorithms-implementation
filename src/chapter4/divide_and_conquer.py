from typing import Optional


def recursive_sum(lst: list[int]) -> int:
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])


def recursive_count(lst: list[int]) -> int:
    if not lst:
        return 0
    return 1 + recursive_count(lst[1:])


def recursive_max(lst: list[int]) -> int:
    if not lst:
        raise ValueError("Cannot find maximum of an empty list")
    if len(lst) == 1:
        return lst[0]
    sub_max = recursive_max(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max


def recursive_binary_search(
    lst: list[int], target: int, low: int = 0, high: Optional[int] = None
) -> int:
    if high is None:
        high = len(lst) - 1

    if low > high:
        return -1  # Target not found

    mid = (low + high) // 2

    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return recursive_binary_search(lst, target, low, mid - 1)
    else:
        return recursive_binary_search(lst, target, mid + 1, high)
