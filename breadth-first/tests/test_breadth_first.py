from breadth_first.breadth_first import breadth_first, BinaryTree, TreeNode, Queue
import pytest


def test_empty_tree():
    tree = BinaryTree()
    tree.root = None
    with pytest.raises(Exception):
        breadth_first(tree)


def test_breadth_first(tree):
    actual = breadth_first(tree)
    expected = ["A", "B", "C", "D", "E", "F", "G"]
    assert actual == expected


def test_breadth_first_with_one_node(tree):
    tree.root = TreeNode(1)
    actual = breadth_first(tree)
    expected = [1]
    assert actual == expected


def test_breadth_first_with_two_nodes(tree):
    tree.root = TreeNode(1)
    tree.root.left = TreeNode("B")
    actual = breadth_first(tree)
    expected = [1, "B"]
    assert actual == expected


def test_breadth_first_with_three_nodes(tree):
    tree.root = TreeNode(1)
    tree.root.left = TreeNode("B")
    tree.root.right = TreeNode("C")
    actual = breadth_first(tree)
    expected = [1, "B", "C"]
    assert actual == expected


@pytest.fixture
def tree():
    tree = BinaryTree()
    tree.root = TreeNode("A")
    tree.root.left = TreeNode("B")
    tree.root.right = TreeNode("C")
    tree.root.left.left = TreeNode("D")
    tree.root.left.right = TreeNode("E")
    tree.root.right.left = TreeNode("F")
    tree.root.right.right = TreeNode("G")
    return tree
