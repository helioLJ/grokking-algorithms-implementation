from src.chapter11.reverse_index import ReverseIndex


def test_add_document() -> None:
    index = ReverseIndex()
    index.add_document(1, "Hello world")
    index.add_document(2, "Hello Python")

    assert index.index == {"hello": {1, 2}, "world": {1}, "python": {2}}


def test_search_single_word() -> None:
    index = ReverseIndex()
    index.add_document(1, "Hello world")
    index.add_document(2, "Hello Python")
    index.add_document(3, "Python programming")

    assert index.search("hello") == [1, 2]
    assert index.search("python") == [2, 3]
    assert index.search("programming") == [3]
    assert index.search("nonexistent") == []


def test_search_multiple_words() -> None:
    index = ReverseIndex()
    index.add_document(1, "Hello world")
    index.add_document(2, "Hello Python")
    index.add_document(3, "Python programming")
    index.add_document(4, "World of Python")

    assert set(index.search("hello python")) == {2}
    assert set(index.search("python world")) == {4}
    assert set(index.search("hello world")) == {1}
    assert index.search("hello programming") == []


def test_case_insensitivity() -> None:
    index = ReverseIndex()
    index.add_document(1, "Hello World")
    index.add_document(2, "PYTHON PROGRAMMING")

    assert index.search("hello") == [1]
    assert index.search("WORLD") == [1]
    assert index.search("python") == [2]
    assert index.search("PROGRAMMING") == [2]


def test_empty_query() -> None:
    index = ReverseIndex()
    index.add_document(1, "Hello world")

    assert index.search("") == []


def test_empty_index() -> None:
    index = ReverseIndex()

    assert index.search("hello") == []
    assert index.search("") == []
