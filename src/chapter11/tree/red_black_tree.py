from typing import Any, Optional


class Color:
    RED = 0
    BLACK = 1


class Node:
    def __init__(self, key: Any, color: int = Color.RED):
        self.key = key
        self.left: "Node"
        self.right: "Node"
        self.parent: Optional["Node"] = None
        self.color = color


class RedBlackTree:
    def __init__(self) -> None:
        self.NIL = Node(key=None, color=Color.BLACK)
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.root: Node = self.NIL

    def insert(self, key: Any) -> None:
        """
        Insert a new key into the Red-Black Tree.

        Args:
            key: The key to be inserted.
        """
        new_node = Node(key)
        new_node.left = self.NIL
        new_node.right = self.NIL

        y: Optional[Node] = None
        x: Node = self.root

        while x != self.NIL:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y is None:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node

        self._insert_fixup(new_node)

    def _insert_fixup(self, node: Node) -> None:
        """
        Fix the Red-Black Tree properties after insertion.

        Args:
            node: The newly inserted node.
        """
        while node.parent and node.parent.color == Color.RED:
            assert node.parent.parent is not None
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.color == Color.RED:
                    node.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    assert node.parent is not None
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    assert node.parent is not None
                    node.parent.color = Color.BLACK
                    assert node.parent.parent is not None
                    node.parent.parent.color = Color.RED
                    self._right_rotate(node.parent.parent)
            else:
                assert node.parent is not None and node.parent.parent is not None
                y = node.parent.parent.left
                if y.color == Color.RED:
                    node.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    assert node.parent is not None
                    if node == node.parent.left:
                        node = node.parent
                        assert node is not None
                        self._right_rotate(node)
                    assert node.parent is not None
                    node.parent.color = Color.BLACK
                    assert node.parent.parent is not None
                    node.parent.parent.color = Color.RED
                    self._left_rotate(node.parent.parent)

        self.root.color = Color.BLACK

    def _left_rotate(self, x: Node) -> None:
        """
        Perform a left rotation on the given node.

        Args:
            x: The node to rotate.
        """
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y: Node) -> None:
        """
        Perform a right rotation on the given node.

        Args:
            y: The node to rotate.
        """
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def search(self, key: Any) -> Optional[Node]:
        """
        Search for a key in the Red-Black Tree.

        Args:
            key: The key to search for.

        Returns:
            The node containing the key if found, None otherwise.
        """
        current = self.root
        while current != self.NIL:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def inorder_traversal(self) -> list[Any]:
        """
        Perform an inorder traversal of the Red-Black Tree.

        Returns:
            A list of keys in inorder traversal.
        """

        def _inorder(node: Node) -> list[Any]:
            if node == self.NIL:
                return []
            return _inorder(node.left) + [node.key] + _inorder(node.right)

        return _inorder(self.root)
