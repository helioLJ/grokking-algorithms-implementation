import unittest
from src.chapter6.graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = Graph()

    def test_add_vertex(self) -> None:
        self.graph.add_vertex("A")
        self.assertIn("A", self.graph.get_vertices())

    def test_add_edge(self) -> None:
        self.graph.add_edge("A", "B")
        self.assertIn("B", self.graph.graph["A"])
        self.assertIn("A", self.graph.graph["B"])

    def test_remove_edge(self) -> None:
        self.graph.add_edge("A", "B")
        self.graph.remove_edge("A", "B")
        self.assertNotIn("B", self.graph.graph["A"])
        self.assertNotIn("A", self.graph.graph["B"])

    def test_get_vertices(self) -> None:
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.assertEqual(set(self.graph.get_vertices()), {"A", "B"})

    def test_get_edges(self) -> None:
        self.graph.add_edge("A", "B")
        self.graph.add_edge("B", "C")
        expected_edges = [{"A", "B"}, {"B", "C"}]
        self.assertEqual(self.graph.get_edges(), expected_edges)


if __name__ == "__main__":
    unittest.main()
