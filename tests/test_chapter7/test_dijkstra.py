import pytest
from src.chapter7.dijkstra import dijkstra, shortest_path


@pytest.fixture
def sample_graph() -> dict[str, dict[str, int]]:
    return {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 1, "D": 5},
        "C": {"A": 2, "B": 1, "D": 8, "E": 10},
        "D": {"B": 5, "C": 8, "E": 2, "F": 6},
        "E": {"C": 10, "D": 2, "F": 3},
        "F": {"D": 6, "E": 3},
    }


def test_dijkstra(sample_graph: dict[str, dict[str, int]]) -> None:
    distances = dijkstra(sample_graph, "A")
    assert distances == {"A": 0, "B": 3, "C": 2, "D": 8, "E": 10, "F": 13}


def test_dijkstra_unreachable_node(sample_graph: dict[str, dict[str, int]]) -> None:
    graph = {"A": {"B": 1}, "B": {"A": 1}, "C": {}}
    distances = dijkstra(graph, "A")
    assert distances == {"A": 0, "B": 1, "C": float("infinity")}


def test_shortest_path(sample_graph: dict[str, dict[str, int]]) -> None:
    path, distance = shortest_path(sample_graph, "A", "F")
    assert path == ["A", "C", "B", "D", "E", "F"]
    assert distance == 13


def test_shortest_path_unreachable(sample_graph: dict[str, dict[str, int]]) -> None:
    graph = {"A": {"B": 1}, "B": {"A": 1}, "C": {}}
    path, distance = shortest_path(graph, "A", "C")
    assert path == []
    assert distance == float("infinity")


def test_shortest_path_same_node(sample_graph: dict[str, dict[str, int]]) -> None:
    path, distance = shortest_path(sample_graph, "A", "A")
    assert path == ["A"]
    assert distance == 0
