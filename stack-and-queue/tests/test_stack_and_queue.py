from threading import activeCount
import pytest
from stack_and_queue.stack_and_queue import Node, Stack, Queue

##### Stack Tests #####

# test 1: instantiate an empty stack
def test_instantiate_an_empty_stack():
    stack = Stack()

    actual = stack.__str__()
    expected = "Empty Stack"
    assert actual == expected


# test 2: return top node of the stack
def test_stack_top_node():
    stack = Stack()
    bat = Node("Bat")
    stack.push(bat)

    actual = stack.top.value
    expected = "Bat"
    assert actual == expected


# test 3: pushing one node to the stack
def test_pushing_one_node_to_the_stack():
    stack = Stack()
    bat = Node("Bat")
    stack.push(bat)

    actual = stack.__str__()
    expected = "Bat -> None"
    assert actual == expected


# test 4: pushing multiple nodes to the stack
def test_pushing_multiple_nodes_to_the_stack(stack):

    actual = stack.__str__()
    expected = "Bat -> Yahia -> Btoush -> None"
    assert actual == expected


# test 5: popping from the stack
def test_stack_pop_method(stack):
    stack.pop()

    actual = stack.__str__()
    expected = "Yahia -> Btoush -> None"
    assert actual == expected


# test 6: empty a stack after multiple pops
def test_empty_a_stack_after_multiple_pops(stack):
    stack.pop()
    stack.pop()
    stack.pop()

    actual = stack.__str__()
    expected = "Empty Stack"
    assert actual == expected


# test 7: returning the popped node of the stack
def test_return_the_popped_node_of_the_stack(stack):

    actual = stack.pop()
    expected = "Bat"
    assert actual == expected


# test 8: raise an exception if we're popping from an empty stack
def test_stack_pop_method_if_the_stack_is_empty():
    with pytest.raises(Exception):
        stack = Stack()
        stack.pop()


# test 9: peek at the top node of the stack
def test_stack_peek_method(stack):

    actual = stack.peek()
    expected = "Bat"
    assert actual == expected


# test 10: raise an exception if we're peeking through an empty stack
def test_stack_peek_method_if_the_stack_is_empty():
    with pytest.raises(Exception):
        stack = Stack()
        stack.peek()


# test 11: is_empty stack method? True
def test_stack_is_empty_method():
    stack = Stack()

    actual = stack.is_empty()
    expected = True
    assert actual == expected


# test 12: is_empty stack method? False
def test_stack_isnt_empty(stack):
    actual = stack.is_empty()
    expected = False
    assert actual == expected


##### Queue Tests #####


# test 13: instantiate an empty queue
def test_empty_queue():
    queue = Queue()

    actual = queue.__str__()
    expected = "Empty Queue"
    assert actual == expected


# test 14: return front node of the queue
def test_queue_front_node(queue):

    actual = queue.front.value
    expected = "Bat"
    assert actual == expected


# test 15: return rear node of the queue
def test_queue_rear_node(queue):

    actual = queue.rear.value
    expected = "Btoush"
    assert actual == expected


# test 16: enqeuing one node to the queue
def test_enqeuing_one_node_to_the_queue():
    queue = Queue()
    bat = Node("Bat")
    queue.enqueue(bat)

    actual = queue.__str__()
    expected = "Bat -> None"
    assert actual == expected


# test 17: enqeuing multiple nodes to the queue
def test_enqeuing_multiple_nodes_to_the_queue(queue):

    actual = queue.__str__()
    expected = "Bat -> Yahia -> Btoush -> None"
    assert actual == expected


# test 18: deqeuing a node from the queue
def test_deqeue_method(queue):
    queue.dequeue()

    actual = queue.__str__()
    expected = "Yahia -> Btoush -> None"
    assert actual == expected


# test 19: empty a queue after multiple dequeues
def test_empty_a_deqeue_after_multiple_dequeues(queue):
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    actual = queue.__str__()
    expected = "Empty Queue"
    assert actual == expected


# test 20: peek into a queue
def test_peek_method_of_the_queue(queue):

    actual = queue.peek()
    expected = "Bat"
    assert actual == expected


# test 21: raise an exception if we're dequeing from an empty queue
def test_queue_deqeue_method_if_the_queue_is_empty():
    with pytest.raises(Exception):
        queue = Queue()
        queue.dequeue()


# test 22: raise an exception if we're peeking through an empty stack
def test_queue_peek_method_if_the_queue_is_empty():
    with pytest.raises(Exception):
        queue = Queue()
        queue.peek()


# test 23: is_empty queue method? True
def test_queue_is_empty_method():
    queue = Queue()

    actual = queue.is_empty()
    expected = True
    assert actual == expected


# test 24: is_empty queue method? False
def test_queue_isnt_empty(queue):
    actual = queue.is_empty()
    expected = False
    assert actual == expected


@pytest.fixture
def stack():
    stack = Stack()
    bat = Node("Bat")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    stack.push(btoush)
    stack.push(yahia)
    stack.push(bat)

    return stack


@pytest.fixture
def queue():
    queue = Queue()
    bat = Node("Bat")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    queue.enqueue(bat)
    queue.enqueue(yahia)
    queue.enqueue(btoush)

    return queue
