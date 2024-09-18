import multiprocessing
from typing import List, Callable, Any


def parallel_map(
    func: Callable[[Any], Any], iterable: List[Any], num_processes: int | None = None
) -> List[Any]:
    """
    Apply a function to every item of an iterable in parallel.

    Args:
        func (Callable[[Any], Any]): The function to apply to each item.
        iterable (List[Any]): The input iterable.
        num_processes (int, optional): Number of processes to use. Defaults to None (uses all available cores).

    Returns:
        List[Any]: A list containing the results of applying func to each item in the iterable.
    """
    if num_processes is None:
        num_processes = multiprocessing.cpu_count()

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(func, iterable)

    return list(results)


def parallel_filter(
    func: Callable[[Any], bool], iterable: List[Any], num_processes: int | None = None
) -> List[Any]:
    """
    Filter an iterable using a predicate function in parallel.

    Args:
        func (Callable[[Any], bool]): The predicate function to apply to each item.
        iterable (List[Any]): The input iterable.
        num_processes (int, optional): Number of processes to use. Defaults to None (uses all available cores).

    Returns:
        List[Any]: A list containing the items from the iterable for which func returns True.
    """
    if num_processes is None:
        num_processes = multiprocessing.cpu_count()

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(func, iterable)

    return [item for item, keep in zip(iterable, results) if keep]
