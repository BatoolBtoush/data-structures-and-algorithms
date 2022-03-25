from tracemalloc import start
import pytest
from reverse_linked_list.reverse_linked_list import LinkedList, Node

# test 1: reverse an empty linked list
def test_empty_linked_list():
    ll = LinkedList()
    ll.reverse_linked_list()

    actual = ll.__str__()
    expected = "Empty linked list"
    assert actual == expected


# test 2: reverse a linked list with even number of nodes
def test_reverse_a_linked_list_with_even_number_of_nodes():
    ll = LinkedList()
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    star = Node("*")
    ll.append(star)
    ll.append(btoush)
    ll.append(yahia)
    ll.append(batool)
    ll.reverse_linked_list()

    actual = ll.__str__()
    expected = "Batool -> Yahia -> Btoush -> * -> None"
    assert actual == expected


# test 3: reverse a linked list with odd number of nodes
def test_reverse_a_linked_list_with_odd_number_of_nodes():
    ll = LinkedList()
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    ll.append(btoush)
    ll.append(yahia)
    ll.append(batool)
    ll.reverse_linked_list()

    actual = ll.__str__()
    expected = "Batool -> Yahia -> Btoush -> None"
    assert actual == expected
