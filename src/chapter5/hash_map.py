def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """
    Find two numbers in the given list that add up to the target sum.

    Args:
    nums (list[int]): A list of integers.
    target (int): The target sum.

    Returns:
    tuple[int, int] | None: A tuple containing the indices of the two numbers
                            that add up to the target sum, or None if no such pair exists.
    """
    num_map: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return (num_map[complement], i)
        num_map[num] = i
    return None
