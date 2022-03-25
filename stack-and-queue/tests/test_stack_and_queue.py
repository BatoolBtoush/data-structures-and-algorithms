import pytest
from stack_and_queue.stack_and_queue import Node, Stack

# test 1: return top node
def test_top_node():
    stack = Stack()    
    bat = Node("Bat")
    stack.push(bat)

    actual = stack.top.value
    expected = "Bat"
    assert actual == expected


# test 2: empty stack
def test_empty_stack():
    stack = Stack()    

    actual = stack.__str__()
    expected = "Empty stack"
    assert actual == expected


# test 3: pushing to the stack
def test_push_method():
    stack = Stack()    
    bat = Node("Bat")
    stack.push(bat)

    actual = stack.__str__()
    expected = "Bat -> None"
    assert actual == expected


# test 4: popping from the stack
def test_pop_method():
    stack = Stack()  
    bat = Node("Bat")
    stack.push(bat)  
    stack.pop()

    actual = stack.__str__()
    expected = "Empty stack"
    assert actual == expected


# test 5: returning the popped node
def test_popped_node():
    stack = Stack()  
    bat = Node("Bat")
    yahia = Node("Yahia")
    btoush = Node ("Btoush")
    stack.push(btoush)
    stack.push(yahia)
    stack.push(bat)

    actual = stack.pop()
    expected = "Bat"
    assert actual == expected


# test 6: peek, return an exception if top doesn't exist
def test_peek_method():
    stack = Stack()  
    bat = Node("Bat")
    yahia = Node("Yahia")
    btoush = Node ("Btoush")
    stack.push(btoush)
    stack.push(yahia)
    stack.push(bat)

    actual = stack.peek()
    expected = "Bat"
    assert actual == expected
    

# test 7: is empty
def test_is_empty_method():
    stack = Stack()  
    
    actual = stack.is_empty()
    expected = True
    assert actual == expected
