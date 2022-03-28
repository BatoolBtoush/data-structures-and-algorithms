import pytest
from stack_queue_pseudo.stack_queue_pseudo import Node, Stack, PseudoQueue

# test 1: enqueuing to the queue
def test_enQueue(pseudoqueue):
    pass

# test 2: dequeuing from the queue
def test_deQueue(pseudoqueue):
    pseudoqueue.deQueue()

# test 3: return the dequeued node
def test_print_popped_node_deQueue(pseudoqueue):

    actual = pseudoqueue.deQueue()
    expected = "Bat"
    assert actual == expected

# test 4: return the dequeued node
def test_print_popped_another_node_deQueue(pseudoqueue):
    pseudoqueue.deQueue()

    actual = pseudoqueue.deQueue()
    expected = "Yahia"
    assert actual == expected

# test 5: raise exception
def test_is_empty_stack2():
    with pytest.raises(Exception):
        pseudoqueue = PseudoQueue()
        pseudoqueue.deQueue()


@pytest.fixture
def pseudoqueue():
    pseudoqueue = PseudoQueue()

    bat = Node("Bat")
    yahia = Node("Yahia")
    btoush = Node("Btoush")

    pseudoqueue.enQueue(btoush)
    pseudoqueue.enQueue(yahia)
    pseudoqueue.enQueue(bat)

    return pseudoqueue
