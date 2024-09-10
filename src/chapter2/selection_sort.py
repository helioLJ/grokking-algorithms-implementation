def selection_sort(arr: list[int]) -> list[int]:
    """
    Implement the selection sort algorithm.

    Args:
    arr (list): The input list to be sorted.

    Returns:
    list: The sorted list.
    """
    new_arr = []
    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


def find_smallest(arr: list[int]) -> int:
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
