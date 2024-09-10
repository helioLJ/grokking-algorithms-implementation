from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """
    A class representing a stack data structure.
    """

    def __init__(self) -> None:
        """
        Initialize an empty stack.
        """
        self.items: list[T] = []

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def push(self, item: T) -> None:
        """
        Push an item onto the stack.

        Args:
            item (T): The item to be pushed onto the stack.
        """
        self.items.append(item)

    def pop(self) -> T:
        """
        Remove and return the top item from the stack.

        Returns:
            T: The top item from the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")

    def peek(self) -> T:
        """
        Return the top item from the stack without removing it.

        Returns:
            T: The top item from the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")

    def size(self) -> int:
        """
        Get the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        return len(self.items)
