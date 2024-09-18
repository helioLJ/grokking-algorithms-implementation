from typing import List, Optional, Any


class BTreeNode:
    def __init__(self, leaf: bool = False):
        self.keys: List[Any] = []
        self.children: List["BTreeNode"] = []
        self.leaf: bool = leaf


class BTree:
    def __init__(self, t: int):
        """
        Initialize an empty B-Tree.

        :param t: Minimum degree of the B-Tree
        """
        self.root: Optional[BTreeNode] = None
        self.t: int = t

    def insert(self, key: Any) -> None:
        """
        Insert a key into the B-Tree.

        :param key: The key to be inserted
        """
        if self.root is None:
            self.root = BTreeNode(leaf=True)
            self.root.keys.append(key)
        else:
            if self.search(key) is not None:
                return  # Key already exists, do not insert duplicate
            if len(self.root.keys) == (2 * self.t) - 1:
                new_root = BTreeNode()
                new_root.children.append(self.root)
                self._split_child(new_root, 0)
                self.root = new_root
            self._insert_non_full(self.root, key)

    def _insert_non_full(self, node: BTreeNode, key: Any) -> None:
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent: BTreeNode, index: int) -> None:
        t = self.t
        child = parent.children[index]
        new_child = BTreeNode(leaf=child.leaf)

        # Move the median key to the parent
        median_index = t - 1
        median_key = child.keys[median_index]
        parent.keys.insert(index, median_key)

        # Split the keys and children to the new child
        new_child.keys = child.keys[median_index + 1 :]
        child.keys = child.keys[:median_index]

        if not child.leaf:
            new_child.children = child.children[t:]
            child.children = child.children[:t]

        parent.children.insert(index + 1, new_child)

    def search(self, key: Any) -> Optional[BTreeNode]:
        """
        Search for a key in the B-Tree.

        :param key: The key to search for
        :return: The node containing the key, or None if not found
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(
        self, node: Optional[BTreeNode], key: Any
    ) -> Optional[BTreeNode]:
        if node is None:
            return None

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return node
        elif node.leaf:
            return None
        else:
            return self._search_recursive(node.children[i], key)

    def __str__(self) -> str:
        """
        Return a string representation of the B-Tree, with the root at the top
        and children indented below their parents.

        :return: String representation of the B-Tree
        """
        lines: List[str] = []
        self._str_recursive(self.root, 0, lines)
        return "".join(lines)

    def _str_recursive(
        self, node: Optional[BTreeNode], level: int, lines: List[str]
    ) -> None:
        if node is None:
            return

        indent = "  " * level
        for key in node.keys:
            lines.append(f"{indent}{key}\n")

        if not node.leaf:
            for child in node.children:
                self._str_recursive(child, level + 1, lines)
