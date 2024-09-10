from typing import Any
import unittest
from src.chapter3.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack: Stack[Any] = Stack()

    def test_push_and_pop(self) -> None:
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_peek(self) -> None:
        self.stack.push("test")
        self.assertEqual(self.stack.peek(), "test")
        self.assertEqual(self.stack.size(), 1)

    def test_is_empty(self) -> None:
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_size(self) -> None:
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)

    def test_pop_empty(self) -> None:
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_empty(self) -> None:
        with self.assertRaises(IndexError):
            self.stack.peek()


if __name__ == "__main__":
    unittest.main()
