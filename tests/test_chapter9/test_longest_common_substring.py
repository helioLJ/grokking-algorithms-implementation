import pytest
from src.chapter9.longest_common_substring import longest_common_substring


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("abcdxyz", "xyzabcd", "abcd"),
        ("zxabcdezy", "yzabcdezx", "abcdez"),
        ("", "abc", ""),
        ("abc", "", ""),
        ("programming", "programmer", "programm"),
        ("hello", "world", ""),
        ("ababc", "babca", "babc"),
    ],
)
def test_longest_common_substring(s1: str, s2: str, expected: str) -> None:
    """
    Test the longest_common_substring function with various input pairs.
    """
    assert longest_common_substring(s1, s2) == expected


def test_longest_common_substring_empty_strings() -> None:
    """
    Test the longest_common_substring function with empty strings.
    """
    assert longest_common_substring("", "") == ""


def test_longest_common_substring_same_string() -> None:
    """
    Test the longest_common_substring function with identical strings.
    """
    s = "abcdefg"
    assert longest_common_substring(s, s) == s


def test_longest_common_substring_no_common() -> None:
    """
    Test the longest_common_substring function with strings having no common substring.
    """
    assert longest_common_substring("abc", "def") == ""


def test_longest_common_substring_multiple_common() -> None:
    """
    Test the longest_common_substring function with strings having multiple common substrings.
    """
    result = longest_common_substring("abcabc", "bcabca")
    assert result == "bcabc"
