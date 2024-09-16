def longest_common_substring(s1: str, s2: str) -> str:
    """
    Find the longest common substring between two strings.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        str: The longest common substring.
    """
    if not s1 or not s2:
        return ""

    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_index = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i

    return s1[end_index - max_length : end_index] if max_length > 1 else ""
