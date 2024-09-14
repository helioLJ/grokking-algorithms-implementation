import heapq
from typing import Dict, List, Tuple, Optional


def dijkstra(graph: Dict[str, Dict[str, int]], start: str) -> Dict[str, int]:
    """
    Implements Dijkstra's algorithm to find the shortest path from a start node to all other nodes in a weighted graph.

    Args:
    graph (Dict[str, Dict[str, int]]): A dictionary representing the graph. Each key is a node, and its value is another dictionary
                                       where keys are neighboring nodes and values are the weights of the edges.
    start (str): The starting node.

    Returns:
    Dict[str, int]: A dictionary where keys are nodes and values are the shortest distances from the start node.
    """
    distances: Dict[str, int] = {node: float("infinity") for node in graph}  # type: ignore
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


def shortest_path(
    graph: Dict[str, Dict[str, int]], start: str, end: str
) -> Tuple[List[str], int]:
    """
    Finds the shortest path between two nodes in a weighted graph using Dijkstra's algorithm.

    Args:
    graph (Dict[str, Dict[str, int]]): A dictionary representing the graph. Each key is a node, and its value is another dictionary
                                       where keys are neighboring nodes and values are the weights of the edges.
    start (str): The starting node.
    end (str): The destination node.

    Returns:
    Tuple[List[str], int]: A tuple containing the list of nodes in the shortest path and the total distance.
                           If no path is found, returns an empty list and infinity.
    """
    distances: Dict[str, int] = {node: float("infinity") for node in graph}  # type: ignore
    distances[start] = 0
    predecessors: Dict[str, Optional[str]] = {node: None for node in graph}
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == end:
            path = []
            current: Optional[str] = current_node
            while current:
                path.append(current)
                current = predecessors[current]
            return list(reversed(path)), current_distance

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return [], float("infinity")  # type: ignore
