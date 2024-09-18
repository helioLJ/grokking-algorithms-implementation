import unittest
from src.chapter11.tree.red_black_tree import RedBlackTree, Color, Node


class TestRedBlackTree(unittest.TestCase):
    def setUp(self) -> None:
        self.rbt = RedBlackTree()

    def test_insert_and_search(self) -> None:
        keys = [7, 3, 18, 10, 22, 8, 11, 26]
        for key in keys:
            self.rbt.insert(key)

        for key in keys:
            node = self.rbt.search(key)
            self.assertIsNotNone(node)
            assert node is not None
            self.assertEqual(node.key, key)

        non_existent = self.rbt.search(100)
        self.assertIsNone(non_existent)

    def test_inorder_traversal(self) -> None:
        keys = [7, 3, 18, 10, 22, 8, 11, 26]
        for key in keys:
            self.rbt.insert(key)

        inorder = self.rbt.inorder_traversal()
        self.assertEqual(inorder, sorted(keys))

    def test_root_is_black(self) -> None:
        keys = [7, 3, 18, 10, 22, 8, 11, 26]
        for key in keys:
            self.rbt.insert(key)

        self.assertEqual(self.rbt.root.color, Color.BLACK)

    def test_red_node_children_are_black(self) -> None:
        keys = [7, 3, 18, 10, 22, 8, 11, 26]
        for key in keys:
            self.rbt.insert(key)

        def check_red_children(node: Node) -> bool:
            if node == self.rbt.NIL:
                return True
            if node.color == Color.RED:
                if node.left != self.rbt.NIL:
                    self.assertEqual(node.left.color, Color.BLACK)
                if node.right != self.rbt.NIL:
                    self.assertEqual(node.right.color, Color.BLACK)
            return check_red_children(node.left) and check_red_children(node.right)

        self.assertTrue(check_red_children(self.rbt.root))

    def test_black_height(self) -> None:
        keys = [7, 3, 18, 10, 22, 8, 11, 26]
        for key in keys:
            self.rbt.insert(key)

        def black_height(node: Node) -> int:
            if node == self.rbt.NIL:
                return 1
            left_height = black_height(node.left)
            right_height = black_height(node.right)
            self.assertEqual(left_height, right_height)
            return left_height + (1 if node.color == Color.BLACK else 0)

        black_height(self.rbt.root)


if __name__ == "__main__":
    unittest.main()
