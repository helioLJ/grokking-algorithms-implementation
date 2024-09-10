def binary_search(sorted_list: list[int], target: int) -> int:
    """
    Perform binary search on a sorted list to find the target value.

    Args:
        sorted_list (list[int]): A sorted list of integers.
        target (int): The value to search for.

    Returns:
        int: The index of the target value if found, or -1 if not found.
    """
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
