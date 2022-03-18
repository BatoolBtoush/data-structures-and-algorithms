import pytest
from linked_list_kth.linked_list_kth import LinkedList,Node




# 1- Can successfully instantiate an empty linked list
def test_empty_linked_list():
    ll = LinkedList()
    expected = None
    actual = ll.head
    assert expected == actual


# 2- Where k is greater than the length of the linked list
def test_k_is_greater_than_the_length():
    ll = LinkedList()
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    ll.insert(btoush)
    ll.insert(yahia)
    ll.insert(batool)
    expected = 'The kth value is out of range'
    actual = ll.find_kth(10)
    assert expected == actual

# 3- Where k and the length of the list are the same
def test_k_and_length_are_the_same():
    ll = LinkedList()
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    ll.insert(btoush)
    ll.insert(yahia)
    ll.insert(batool)
    expected = None
    actual = ll.find_kth(3)
    assert expected == actual


# 4- Where k is not a positive integer
def test_k_is_not_a_positive_integer():
    ll = LinkedList()
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    ll.insert(btoush)
    ll.insert(yahia)
    ll.insert(batool)
    expected = 'The kth value is of negative value, please provide a positive one!'
    actual = ll.find_kth(-50)
    assert expected == actual

# 5- Where the linked list is of a size 1
def test_the_linked_list_is_of_size_1():
    ll = LinkedList()
    batool = Node("Batool")
    ll.insert(batool)
    expected = 'Batool'
    actual = ll.find_kth(0)
    assert expected == actual

# 6- additional test 
def test_one():
    ll = LinkedList()
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    one = Node("number 1")
    two = Node("number 2")
    ll.append(one)
    ll.append(two)
    ll.insert(btoush)
    ll.insert(yahia)
    ll.insert(batool)
    expected = 'number 2'
    actual = ll.find_kth(0)
    assert expected == actual

# 7- additional test
def test_two():
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
    expected = 'Btoush'
    actual = ll.find_kth(2)
    assert expected == actual

# 8- additional test when the kth value is negative
def test_three():
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
    expected = 'The kth value is of negative value, please provide a positive one!'
    actual = ll.find_kth(-6)
    assert expected == actual

# 9- additional test when k is equal to the length of the linked list
def test_four():
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
    expected = None
    actual = ll.find_kth(5)
    assert expected == actual

