import unittest
from src.chapter11.tree.splay_tree import SplayTree


class TestSplayTree(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = SplayTree()

    def test_insert_and_search(self) -> None:
        self.tree.insert(5, "five")
        self.tree.insert(3, "three")
        self.tree.insert(7, "seven")

        self.assertEqual(self.tree.search(5), "five")
        self.assertEqual(self.tree.search(3), "three")
        self.assertEqual(self.tree.search(7), "seven")
        self.assertIsNone(self.tree.search(1))

    def test_delete(self) -> None:
        self.tree.insert(5, "five")
        self.tree.insert(3, "three")
        self.tree.insert(7, "seven")

        self.assertTrue(self.tree.delete(3))
        self.assertIsNone(self.tree.search(3))
        self.assertFalse(self.tree.delete(10))

    def test_splay_after_search(self) -> None:
        self.tree.insert(5, "five")
        self.tree.insert(3, "three")
        self.tree.insert(7, "seven")

        self.tree.search(3)
        self.assertIsNotNone(self.tree.root)
        assert self.tree.root is not None
        self.assertEqual(self.tree.root.key, 3)

    def test_splay_after_insert(self) -> None:
        self.tree.insert(5, "five")
        self.tree.insert(3, "three")
        self.tree.insert(7, "seven")
        assert self.tree.root is not None
        self.assertEqual(self.tree.root.key, 7)

    def test_splay_after_delete(self) -> None:
        self.tree.insert(5, "five")
        self.tree.insert(3, "three")
        self.tree.insert(7, "seven")

        self.tree.delete(3)
        assert self.tree.root is not None
        self.assertEqual(self.tree.root.key, 5)

    def test_empty_tree(self) -> None:
        self.assertIsNone(self.tree.search(1))
        self.assertFalse(self.tree.delete(1))


if __name__ == "__main__":
    unittest.main()
