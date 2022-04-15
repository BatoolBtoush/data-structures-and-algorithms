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


class BinarySearch(BinaryTree):
    def add(self, value):

        if self.root is None:
            self.root = TreeNode(value)

        if self.root.value == value:
            raise Exception("Value already exists in the tree!")

        current = self.root
        while current:
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    break
                else:
                    current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = TreeNode(value)
                    break
                else:
                    current = current.right
            else:
                break

    def contains(self, value):

        current = self.root
        while current:
            if current.value == value:
                return True
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right

        return False


if __name__ == "__main__":
    BT = BinaryTree()
    BTS = BinarySearch()
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    BT.root = a

    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)

    # BT.root = root
    BT.root = a

    print(BT.pre_order())
    print(BT.in_order())
    print(BT.post_order())

    BTS.add(7)
    BTS.add(8)
    BTS.add(9)
    BTS.add(10)

    #print(BTS.contains(9))
