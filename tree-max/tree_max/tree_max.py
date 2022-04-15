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

    def tree_max(self):

        current_maximum = self.root.value

        def _walk(value):
            nonlocal current_maximum

            if current_maximum is None:
                raise Exception("Tree is empty!")

            if value.value > current_maximum:
                current_maximum = value.value

            if value.left:
                _walk(value.left)

            if value.right:
                _walk(value.right)

        _walk(self.root)

        return current_maximum

        # def _walk(root):
        #     currnet = root
        #     left_current = _walk(root.left)
        #     right_currnet = _walk(root.right)

        #     if left_current.value > currnet.value:
        #         currnet = left_current
        #     if right_currnet.value > currnet.value:
        #         currnet = right_currnet
        #     return currnet.value

        # currnet = self.root.value

        # def _walk(node):

        #     current = node
        #     if node.value > current.value:
        #         current = node.value

        #     if node.left:
        #         _walk(node.left)

        #     if node.right:
        #         _walk(node.right)

        # _walk(self.root)
        # return currnet.value


if __name__ == "__main__":
    BT = BinaryTree()
    # a = TreeNode(90)
    # b = TreeNode(33)
    # c = TreeNode(3)
    # d = TreeNode(99)
    # e = TreeNode(22)
    # f = TreeNode(200)

    # a.left = b
    # a.right = c
    # b.left = d
    # b.right = e
    # c.left = f

    # BT.root = a

    root = TreeNode(90)
    root.left = TreeNode(33)
    root.right = TreeNode(3)
    root.left.left = TreeNode(99)
    root.left.right = TreeNode(22)
    root.right.left = TreeNode(200)

    BT.root = root

    print(BT.pre_order())
    print(BT.in_order())
    print(BT.post_order())
    print("max value in the tree is:", BT.tree_max())
