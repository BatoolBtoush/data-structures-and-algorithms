import pytest
from linked_list_kth.linked_list_kth import LinkedList




# 1- Can successfully instantiate an empty linked list
def test_empty_linked_list():
    ll = LinkedList()
    expected = None
    actual = ll.head
    assert expected == actual
