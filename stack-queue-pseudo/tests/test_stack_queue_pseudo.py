import pytest
from stack_queue_pseudo.stack_queue_pseudo import Node, Stack, PseudoQueue

# test 1: enqueuing to the queue
def test_enqueue(pseudoqueue):
    pass


# test 2: top of stack one
def test_top_of_stack_one(pseudoqueue):
    
    actual = pseudoqueue.stack1.top.value
    expected = "btoush"
    assert actual == expected


# test 3: return the dequeued node
def test_print_popped_node_dequeue(pseudoqueue):

    actual = pseudoqueue.dequeue()
    expected = "btoush"
    assert actual == expected


# test 4: return the dequeued node
def test_print_popped_another_node_dequeue(pseudoqueue):
    pseudoqueue.dequeue()

    actual = pseudoqueue.dequeue()
    expected = "yahia"
    assert actual == expected


# test 5: raise exception
def test_is_empty_stack2():
    with pytest.raises(Exception):
        pseudoqueue = PseudoQueue()
        pseudoqueue.dequeue()


@pytest.fixture
def pseudoqueue():
    pseudoqueue = PseudoQueue()

    pseudoqueue.enqueue("btoush")
    pseudoqueue.enqueue("yahia")
    pseudoqueue.enqueue("bat")

    return pseudoqueue
