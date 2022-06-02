class TreeNode:
    """
    Class for initializing a tree TreeNodes.
    Each TreeNode has a value and almost everyone of which has a left and a right child.
    """

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return f"{self.value} --> {self.right}"


class BinaryTree:
    """ "
    Class for initializing a binary tree with TreeNodes, which are linked to each other.
    The root TreeNode is the first TreeNode in the point of access to the tree.
    Class methods:
    - pre_order() - returns a list of values in pre-order traversal (root, left, right)
    - in_order() - returns a list of values in in-order traversal (left, root, right)
    - post_order() - returns a list of values in post-order traversal (left, right, root)
    """

    def __init__(self):
        self.root = None

    def pre_order(self):
        stack = []

        if self.root is None:
            raise Exception("Tree is empty")

        def _walk(root):
            stack.append(root.value)

            if root.left:
                _walk(root.left)
            if root.right:
                _walk(root.right)

        _walk(self.root)
        return stack
        # print(root.value)
        # if root.left:
        #     self.pre_order(root.left)
        # if root.right:
        #     self.pre_order(root.right)

    def in_order(self):

        stack = []

        if self.root is None:
            raise Exception("Tree is empty")

        def _walk(root):

            if root.left:
                _walk(root.left)

            stack.append(root.value)

            if root.right:
                _walk(root.right)

        _walk(self.root)
        return stack

    def post_order(self):

        stack = []

        if self.root is None:
            raise Exception("Tree is empty")

        def _walk(root):

            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)

            stack.append(root.value)

        _walk(self.root)
        return stack


class HashTable(object):
    def __init__(self, size=1024):

        self.size = size
        self.map = [None] * size

    def hash(self, key):
        """
        This method takes an argument of type string (key) and returns an integer value (hash value) which
        is the index  of the key in the table.
        """
        sum_of_ascii = 0
        for char in key:
            char_ascii = ord(char)
            sum_of_ascii += char_ascii
        hashed_key = (sum_of_ascii * 19) % self.size

        return hashed_key

    def set(self, key, value):
        """
        This method takes two arguments:
        1. A type string (key)
        2. Value

        This method does the following tasks:
        - hash the key by calling the hash method
        - set the key and value pair in the table, while handling collisions
        - checks if the key is already in the table, and if so it would update the value for that key to the value
            provided in the method's parameter

        """
        index = self.hash(key)
        if self.map[index] is None:
            self.map[index] = [[key, value]]
        else:
            # check if key is already in the table
            # if so, update the value for that key to the value provided in the method's parameter
            for i in range(len(self.map[index])):
                if self.map[index][i][0] == key:
                    self.map[index][i][1] = value
                    return
            self.map[index].append([key, value])

    def get(self, key):
        """
        This method takes a type string (key) and returns the value associated with that key.
        """
        index = self.hash(key)
        if self.map[index] is None:
            return None
        else:
            for i in range(len(self.map[index])):
                if self.map[index][i][0] == key:
                    return self.map[index][i][1]
            return None

    def contains(self, key):
        """
        This method takes a type string (key) and returns a Boolean:
        True if the key is in the table, and False otherwise.
        """
        index = self.hash(key)
        if self.map[index] is None:
            return False
        else:
            for i in range(len(self.map[index])):
                if self.map[index][i][0] == key:
                    return True
            return False

    def keys(self):
        """
        This method returns a collection of all keys in the table.
        """
        keys = []
        for i in range(len(self.map)):
            if self.map[i] is not None:
                for j in range(len(self.map[i])):
                    keys.append(self.map[i][j][0])
        return keys


def tree_intersection(tree1, tree2):
    """
    This method takes two arguments:
    1. A binary tree (tree1)
    2. A binary tree (tree2)
    and returns a list of values that are in both trees.
    """
    hashtable = HashTable()
    empty = []
    tree1_values = tree1.pre_order()
    tree2_values = tree2.pre_order()

    if tree1.root is None or tree2.root is None:
        raise Exception("Tree is empty")

    for value in tree1_values:
        hashtable.set(str(value), None)
    for value in tree2_values:
        if hashtable.contains(str(value)):
            empty.append(value)
    return empty


if __name__ == "__main__":
    hashtable = HashTable()
    tree1 = BinaryTree()
    tree2 = BinaryTree()

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

    print(tree_intersection(tree1, tree2))
