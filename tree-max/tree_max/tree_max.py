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


    def max_tree(self):

        def _walk(root):
            currnet = root
            left_current = _walk(root.left)
            right_currnet = _walk(root.right)
            
            if (left_current.value > currnet.value):
                currnet = left_current
            if (right_currnet.value > currnet.value):
                currnet = right_currnet
            return currnet.value



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




        # current = root
        # left_current = root.left
        # right_currnet = root.right
        # if right_currnet.value > current.value:
        #     current = right_currnet
        # if left_current.value > current.value:
        #     current = left_current

        # return current.value

            
            


if __name__ == "__main__":
    BT = BinaryTree()
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(99)
    e = TreeNode(5)
    f = TreeNode(6)

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
    print(BT.max_tree())