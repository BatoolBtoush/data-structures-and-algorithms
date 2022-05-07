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

    # print(a)
    print(BT.pre_order())
    print(BT.in_order())
    print(BT.post_order())
    print(breadth_first(BT))
