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

    
    def pre_order(self,root):
        stack = []
        
        if root:
            stack.append(root.value)
            stack = stack + self.pre_order(root.left)
            stack = stack + self.pre_order(root.right)
        return stack
            

    def in_order(self, root):
        stack = []
        
        if root:
            stack = stack + self.pre_order(root.left)
            stack.append(root.value)
            stack = stack + self.pre_order(root.right)
        return stack


    def post_order(self, root):
        stack = []
        
        if root:
            stack = stack + self.pre_order(root.left)
            stack = stack + self.pre_order(root.right)
            stack.append(root.value)
        return stack


class BinarySearchClass:
    def add(self, value):
        pass

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
    g = TreeNode("g")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    print(a)
    print(BT.pre_order(a))
    print(BT.in_order(a))
    print(BT.post_order(a))


