import unittest
from src.chapter11.parallel_algorithm import parallel_map, parallel_filter


def square(x: int) -> int:
    return x**2


def is_even(x: int) -> bool:
    return x % 2 == 0


class TestParallelAlgorithm(unittest.TestCase):
    def test_parallel_map(self) -> None:
        """Test the parallel_map function with a simple squaring operation."""
        input_list = list(range(10))
        expected_output = [x**2 for x in input_list]
        result = parallel_map(square, input_list)
        self.assertEqual(result, expected_output)

    def test_parallel_map_empty_list(self) -> None:
        """Test the parallel_map function with an empty list."""
        result = parallel_map(square, [])
        self.assertEqual(result, [])

    def test_parallel_filter(self) -> None:
        """Test the parallel_filter function with a simple even number filter."""
        input_list = list(range(10))
        expected_output = [x for x in input_list if x % 2 == 0]
        result = parallel_filter(is_even, input_list)
        self.assertEqual(result, expected_output)

    def test_parallel_filter_empty_list(self) -> None:
        """Test the parallel_filter function with an empty list."""
        result = parallel_filter(is_even, [])
        self.assertEqual(result, [])

    def test_parallel_map_with_processes(self) -> None:
        """Test the parallel_map function with a specified number of processes."""
        input_list = list(range(100))
        expected_output = [x**2 for x in input_list]
        result = parallel_map(square, input_list, num_processes=2)
        self.assertEqual(result, expected_output)

    def test_parallel_filter_with_processes(self) -> None:
        """Test the parallel_filter function with a specified number of processes."""
        input_list = list(range(100))
        expected_output = [x for x in input_list if x % 2 == 0]
        result = parallel_filter(is_even, input_list, num_processes=2)
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
