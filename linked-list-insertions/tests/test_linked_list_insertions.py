import pytest
from linked_list_insertions.linked_list_insertions import LinkedList, Node


### 1- Can successfully instantiate an empty linked list
def test_empty_linked_list():
    ll = LinkedList()
    expected = None
    actual = ll.head
    assert expected == actual


#### 2- Can successfully add a node to the end of the linked list
def test_appending_a_node_to_the_end_of_the_linked_list():
    ll = LinkedList()
    batool = Node("Batool")
    ll.append(batool)

    expected = f"Batool -> {None}"
    actual = ll.__str__()
    assert expected == actual


#### 3- Can successfully add multiple nodes to the end of a linked list
def test_appending_multiple_nodes_to_the_linked_list():
    ll = LinkedList()
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    ll.append(btoush)
    ll.append(yahia)
    ll.append(batool)

    expected = f"Btoush -> Yahia -> Batool -> {None}"
    actual = ll.__str__()
    assert expected == actual


### 4- Can successfully insert a node before a node located i the middle of a linked list
def test_inserting_a_node_before_a_node_located_in_the_middle_of_the_linked_list():
    ll = LinkedList()
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    one = Node("number 1")
    two = Node("number 2")
    before = Node("added before")
    ll.append(batool)
    ll.append(yahia)
    ll.append(btoush)
    ll.append(one)
    ll.append(two)
    ll.insert_before(btoush, before)

    expected = (
        f"Batool -> Yahia -> added before -> Btoush -> number 1 -> number 2 -> {None}"
    )
    actual = ll.__str__()
    assert expected == actual


### 5- Can successfully insert a node before the first node of a linked list
def test_inserting_a_node_before_the_first_node_of_the_linked_list():
    ll = LinkedList()
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    one = Node("number 1")
    two = Node("number 2")
    before = Node("added before")
    ll.append(batool)
    ll.append(yahia)
    ll.append(btoush)
    ll.append(one)
    ll.append(two)
    ll.insert_before(batool, before)

    expected = (
        f"added before -> Batool -> Yahia -> Btoush -> number 1 -> number 2 -> {None}"
    )
    actual = ll.__str__()
    assert expected == actual


### 6- Can successfully insert after a node in the middle of the linked list
def test_inserting_a_node_after_a_node_located_in_the_middle_of_the_linked_list():
    ll = LinkedList()
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    one = Node("number 1")
    two = Node("number 2")
    after = Node("added after")

    ll.append(batool)
    ll.append(yahia)
    ll.append(btoush)
    ll.append(one)
    ll.append(two)
    ll.insert_after(btoush, after)

    expected = (
        f"Batool -> Yahia -> Btoush -> added after -> number 1 -> number 2 -> {None}"
    )
    actual = ll.__str__()
    assert expected == actual


### 7- Can successfully insert a node after the last node of the linked list:
def test_inserting_a_node_after_the_last_node_of_the_linked_list():
    ll = LinkedList()
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    one = Node("number 1")
    two = Node("number 2")
    after = Node("added after")

    ll.append(batool)
    ll.append(yahia)
    ll.append(btoush)
    ll.append(one)
    ll.append(two)
    ll.insert_after(two, after)

    expected = (
        f"Batool -> Yahia -> Btoush -> number 1 -> number 2 -> added after -> {None}"
    )
    actual = ll.__str__()
    assert expected == actual
