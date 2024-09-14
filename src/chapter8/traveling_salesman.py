import itertools
from typing import List, Tuple


def traveling_salesman(distances: List[List[int]]) -> Tuple[List[int], int]:
    """
    Solve the Traveling Salesman Problem using a brute-force approach.

    :param distances: A 2D list representing the distance matrix between cities
    :return: A tuple containing the shortest route and its total distance
    :raises ValueError: If the input is invalid (empty or non-square matrix)
    """
    if not distances or not all(len(row) == len(distances) for row in distances):
        raise ValueError("Invalid input: distances must be a non-empty square matrix")

    num_cities = len(distances)
    cities = list(range(num_cities))
    shortest_route: List[int] = []
    shortest_distance = float("inf")

    for route in itertools.permutations(cities[1:]):
        current_route = [0] + list(route) + [0]
        distance = sum(
            distances[current_route[i]][current_route[i + 1]] for i in range(num_cities)
        )

        if distance < shortest_distance:
            shortest_distance = distance
            shortest_route = current_route

    return shortest_route, int(shortest_distance)
