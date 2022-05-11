import pytest
from sum_odd_binary import __version__
from sum_odd_binary.sum_odd_binary import Node, Queue, TreeNode , BinaryTree, BinarySearch, sum_of_odd_numbers_breadth_first_traversal


def test_version():
    assert __version__ == '0.1.0'


def test_sum_of_odd_numbers_breadth_first_traversal(tree):
    assert sum_of_odd_numbers_breadth_first_traversal(tree) == 39

def test_sum_of_odd_numbers_pre_order_traversal(tree):
    assert tree.sum_of_odd_numbers_pre_order_traversal() == 39


@pytest.fixture
def tree():
    tree = BinarySearch()
    a = TreeNode(13)
    tree.root = a
    tree.add(11)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)

    return tree



