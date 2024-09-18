from typing import List, Optional, Generic, TypeVar, Callable, Any
from functools import total_ordering

T = TypeVar("T")


@total_ordering
class ComparableElement(Generic[T]):
    def __init__(self, value: T, compare: Callable[[Any, Any], bool]):
        self.value = value
        self.compare = compare

    def __lt__(self, other: "ComparableElement[T]") -> bool:
        return self.compare(self.value, other.value)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ComparableElement):
            return NotImplemented
        return bool(self.value == other.value)


class MinHeap(Generic[T]):
    """
    A min-heap implementation using a list.
    """

    def __init__(self, compare: Callable[[Any, Any], bool] = lambda x, y: x < y):
        """
        Initialize an empty heap.

        :param compare: A function to compare two elements, defaults to less than operator.
        """
        self.heap: List[ComparableElement[T]] = []
        self.compare = compare

    def parent(self, i: int) -> int:
        """
        Get the parent index of a given index.

        :param i: The index of the current element.
        :return: The index of the parent element.
        """
        return (i - 1) // 2

    def left_child(self, i: int) -> int:
        """
        Get the left child index of a given index.

        :param i: The index of the current element.
        :return: The index of the left child element.
        """
        return 2 * i + 1

    def right_child(self, i: int) -> int:
        """
        Get the right child index of a given index.

        :param i: The index of the current element.
        :return: The index of the right child element.
        """
        return 2 * i + 2

    def swap(self, i: int, j: int) -> None:
        """
        Swap two elements in the heap.

        :param i: The index of the first element.
        :param j: The index of the second element.
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key: T) -> None:
        """
        Insert a new key into the heap.

        :param key: The key to be inserted.
        """
        self.heap.append(ComparableElement(key, self.compare))
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i: int) -> None:
        """
        Maintain the heap property by moving an element up the tree.

        :param i: The index of the element to heapify up.
        """
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._heapify_up(parent)

    def extract_min(self) -> Optional[T]:
        """
        Extract and return the minimum element from the heap.

        :return: The minimum element, or None if the heap is empty.
        """
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop().value

        min_elem = self.heap[0].value
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_elem

    def _heapify_down(self, i: int) -> None:
        """
        Maintain the heap property by moving an element down the tree.

        :param i: The index of the element to heapify down.
        """
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right

        if min_index != i:
            self.swap(i, min_index)
            self._heapify_down(min_index)

    def get_min(self) -> Optional[T]:
        """
        Get the minimum element from the heap without removing it.

        :return: The minimum element, or None if the heap is empty.
        """
        return self.heap[0].value if self.heap else None

    def size(self) -> int:
        """
        Get the number of elements in the heap.

        :return: The number of elements in the heap.
        """
        return len(self.heap)

    def is_empty(self) -> bool:
        """
        Check if the heap is empty.

        :return: True if the heap is empty, False otherwise.
        """
        return len(self.heap) == 0


class MaxHeap(Generic[T]):
    """
    A max-heap implementation using a list.
    """

    def __init__(self, compare: Callable[[Any, Any], bool] = lambda x, y: x > y):
        """
        Initialize an empty heap.

        :param compare: A function to compare two elements, defaults to greater than operator.
        """
        self.heap: List[ComparableElement[T]] = []
        self.compare = compare

    def parent(self, i: int) -> int:
        """
        Get the parent index of a given index.

        :param i: The index of the current element.
        :return: The index of the parent element.
        """
        return (i - 1) // 2

    def left_child(self, i: int) -> int:
        """
        Get the left child index of a given index.

        :param i: The index of the current element.
        :return: The index of the left child element.
        """
        return 2 * i + 1

    def right_child(self, i: int) -> int:
        """
        Get the right child index of a given index.

        :param i: The index of the current element.
        :return: The index of the right child element.
        """
        return 2 * i + 2

    def swap(self, i: int, j: int) -> None:
        """
        Swap two elements in the heap.

        :param i: The index of the first element.
        :param j: The index of the second element.
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key: T) -> None:
        """
        Insert a new key into the heap.

        :param key: The key to be inserted.
        """
        self.heap.append(ComparableElement(key, self.compare))
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i: int) -> None:
        """
        Maintain the heap property by moving an element up the tree.

        :param i: The index of the element to heapify up.
        """
        parent = self.parent(i)
        if i > 0 and self.compare(self.heap[i].value, self.heap[parent].value):
            self.swap(i, parent)
            self._heapify_up(parent)

    def extract_max(self) -> Optional[T]:
        """
        Extract and return the maximum element from the heap.

        :return: The maximum element, or None if the heap is empty.
        """
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop().value

        max_elem = self.heap[0].value
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_elem

    def _heapify_down(self, i: int) -> None:
        """
        Maintain the heap property by moving an element down the tree.

        :param i: The index of the element to heapify down.
        """
        max_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.compare(
            self.heap[left].value, self.heap[max_index].value
        ):
            max_index = left
        if right < len(self.heap) and self.compare(
            self.heap[right].value, self.heap[max_index].value
        ):
            max_index = right

        if max_index != i:
            self.swap(i, max_index)
            self._heapify_down(max_index)

    def get_max(self) -> Optional[T]:
        """
        Get the maximum element from the heap without removing it.

        :return: The maximum element, or None if the heap is empty.
        """
        return self.heap[0].value if self.heap else None

    def size(self) -> int:
        """
        Get the number of elements in the heap.

        :return: The number of elements in the heap.
        """
        return len(self.heap)

    def is_empty(self) -> bool:
        """
        Check if the heap is empty.

        :return: True if the heap is empty, False otherwise.
        """
        return len(self.heap) == 0
