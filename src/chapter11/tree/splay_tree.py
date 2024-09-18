from typing import Optional, Any


class Node:
    def __init__(self, key: Any, value: Any):
        self.key = key
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class SplayTree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def insert(self, key: Any, value: Any) -> None:
        """
        Insert a key-value pair into the Splay Tree.

        :param key: The key to insert
        :param value: The value associated with the key
        """
        if not self.root:
            self.root = Node(key, value)
            return

        self._splay(key)
        if self.root.key == key:
            self.root.value = value
        elif key < self.root.key:
            new_node = Node(key, value)
            new_node.left = self.root.left
            new_node.right = self.root
            self.root.left = None
            self.root = new_node
        else:
            new_node = Node(key, value)
            new_node.right = self.root.right
            new_node.left = self.root
            self.root.right = None
            self.root = new_node

    def search(self, key: Any) -> Optional[Any]:
        """
        Search for a key in the Splay Tree and return its value.

        :param key: The key to search for
        :return: The value associated with the key, or None if not found
        """
        if not self.root:
            return None

        self._splay(key)
        return self.root.value if self.root.key == key else None

    def delete(self, key: Any) -> bool:
        """
        Delete a key-value pair from the Splay Tree.

        :param key: The key to delete
        :return: True if the key was found and deleted, False otherwise
        """
        if not self.root:
            return False

        self._splay(key)
        if self.root.key != key:
            return False

        if not self.root.left:
            self.root = self.root.right
        else:
            new_root = self.root.right
            self.root = self.root.left
            self._splay(key)
            self.root.right = new_root

        return True

    def _splay(self, key: Any) -> None:
        """
        Perform the splay operation to bring the node with the given key to the root.

        :param key: The key to splay
        """
        if not self.root:
            return

        header = Node(None, None)
        left = right = header

        while True:
            if key < self.root.key:
                if not self.root.left:
                    break
                if key < self.root.left.key:
                    self._rotate_right()
                    if not self.root.left:
                        break
                right.left = self.root
                right = right.left
                self.root = self.root.left
            elif key > self.root.key:
                if not self.root.right:
                    break
                if key > self.root.right.key:
                    self._rotate_left()
                    if not self.root.right:
                        break
                left.right = self.root
                left = left.right
                self.root = self.root.right
            else:
                break

        left.right = self.root.left
        right.left = self.root.right
        self.root.left = header.right
        self.root.right = header.left

    def _rotate_left(self) -> None:
        """Perform a left rotation."""
        old_root = self.root
        assert self.root is not None
        self.root = self.root.right
        assert self.root is not None
        assert old_root is not None
        old_root.right = self.root.left
        self.root.left = old_root

    def _rotate_right(self) -> None:
        """Perform a right rotation."""
        old_root = self.root
        assert self.root is not None
        self.root = self.root.left
        assert self.root is not None
        assert old_root is not None
        old_root.left = self.root.right
        self.root.right = old_root
