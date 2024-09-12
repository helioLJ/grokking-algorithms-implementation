from typing import Any


class Graph:
    """
    A class representing an undirected graph.
    """

    def __init__(self) -> None:
        """
        Initialize an empty graph.
        """
        self.graph: dict[Any, list[Any]] = {}

    def add_vertex(self, vertex: Any) -> None:
        """
        Add a vertex to the graph.

        Args:
            vertex: The vertex to be added.
        """
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1: Any, vertex2: Any) -> None:
        """
        Add an edge between two vertices in the graph.

        Args:
            vertex1: The first vertex of the edge.
            vertex2: The second vertex of the edge.
        """
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def remove_edge(self, vertex1: Any, vertex2: Any) -> None:
        """
        Remove an edge between two vertices in the graph.

        Args:
            vertex1: The first vertex of the edge.
            vertex2: The second vertex of the edge.
        """
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1] = [v for v in self.graph[vertex1] if v != vertex2]
            self.graph[vertex2] = [v for v in self.graph[vertex2] if v != vertex1]

    def get_vertices(self) -> list[Any]:
        """
        Get all vertices in the graph.

        Returns:
            A list of all vertices in the graph.
        """
        return list(self.graph.keys())

    def get_edges(self) -> list[set[Any]]:
        """
        Get all edges in the graph.

        Returns:
            A list of sets, where each set contains two vertices representing an edge.
        """
        edges = []
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                if {vertex, neighbor} not in edges:
                    edges.append({vertex, neighbor})
        return edges
