import pytest
from linked_list.linked_list import LinkedList, Node

# 1- Can successfully instantiate an empty linked list
def test_empty_linked_list():
    ll = LinkedList()
    expected = None
    actual = ll.head
    assert expected == actual


# 2- Can properly insert into the linked list
def test_insert_method():
    ll = LinkedList()
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    ll.insert(btoush)
    ll.insert(yahia)
    ll.insert(batool)

    expected = f"Batool -> Yahia -> Btoush -> {None}"
    actual = ll.__str__()
    assert expected == actual


# 3- The head property will properly point to the first node in the linked list
def test_if_the_head_property_points_to_the_first_node():
    ll = LinkedList()
    batool = Node("Batool")
    ll.insert(batool)

    expected = "Batool"
    actual = batool.value
    assert expected == actual


# 4- Can properly insert multiple nodes into the linked list
def test_insert_multiple_nodes_into_the_linked_list():
    ll = LinkedList()
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    one = Node("number 1")
    two = Node("number 2")
    ll.insert(btoush)
    ll.insert(yahia)
    ll.insert(batool)
    ll.insert(two)
    ll.insert(one)

    expected = f"number 1 -> number 2 -> Batool -> Yahia -> Btoush -> {None}"
    actual = ll.__str__()
    assert expected == actual


# 5- Will return true when finding a value within the linked list that exists (includes method)
def test_if_a_value_exists_in_the_linked_list_using_includes_method():
    ll = LinkedList()
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    ll.insert(btoush)
    ll.insert(yahia)
    ll.insert(batool)

    expected = True
    actual = ll.includes("Batool")
    assert expected == actual


# 6- Will return false when searching for a value in the linked list that does not exist (includes method)
def test_if_a_value_doesnt_exist_in_the_linked_list_using_includes_method():
    ll = LinkedList()
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    ll.insert(btoush)
    ll.insert(yahia)
    ll.insert(batool)

    expected = False
    actual = ll.includes("Bat")
    assert expected == actual


# 7- Can properly return a collection of all the values that exist in the linked list
def test_to_retrun_a_collection_of_the_values_in_the_linked_list():
    ll = LinkedList()
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    one = Node("number 1")
    two = Node("number 2")
    ll.insert(btoush)
    ll.insert(yahia)
    ll.insert(batool)
    ll.append(one)
    ll.append(two)

    expected = ["Batool", "Yahia", "Btoush", "number 1", "number 2"]
    actual = ll.display()
    assert expected == actual


# 8- testing the append method
def test_appending_to_the_linked_list():
    ll = LinkedList()
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")

    ll.append(btoush)
    ll.append(yahia)
    ll.append(batool)

    expected = f"Btoush -> Yahia -> Batool -> {None}"
    actual = ll.to_string()
    assert expected == actual


# 9- testing the to_string method
def test_the_to_string_method():
    ll = LinkedList()
    batool = Node("Batool")
    ll.insert(batool)

    expected = f"Batool -> {None}"
    actual = ll.to_string()
    assert expected == actual


# @pytest.fixture
# def ll():

#
#     one = Node("number 1")
#     two = Node("number 2")

#     ll.append(btoush)
#     ll.insert(two)
#     ll.insert(one)
