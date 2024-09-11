import unittest
from src.chapter4.quick_sort import quick_sort


class TestQuickSort(unittest.TestCase):
    def test_empty_list(self) -> None:
        self.assertEqual(quick_sort([]), [])

    def test_single_element(self) -> None:
        self.assertEqual(quick_sort([1]), [1])

    def test_sorted_list(self) -> None:
        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self) -> None:
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self) -> None:
        self.assertEqual(
            quick_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]),
            [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9],
        )

    def test_list_with_duplicates(self) -> None:
        self.assertEqual(quick_sort([3, 3, 3, 1, 1, 2, 2]), [1, 1, 2, 2, 3, 3, 3])


if __name__ == "__main__":
    unittest.main()
