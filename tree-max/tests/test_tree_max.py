from tree_max.tree_max import TreeNode, BinaryTree
import pytest


def test_empty_tree():
    binary_tree = BinaryTree()
    binary_tree.root = None
    with pytest.raises(Exception):
        binary_tree.tree_max()


def test_tree_max_one_node():
    binary_tree = BinaryTree()
    binary_tree.root = TreeNode(2)
    actual = binary_tree.tree_max()
    expected = 2
    assert actual == expected


def test_tree_max_two_nodes():
    binary_tree = BinaryTree()
    binary_tree.root = TreeNode(0)
    binary_tree.root.left = TreeNode(12)
    actual = binary_tree.tree_max()
    expected = 12
    assert actual == expected


def test_tree_max_three_nodes():
    binary_tree = BinaryTree()
    binary_tree.root = TreeNode(9)
    binary_tree.root.left = TreeNode(8)
    binary_tree.root.right = TreeNode(7)
    actual = binary_tree.tree_max()
    expected = 9
    assert actual == expected


def test_tree_max_four_nodes(binary_tree):
    actual = binary_tree.tree_max()
    expected = 200
    assert actual == expected


@pytest.fixture
def binary_tree():
    binary_tree = BinaryTree()
    binary_tree.root = TreeNode(90)
    binary_tree.root.left = TreeNode(33)
    binary_tree.root.right = TreeNode(3)
    binary_tree.root.left.left = TreeNode(99)
    binary_tree.root.left.right = TreeNode(22)
    binary_tree.root.right.left = TreeNode(200)
    return binary_tree
