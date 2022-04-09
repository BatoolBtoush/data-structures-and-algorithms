import pytest
from linked_list_zip.linked_list_zip import LinkedList, Node, zip_lists

# test 1: if linked list 1 is empty
def test_if_llist_is_empty():
    llist1 = LinkedList()
    llist2 = LinkedList()

    # nodes for the second linked list
    emily = Node("Daisy")
    adam = Node("Adam")
    jb = Node("JB")
    llist2.insert(jb)
    llist2.insert(adam)
    llist2.insert(emily)

    # merging
    zip_lists(llist1, llist2)

    expected = "Daisy -> Adam -> JB -> None"
    actual = llist1.__str__()
    assert expected == actual


# test 2: if linked list 2 is empty
def test_if_llist2_is_empty():
    llist1 = LinkedList()
    llist2 = LinkedList()

    # nodes for the first linked list
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    llist1.insert(btoush)
    llist1.insert(yahia)
    llist1.insert(batool)

    # merging
    zip_lists(llist1, llist2)

    expected = "Batool -> Yahia -> Btoush -> None"
    actual = llist1.__str__()
    assert expected == actual


# test 3: if the two linked lists are of equal length
def test_if_the_two_linked_lists_are_of_the_same_length():
    llist1 = LinkedList()
    llist2 = LinkedList()

    # nodes for the first linked list
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    llist1.insert(btoush)
    llist1.insert(yahia)
    llist1.insert(batool)

    # nodes for the second linked list
    emily = Node("Daisy")
    adam = Node("Adam")
    jb = Node("JB")
    llist2.insert(jb)
    llist2.insert(adam)
    llist2.insert(emily)

    # merging
    zip_lists(llist1, llist2)

    expected = "Batool -> Daisy -> Yahia -> Adam -> Btoush -> JB -> None"
    actual = llist1.__str__()
    assert expected == actual


# test 4: if linked list 1 is longer than linked list 2
def test_if_llist1_is_longer_than_llist2():
    llist1 = LinkedList()
    llist2 = LinkedList()

    # nodes for the first linked list
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    one = Node("number 1")
    llist1.insert(btoush)
    llist1.insert(yahia)
    llist1.insert(batool)
    llist1.append(one)

    # nodes for the second linked list
    emily = Node("Daisy")
    adam = Node("Adam")
    jb = Node("JB")
    llist2.insert(jb)
    llist2.insert(adam)
    llist2.insert(emily)

    # merging
    zip_lists(llist1, llist2)

    expected = "Batool -> Daisy -> Yahia -> Adam -> Btoush -> JB -> number 1 -> None"
    actual = llist1.__str__()
    assert expected == actual


# test 5: if linked list 1 is shorter than linked list 2
def test_if_llist1_is_shorter_than_llist2():
    llist1 = LinkedList()
    llist2 = LinkedList()

    # nodes for the first linked list
    batool = Node("Batool")
    btoush = Node("Btoush")
    llist1.insert(btoush)
    llist1.insert(batool)

    # nodes for the second linked list
    emily = Node("Daisy")
    adam = Node("Adam")
    jb = Node("JB")
    llist2.insert(jb)
    llist2.insert(adam)
    llist2.insert(emily)

    # merging
    zip_lists(llist1, llist2)

    expected = "Batool -> Daisy -> Btoush -> Adam -> JB -> None"
    actual = llist1.__str__()
    assert expected == actual
