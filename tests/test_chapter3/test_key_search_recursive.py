import unittest
from src.chapter3.key_search_recursive import key_search_recursive


class TestKeySearchRecursive(unittest.TestCase):
    def test_key_search_recursive(self) -> None:
        # Test case 1: Key exists in the list
        self.assertEqual(key_search_recursive([1, 3, 5, 7, 9], 5), 2)

        # Test case 2: Key does not exist in the list
        self.assertEqual(key_search_recursive([1, 3, 5, 7, 9], 4), -1)

        # Test case 3: Empty list
        self.assertEqual(key_search_recursive([], 1), -1)

        # Test case 4: Key is the first element
        self.assertEqual(key_search_recursive([1, 3, 5, 7, 9], 1), 0)

        # Test case 5: Key is the last element
        self.assertEqual(key_search_recursive([1, 3, 5, 7, 9], 9), 4)


if __name__ == "__main__":
    unittest.main()
