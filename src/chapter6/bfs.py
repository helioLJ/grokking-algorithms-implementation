from collections import deque
from typing import Any, Optional
from src.chapter6.graph import Graph


def bfs(graph: Graph, start: Any) -> list[Any]:
    """
    Perform a Breadth-First Search on the given graph.

    Args:
        graph: The Graph object to search.
        start: The starting vertex for the search.

    Returns:
        A list of vertices in the order they were visited.
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph.graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def find_path(graph: Graph, start: Any, end: Any) -> Optional[list[Any]]:
    """
    Find a path between start and end vertices using BFS.

    Args:
        graph: The Graph object to search.
        start: The starting vertex.
        end: The target vertex.

    Returns:
        A list representing the path from start to end, or None if no path exists.
    """
    visited = set()
    queue = deque([(start, [start])])
    visited.add(start)

    while queue:
        (vertex, path) = queue.popleft()
        if vertex == end:
            return path

        for neighbor in graph.graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None
