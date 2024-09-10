from typing import Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def append(self, data: int) -> None:
        """Add a new node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data: int) -> None:
        """Add a new node with the given data to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data: int) -> None:
        """Delete the first occurrence of a node with the given data."""
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def find(self, data: int) -> Optional[Node]:
        """Find and return the first node with the given data, or None if not found."""
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def print_list(self) -> None:
        """Print the entire linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next
