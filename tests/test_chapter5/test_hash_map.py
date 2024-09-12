from pytest_benchmark.fixture import BenchmarkFixture  # type: ignore

from src.chapter5.hash_map import two_sum


def test_two_sum_basic() -> None:
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)


def test_two_sum_no_solution() -> None:
    assert two_sum([2, 7, 11, 15], 30) is None


def test_two_sum_duplicate_numbers() -> None:
    assert two_sum([3, 3], 6) == (0, 1)


def test_two_sum_zero_target() -> None:
    assert two_sum([0, 1, 2], 0) is None


def test_two_sum_negative_numbers() -> None:
    assert two_sum([-1, -2, -3, -4, -5], -8) == (2, 4)


def test_two_sum_large_list() -> None:
    large_list = list(range(10000))
    target = 19997
    assert two_sum(large_list, target) == (9998, 9999)


def test_two_sum_empty_list() -> None:
    assert two_sum([], 10) is None


def test_two_sum_performance(benchmark: BenchmarkFixture) -> None:
    large_list = list(range(100000))
    target = 199997
    result = benchmark(two_sum, large_list, target)
    assert result == (99998, 99999)
