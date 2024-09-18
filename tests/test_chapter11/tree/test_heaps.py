from src.chapter11.tree.heaps import MinHeap, MaxHeap


def test_min_heap_insert_and_extract_min() -> None:
    heap = MinHeap[int]()
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    heap.insert(1)

    assert heap.extract_min() == 1
    assert heap.extract_min() == 3
    assert heap.extract_min() == 5
    assert heap.extract_min() == 7
    assert heap.extract_min() is None


def test_min_heap_get_min() -> None:
    heap = MinHeap[int]()
    assert heap.get_min() is None

    heap.insert(5)
    heap.insert(3)
    heap.insert(7)

    assert heap.get_min() == 3
    heap.extract_min()
    assert heap.get_min() == 5


def test_min_heap_size_and_is_empty() -> None:
    heap = MinHeap[int]()
    assert heap.is_empty()
    assert heap.size() == 0

    heap.insert(5)
    heap.insert(3)
    heap.insert(7)

    assert not heap.is_empty()
    assert heap.size() == 3

    heap.extract_min()
    assert heap.size() == 2

    heap.extract_min()
    heap.extract_min()
    assert heap.is_empty()
    assert heap.size() == 0


def test_min_heap_insert_duplicate_values() -> None:
    heap = MinHeap[int]()
    heap.insert(5)
    heap.insert(3)
    heap.insert(3)
    heap.insert(1)

    assert heap.extract_min() == 1
    assert heap.extract_min() == 3
    assert heap.extract_min() == 3
    assert heap.extract_min() == 5
    assert heap.extract_min() is None


def test_min_heap_large_number_of_elements() -> None:
    heap = MinHeap[int]()
    elements = [10, 5, 15, 2, 8, 12, 18, 1, 7, 9]
    for elem in elements:
        heap.insert(elem)

    sorted_elements = sorted(elements)
    for expected in sorted_elements:
        assert heap.extract_min() == expected

    assert heap.is_empty()


def test_max_heap_insert_and_extract_max() -> None:
    heap = MaxHeap[int]()
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    heap.insert(1)

    assert heap.extract_max() == 7
    assert heap.extract_max() == 5
    assert heap.extract_max() == 3
    assert heap.extract_max() == 1
    assert heap.extract_max() is None


def test_max_heap_get_max() -> None:
    heap = MaxHeap[int]()
    assert heap.get_max() is None

    heap.insert(5)
    heap.insert(3)
    heap.insert(7)

    assert heap.get_max() == 7
    heap.extract_max()
    assert heap.get_max() == 5


def test_max_heap_size_and_is_empty() -> None:
    heap = MaxHeap[int]()
    assert heap.is_empty()
    assert heap.size() == 0

    heap.insert(5)
    heap.insert(3)
    heap.insert(7)

    assert not heap.is_empty()
    assert heap.size() == 3

    heap.extract_max()
    assert heap.size() == 2

    heap.extract_max()
    heap.extract_max()
    assert heap.is_empty()
    assert heap.size() == 0


def test_max_heap_insert_duplicate_values() -> None:
    heap = MaxHeap[int]()
    heap.insert(5)
    heap.insert(3)
    heap.insert(3)
    heap.insert(1)

    assert heap.extract_max() == 5
    assert heap.extract_max() == 3
    assert heap.extract_max() == 3
    assert heap.extract_max() == 1
    assert heap.extract_max() is None


def test_max_heap_large_number_of_elements() -> None:
    heap = MaxHeap[int]()
    elements = [10, 5, 15, 2, 8, 12, 18, 1, 7, 9]
    for elem in elements:
        heap.insert(elem)

    sorted_elements = sorted(elements, reverse=True)
    for expected in sorted_elements:
        assert heap.extract_max() == expected

    assert heap.is_empty()
