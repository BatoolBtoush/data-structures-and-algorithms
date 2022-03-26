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


class Stack:
    """
    - The __init__ method: creates an empty Stack when instantiated.
    with a property of a top node, but since the top isn't added yet, then the top will point to None.
    - The __str__ I can choose the kind of representation I want to for each node I create.
    - The push(): To add or push a node into the stack, I would assign it as the new top,
    with its next pointing to the original top.
    - The pop(): To remove or pop a node off the stack we are removing it from the top.
    So the top node will be re-assigned to the node that lives below and the top node is returned to the user.
    - The peek(): This method is for inspecting the top node of the stack.
    -The is_empty(): This method returns a True or False, based on the existance of a top node or not.
    (empty stack or not).


    """

    def __init__(self):
        self.top = None

    def __str__(self):
        output = ""
        if self.top is None:
            output = "Empty Stack"
        else:
            current = self.top
            while current:
                output += f"{current.value} -> "
                current = current.next

            output += "None"
        return output

    def push(self, node):
        # if the stack is empty, push the new node to the top node
        if self.top is None:
            self.top = node
        # if the stack isn't empty
        # then make the new node as the top and the previous top node is the next of the new top node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.is_empty() == True:
            raise Exception("Nothing to pop from, the stack is empty!!")
        else:
            # save the top in a temp value
            temp = self.top
            # re-assign the next of the previous top value as the new top node
            self.top = self.top.next
            # deleting the node by having it point to None
            temp.next = None
            return temp.value

    def peek(self):
        if self.is_empty() == True:
            raise Exception("Nothing to peek at, the stack is empty!!")
        else:
            return self.top.value

    def is_empty(self):
        return self.top == None


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

    def enqueue(self, node):
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


if __name__ == "__main__":
    # empty stack
    stack = Stack()
    # print("empty stack",stack)

    # creating nodes
    bat = Node("Bat")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    # print(bat)

    # pushing nodes to an empty stack
    # stack.push(btoush)
    # stack.push(yahia)
    # stack.push(bat)

    # print("not an empty stack",stack)

    # poping a node from a stack
    # print(stack.__str__())
    # # print(stack.pop())
    # # print(stack.__str__())

    # # peeking at the top node
    # print(stack.peek())

    # # is the stack empty
    # print(stack.is_empty())

    ###################################################################################################

    # empty queue
    queue = Queue()
    # print("empty queue", queue)

    # creating nodes
    bat = Node("Bat")
    yahia = Node("Yahia")
    btoush = Node("Btoush")

    # empty queue before enqueuing node into the queue
    # print(queue.__str__())

    # enqueuing nodes
    queue.enqueue(bat)
    queue.enqueue(yahia)
    queue.enqueue(btoush)

    # not an empty queue
    # print(queue.__str__())

    # dequeuing a node from a queue
    print(queue.__str__())
    print(queue.dequeue())
    # print(queue.dequeue())
    print(queue.is_empty())
    print(queue.peek())
    print(queue.__str__())
