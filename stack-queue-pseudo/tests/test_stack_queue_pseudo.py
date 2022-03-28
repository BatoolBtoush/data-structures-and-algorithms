import pytest
from stack_queue_pseudo.stack_queue_pseudo import Node, Stack, PseudoQueue

# test 1: enqueuing to the queue
def test_enqueue(pseudoqueue):
    pass


# test 2: dequeuing from the queue
def test_dequeue(pseudoqueue):
    pseudoqueue.dequeue()


# test 3: return the dequeued node
def test_print_popped_node_dequeue(pseudoqueue):

    actual = pseudoqueue.dequeue()
    expected = "Bat"
    assert actual == expected


# test 4: return the dequeued node
def test_print_popped_another_node_dequeue(pseudoqueue):
    pseudoqueue.dequeue()

    actual = pseudoqueue.dequeue()
    expected = "Yahia"
    assert actual == expected


# test 5: raise exception
def test_is_empty_stack2():
    with pytest.raises(Exception):
        pseudoqueue = PseudoQueue()
        pseudoqueue.dequeue()


@pytest.fixture
def pseudoqueue():
    pseudoqueue = PseudoQueue()

    bat = Node("Bat")
    yahia = Node("Yahia")
    btoush = Node("Btoush")

    pseudoqueue.enqueue(btoush)
    pseudoqueue.enqueue(yahia)
    pseudoqueue.enqueue(bat)

    return pseudoqueue
