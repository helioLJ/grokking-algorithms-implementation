def key_search_recursive(arr: list[int], key: int) -> int:
    """
    Perform a recursive key search on a sorted list.

    Args:
    arr (list): A sorted list of integers
    key (int): The key to search for

    Returns:
    int: The index of the key if found, -1 otherwise
    """
    return _key_search_recursive_helper(arr, key, 0, len(arr) - 1)


def _key_search_recursive_helper(arr: list[int], key: int, low: int, high: int) -> int:
    """
    Helper function for the recursive key search algorithm.

    Args:
    arr (list): A sorted list of integers
    key (int): The key to search for
    low (int): The lower bound of the search range
    high (int): The upper bound of the search range

    Returns:
    int: The index of the key if found, -1 otherwise
    """
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return _key_search_recursive_helper(arr, key, mid + 1, high)
    else:
        return _key_search_recursive_helper(arr, key, low, mid - 1)
