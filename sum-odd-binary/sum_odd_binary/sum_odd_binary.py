class Node:
    """
    - The __init__ method I have to consider the value the node contain,
    but since the node isn't added yet, then the node will point to None.
    - The __str__ I can choose the kind of representation I want to for each node I create.
    """

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"


class Queue:
    """
    - The __init__ method: creates an empty queue when instantiated.
    with a property of a front and a rear node, but since the front and rear aren't added yet,
    they will point to None.
    - The __str__ I can choose the kind of representation I want to for each node I create.
    - The enqueue(): Changes the next property of the rear node to point to the node we are adding
     and re-assigns the rear reference or pointer to point to the node we are adding.
    - The dequeue(): Creates a temporary reference named temp and have it point to the same node
    that front is pointing too. And re-assigns front to the next value that the node front is pointing to.
    Also re-assigns the next property on the temp node to None.
    - The peek(): This method is for inspecting the front node of the queue.
    - The is_empty(): This method returns a True or False, based on the existance of a top node or not.
    (empty queue or not).
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def __str__(self):
        output = ""
        if self.front is None:
            output = "Empty Queue"
        else:
            current = self.front
            while current:
                output += f"{current.value} -> "
                current = current.next

            output += "None"
        return output

    def enqueue(self, data):
        node = Node(data)

        if self.front is None:
            self.front = node
            self.rear = node
        # if the queue isn't empty
        # then add the new node in the rear of the queue
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty() == True:
            raise Exception("Nothing to dequeue from, the queue is empty!!")
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value

    def peek(self):
        if self.is_empty() == True:
            raise Exception("Nothing to peek at, the queue is empty!!")
        else:
            return self.front.value

    def is_empty(self):
        return self.front == None


class TreeNode:
    """
    Class for initializing a tree nodes.
    Each node has a value and almost everyone of which has a left and a right child.
    """

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return f"{self.value} --> {self.right}"

    # def __str__(self):
    #     return f"{self.value} --> {self.left}"


class BinaryTree:
    """ "
    Class for initializing a binary tree with nodes, which are linked to each other.
    The root node is the first node in the point of access to the tree.

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


class BinarySearch(BinaryTree):
    """
    Class that is a child-class of the Binary Tree Class.

    The special characteristics of the Binary Search Tree are:
    - The left child of a node is always less than the parent(root) node.
    - The right child of a node is always greater than the parent(root) node.


    Class methods:
    - add() - adds a node to the tree, according to the Binary Search Tree rules.
    - contains() - checks if a node is in the tree. Returns True if it exists or False if it doesn't.
    - sum_of_odd_numbers_pre_order_traversal() - returns the sum of all the odd nodes in the tree using the
    pre-order traversal.

    """

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

    def sum_of_odd_numbers_pre_order_traversal(self):
        """
        Returns the sum of all the odd nodes in the tree using the pre-order traversal.
        """
        sum = 0
        if self.root is None:
            raise Exception("Tree is empty")

        def _walk(root):
            nonlocal sum
            if root.value % 2 != 0:
                sum += root.value
            if root.left:
                _walk(root.left)
            if root.right:
                _walk(root.right)

        _walk(self.root)
        return sum


def breadth_first(tree):
    output = []
    queue = Queue()
    queue.enqueue(tree.root)

    if not tree.root:
        raise Exception("The tree is empty!")

    while not queue.is_empty():
        dequeued = queue.dequeue()
        if dequeued:
            output.append(dequeued.value)

        if dequeued.left:
            queue.enqueue(dequeued.left)
        if dequeued.right:
            queue.enqueue(dequeued.right)

    return output


def sum_of_odd_numbers_breadth_first_traversal(tree):
    """
    Returns the sum of all the odd nodes in the tree using the breadth-first traversal.
    """
    sum = 0
    queue = Queue()
    queue.enqueue(tree.root)

    if not tree.root:
        raise Exception("The tree is empty!")

    while not queue.is_empty():
        dequeued = queue.dequeue()

        if dequeued:
            if dequeued.value % 2 != 0:
                sum += dequeued.value

        if dequeued.left:
            queue.enqueue(dequeued.left)
        if dequeued.right:
            queue.enqueue(dequeued.right)

    return sum


if __name__ == "__main__":

    # ********************************************************************************************
    # BT = BinaryTree()
    # a = TreeNode("A")
    # b = TreeNode("B")
    # c = TreeNode("C")
    # d = TreeNode("D")
    # e = TreeNode("E")
    # f = TreeNode("F")
    # a.left = b
    # a.right = c
    # b.left = d
    # b.right = e
    # c.left = f
    # BT.root = a
    # print("Pre Order traversal BT: ", BT.pre_order())
    # print("In Order traversal BT: ", BT.in_order())
    # print("Post Order traversal BT: ", BT.post_order())
    # print("Breadth First traversal BT: ", breadth_first(BT))

    # ********************************************************************************************
    BTS = BinarySearch()
    # a = TreeNode(13)
    # BTS.root = a
    # BTS.add(12)
    # BTS.add(21)
    # BTS.add(3)
    # BTS.add(10)
    # BTS.add(5)
    # BTS.add(97)
    # BTS.add(101)
    # BTS.add(200)
    # BTS.add(6)

    a = TreeNode(8)
    BTS.root = a
    BTS.add(3)
    BTS.add(1)
    BTS.add(6)
    BTS.add(4)
    BTS.add(7)
    BTS.add(10)
    BTS.add(14)
    BTS.add(13)

    
    print("Pre Order traversal BTS: ", BTS.pre_order())
    print("In Order traversal BTS: ", BTS.in_order())
    print("Post Order traversal BTS: ", BTS.post_order())
    print("Breadth First traversal BTS: ", breadth_first(BTS))
    print("Does it contain: ", BTS.contains(9))
    print(
        "Summation of odd numbers using pre order: ",
        BTS.sum_of_odd_numbers_pre_order_traversal(),
    )
    print(
        "Summation of odd numbers using breadth first: ",
        sum_of_odd_numbers_breadth_first_traversal(BTS),
    )
