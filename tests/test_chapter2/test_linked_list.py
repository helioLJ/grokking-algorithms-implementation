import pytest
from src.chapter2.linked_list import LinkedList, Node


def test_node_creation() -> None:
    node = Node(5)
    assert node.data == 5
    assert node.next is None


def test_linked_list_creation() -> None:
    ll = LinkedList()
    assert ll.head is None


def test_append() -> None:
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    head = ll.head
    assert head is not None
    assert head.data == 1
    assert head.next is not None
    assert head.next.data == 2
    assert head.next.next is not None
    assert head.next.next.data == 3
    assert head.next.next.next is None


def test_prepend() -> None:
    ll = LinkedList()
    ll.prepend(3)
    ll.prepend(2)
    ll.prepend(1)

    head = ll.head
    assert head is not None
    assert head.data == 1
    assert head.next is not None
    assert head.next.data == 2
    assert head.next.next is not None
    assert head.next.next.data == 3
    assert head.next.next.next is None


def test_delete() -> None:
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    ll.delete(2)
    head = ll.head
    assert head is not None
    assert head.data == 1
    assert head.next is not None
    assert head.next.data == 3
    assert head.next.next is None

    ll.delete(1)
    head = ll.head
    assert head is not None
    assert head.data == 3
    assert head.next is None

    ll.delete(3)
    assert ll.head is None


def test_find() -> None:
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    found_node = ll.find(2)
    assert found_node is not None and found_node.data == 2
    assert ll.find(4) is None


def test_print(capsys: pytest.CaptureFixture[str]) -> None:
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    ll.print_list()
    captured = capsys.readouterr()
    assert captured.out == "1 -> 2 -> 3\n"
