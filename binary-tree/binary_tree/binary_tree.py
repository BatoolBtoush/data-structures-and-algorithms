from lib2to3.pytree import Node


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return f"{self.value} --> {self.right}"

    # def __str__(self):
    #     return f"{self.value} --> {self.left}"


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        stack = []

        def _walk(root):
            stack.append(root.value)

            if root.left:
                _walk(root.left)
            if root.right:
                _walk(root.right)

        _walk(self.root)
        return stack

    def in_order(self):

        stack = []

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

        def _walk(root):

            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)

            stack.append(root.value)

        _walk(self.root)
        return stack


class BinarySearchClass:
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            def _walk(value):
            

            _walk(value, self.root)




    def contains(self, value):
        pass


if __name__ == "__main__":
    BT = BinaryTree()
    a = TreeNode("a")
    b = TreeNode("b")
    c = TreeNode("c")
    d = TreeNode("d")
    e = TreeNode("e")
    f = TreeNode("f")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f

    BT.root = a

    print(a)
    print(BT.pre_order())
    print(BT.in_order())
    print(BT.post_order())
