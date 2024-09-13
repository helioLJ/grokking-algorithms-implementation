import heapq
from typing import Dict, List, Tuple, Optional


def dijkstra(graph: Dict[str, Dict[str, int]], start: str) -> Dict[str, int]:
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
