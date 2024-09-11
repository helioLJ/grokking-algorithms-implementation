def partition(arr: list[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_recursive(arr: list[int], low: int, high: int) -> None:
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_recursive(arr, low, pi - 1)
        quick_sort_recursive(arr, pi + 1, high)


def quick_sort(arr: list[int]) -> list[int]:
    """
    Sorts the input list using the Quick Sort algorithm.

    Args:
    arr (list[int]): The list to be sorted.

    Returns:
    list[int]: The sorted list.
    """
    if len(arr) <= 1:
        return arr

    quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr
