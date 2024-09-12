import unittest
from src.chapter6.graph import Graph
from src.chapter6.bfs import bfs, find_path


class TestBFS(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = Graph()
        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")
        self.graph.add_edge("B", "D")
        self.graph.add_edge("C", "D")
        self.graph.add_edge("D", "E")

    def test_bfs(self) -> None:
        result = bfs(self.graph, "A")
        self.assertEqual(result, ["A", "B", "C", "D", "E"])

    def test_bfs_disconnected(self) -> None:
        self.graph.add_vertex("F")
        result = bfs(self.graph, "A")
        self.assertEqual(result, ["A", "B", "C", "D", "E"])
        self.assertNotIn("F", result)

    def test_find_path_existing(self) -> None:
        path = find_path(self.graph, "A", "E")
        self.assertIn(path, [["A", "B", "D", "E"], ["A", "C", "D", "E"]])

    def test_find_path_non_existing(self) -> None:
        self.graph.add_vertex("F")
        path = find_path(self.graph, "A", "F")
        self.assertIsNone(path)

    def test_find_path_same_vertex(self) -> None:
        path = find_path(self.graph, "A", "A")
        self.assertEqual(path, ["A"])


if __name__ == "__main__":
    unittest.main()
