import unittest
from src.chapter11.tree.b_tree import BTree


class TestBTree(unittest.TestCase):
    def setUp(self) -> None:
        self.b_tree = BTree(t=3)

    def test_insert_and_search(self) -> None:
        keys = [10, 20, 5, 6, 12, 30, 7, 17]
        for key in keys:
            self.b_tree.insert(key)

        for key in keys:
            self.assertIsNotNone(self.b_tree.search(key))

        self.assertIsNone(self.b_tree.search(100))

    def test_string_representation(self) -> None:
        keys = [10, 20, 5, 6, 12, 30, 7, 17]
        for key in keys:
            self.b_tree.insert(key)

        expected_output = (
            "10\n" "  5\n" "  6\n" "  7\n" "  12\n" "  17\n" "  20\n" "  30\n"
        )
        self.assertEqual(str(self.b_tree), expected_output)

    def test_empty_tree(self) -> None:
        self.assertIsNone(self.b_tree.search(10))
        self.assertEqual(str(self.b_tree), "")

    def test_single_node_tree(self) -> None:
        self.b_tree.insert(10)
        self.assertIsNotNone(self.b_tree.search(10))
        self.assertEqual(str(self.b_tree), "10\n")

    def test_multiple_splits(self) -> None:
        keys = list(range(1, 21))
        for key in keys:
            self.b_tree.insert(key)

        for key in keys:
            self.assertIsNotNone(self.b_tree.search(key))

    def test_duplicate_keys(self) -> None:
        keys = [10, 20, 5, 6, 12, 30, 7, 17, 10, 20]
        for key in keys:
            self.b_tree.insert(key)

        node_10 = self.b_tree.search(10)
        node_20 = self.b_tree.search(20)
        self.assertIsNotNone(node_10)
        self.assertIsNotNone(node_20)
        assert node_10 is not None
        assert node_20 is not None
        self.assertEqual(node_10.keys.count(10), 1)  # Updated to expect 1 occurrence
        self.assertEqual(node_20.keys.count(20), 1)  # Updated to expect 1 occurrence


if __name__ == "__main__":
    unittest.main()
