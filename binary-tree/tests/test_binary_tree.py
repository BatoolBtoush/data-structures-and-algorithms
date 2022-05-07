from binary_tree.binary_tree import BinarySearch, BinaryTree, TreeNode
import pytest


def test_empty_tree():
    binary_tree = BinaryTree()
    binary_tree.root = None
    with pytest.raises(Exception):
        binary_tree.pre_order()


def test_a_tree_with_a_root_node():
    binary_tree = BinaryTree()
    binary_tree.root = TreeNode(1)
    actual = binary_tree.pre_order()
    expected = [1]
    assert actual == expected


def test_pre_order(binary_tree):
    actual = binary_tree.pre_order()
    expected = [1, 2, 4, 5, 3, 6, 7]
    assert actual == expected


def test_in_order(binary_tree):
    actual = binary_tree.in_order()
    expected = [4, 2, 5, 1, 6, 3, 7]
    assert actual == expected


def test_post_order(binary_tree):
    actual = binary_tree.post_order()
    expected = [4, 5, 2, 6, 7, 3, 1]
    assert actual == expected


def test_add(binary_search_tree):
    binary_search_tree.add(9)
    actual = binary_search_tree.contains(9)
    expected = True
    assert actual == expected


def test_add_duplicate(binary_search_tree):
    with pytest.raises(Exception):
        binary_search_tree.add(1)


def test_contains_true(binary_search_tree):
    actual = binary_search_tree.contains(1)
    expected = True
    assert actual == expected


def test_contains_false(binary_search_tree):
    actual = binary_search_tree.contains(3)
    expected = False
    assert actual == expected


@pytest.fixture
def binary_tree():
    binary_tree = BinaryTree()
    binary_tree.root = TreeNode(1)
    binary_tree.root.left = TreeNode(2)
    binary_tree.root.right = TreeNode(3)
    binary_tree.root.left.left = TreeNode(4)
    binary_tree.root.left.right = TreeNode(5)
    binary_tree.root.right.left = TreeNode(6)
    binary_tree.root.right.right = TreeNode(7)
    return binary_tree


@pytest.fixture
def binary_search_tree():
    binary_search_tree = BinarySearch()
    binary_search_tree.root = TreeNode(1)
    binary_search_tree.add(80)
    binary_search_tree.add(60)
    binary_search_tree.add(70)
    binary_search_tree.add(40)
    return binary_search_tree
