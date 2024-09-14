from typing import List, Tuple, Dict, Set


def classroom_scheduling(classes: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Schedule classes to maximize the number of non-overlapping classes.

    Args:
    classes (List[Tuple[int, int]]): List of classes, each represented by (start_time, end_time).

    Returns:
    List[Tuple[int, int]]: List of scheduled classes.
    """
    sorted_classes = sorted(classes, key=lambda x: x[1])
    schedule = [sorted_classes[0]]
    for c in sorted_classes[1:]:
        if c[0] >= schedule[-1][1]:
            schedule.append(c)
    return schedule


def knapsack(
    items: List[Tuple[str, int, int]], capacity: int
) -> List[Tuple[str, int, int]]:
    """
    Solve the 0-1 knapsack problem to maximize value within a given capacity.

    Args:
    items (List[Tuple[str, int, int]]): List of items, each represented by (name, weight, value).
    capacity (int): Maximum weight capacity of the knapsack.

    Returns:
    List[Tuple[str, int, int]]: List of items to include in the knapsack.
    """
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, weight, value = items[i - 1]
        for w in range(capacity + 1):
            if weight > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

    res = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            res.append(items[i - 1])
            w -= items[i - 1][1]

    res.reverse()
    return res


def truck_loading(boxes: List[int], truck_capacity: int) -> List[int]:
    """
    Load boxes into a truck to maximize the weight carried within the truck's capacity.

    Args:
    boxes (List[int]): List of box weights.
    truck_capacity (int): Maximum weight capacity of the truck.

    Returns:
    List[int]: List of box weights loaded into the truck.
    """
    sorted_boxes = sorted(boxes, reverse=True)
    loaded_boxes = []
    current_load = 0
    for box in sorted_boxes:
        if current_load + box <= truck_capacity:
            loaded_boxes.append(box)
            current_load += box
    return loaded_boxes


def europe_trip(
    places: List[Tuple[str, int, int]], days: int
) -> List[Tuple[str, int, int]]:
    """
    Plan a Europe trip to maximize enjoyment within a given number of days.

    Args:
    places (List[Tuple[str, int, int]]): List of places, each represented by (name, enjoyment, days_required).
    days (int): Total number of days available for the trip.

    Returns:
    List[Tuple[str, int, int]]: List of places to visit during the trip.
    """
    # Add index to maintain original order
    indexed_places = list(enumerate(places))
    sorted_places = sorted(
        indexed_places, key=lambda x: (-x[1][1] / x[1][2], -x[1][1], x[0])
    )
    itinerary = []
    total_days = 0
    for _, place in sorted_places:
        if total_days + place[2] <= days:
            itinerary.append(place)
            total_days += place[2]
    return itinerary


def set_cover(states: Set[str], stations: Dict[str, Set[str]]) -> Set[str]:
    """
    Find the minimum set of radio stations to cover all states.

    Args:
    states (Set[str]): Set of all states to be covered.
    stations (Dict[str, Set[str]]): Dictionary of radio stations and the states they cover.

    Returns:
    Set[str]: Set of selected radio stations that cover all states.
    """
    uncovered = set(states)
    selected_stations = set()

    while uncovered:
        best_station = max(stations, key=lambda s: len(uncovered & stations[s]))
        selected_stations.add(best_station)
        uncovered -= stations[best_station]

    return selected_stations
