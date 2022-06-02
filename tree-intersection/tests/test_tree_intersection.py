from tree_intersection.tree_intersection import tree_intersection, TreeNode, BinaryTree
import pytest


def test_tree_intersection_empty_trees():
    tree1 = BinaryTree()
    tree2 = BinaryTree()

    with pytest.raises(Exception):
        tree_intersection(tree1, tree2)


def test_tree_intersection_one_empty_tree():
    tree1 = BinaryTree()
    tree1.root = TreeNode(150)
    tree1.root.left = TreeNode(100)
    tree1.root.right = TreeNode(200)

    tree2 = BinaryTree()

    with pytest.raises(Exception):
        tree_intersection(tree1, tree2)


def test_tree_intersection_with_intersections():
    tree1 = BinaryTree()
    tree1.root = TreeNode(150)
    tree1.root.left = TreeNode(100)
    tree1.root.right = TreeNode(250)
    tree1.root.left.left = TreeNode(75)
    tree1.root.left.right = TreeNode(160)
    tree1.root.left.right.left = TreeNode(125)
    tree1.root.left.right.right = TreeNode(175)
    tree1.root.right.left = TreeNode(200)
    tree1.root.right.right = TreeNode(350)
    tree1.root.right.right.left = TreeNode(300)
    tree1.root.right.right.right = TreeNode(500)

    tree2 = BinaryTree()
    tree2.root = TreeNode(42)
    tree2.root.left = TreeNode(100)
    tree2.root.right = TreeNode(600)
    tree2.root.left.left = TreeNode(15)
    tree2.root.left.right = TreeNode(160)
    tree2.root.left.right.left = TreeNode(125)
    tree2.root.left.right.right = TreeNode(175)
    tree2.root.right.left = TreeNode(200)
    tree2.root.right.right = TreeNode(350)
    tree2.root.right.right.left = TreeNode(4)
    tree2.root.right.right.right = TreeNode(500)

    actual = tree_intersection(tree1, tree2)
    expected = [100, 160, 125, 175, 200, 350, 500]
    assert actual == expected


def test_tree_intersection_no_intersection():
    tree1 = BinaryTree()
    tree1.root = TreeNode(150)
    tree1.root.left = TreeNode(10)
    tree1.root.right = TreeNode(200)

    tree2 = BinaryTree()
    tree2.root = TreeNode(42)
    tree2.root.left = TreeNode(100)
    tree2.root.right = TreeNode(600)

    actual = tree_intersection(tree1, tree2)
    expected = []
    assert actual == expected


def test_tree_intersection_one_tree_has_string_value():
    tree1 = BinaryTree()
    tree1.root = TreeNode("string value")
    tree1.root.left = TreeNode(100)
    tree1.root.right = TreeNode(200)

    tree2 = BinaryTree()
    tree2.root = TreeNode(42)
    tree2.root.left = TreeNode(100)
    tree2.root.right = TreeNode(600)

    actual = tree_intersection(tree1, tree2)
    expected = [100]
    assert actual == expected


def test_tree_intersection_both_trees_have_string_values():
    tree1 = BinaryTree()
    tree1.root = TreeNode("string value")
    tree1.root.left = TreeNode(100)
    tree1.root.right = TreeNode(200)

    tree2 = BinaryTree()
    tree2.root = TreeNode("string value")
    tree2.root.left = TreeNode(100)
    tree2.root.right = TreeNode(600)
    
    actual = tree_intersection(tree1, tree2)
    expected = ["string value", 100]
    assert actual == expected
