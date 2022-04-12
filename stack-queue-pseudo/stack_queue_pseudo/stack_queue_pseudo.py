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

    def length(self):
        current = self.top
        total = 0
        while current is not None:
            total += 1
            current = current.next

        return total

    def is_empty(self):
        return self.top == None


class PseudoQueue:

    """
    This class implement a Queue using two stacks and utilizing 2 Stack instances to create
    and manage the queue.

    input: self, nodes
    output : return popped node from stack2

    Methods:
        enqueue: has an arguments of a node and it inserts this node into the PseudoQueue class.
        dequeue: has no arguments it only extracts the node from the PseudoQueue class.
    """

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def __str__(self):
        output = ""
        if self.stack1.top is None:
            output = "Empty stack1"
        else:
            current = self.stack1.top
            while current:
                output += f"{current.value} -> "
                current = current.next
            output += "None"
        return output

    def enqueue(self, node):

        # if stack 1 is not empty, then empty its componenents into stack 2 by pushing them
        # and after that, push into stack 1 the node normally
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        self.stack1.push(node)

        # now get back all the elements from stack 2 into stack 1
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

    def dequeue(self):

        if self.stack1.is_empty() and self.stack2.is_empty():
            raise Exception("Empty Queue!")

        elif self.stack2.is_empty():
            while not self.stack1.is_empty():
                return self.stack1.pop()

        else:
            return self.stack1.pop()

    # def __init__(self):
    #     self.stack1 = []
    #     self.stack2 = []

    # def enQueue(self, node):

    #     while len(self.stack1) != 0:
    #         self.stack2.append(self.stack1[-1])
    #         self.stack1.pop()

    #     self.stack1.append(node)

    #     while len(self.stack2) != 0:
    #         self.stack1.append(self.stack2[-1])
    #         self.stack2.pop()

    # def deQueue(self):

    #     if len(self.stack1) == 0:
    #         print("Q is Empty")

    #     x = self.stack1[-1]
    #     self.stack1.pop()
    #     return x


if __name__ == "__main__":
    # stac = Stack()
    # creating nodes
    bat = Node("Bat")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    # stac.push(bat)
    # print(stac.length())

    ###################################################################################################

    pseudoqueue = PseudoQueue()
    pseudoqueue.enqueue(btoush)
    pseudoqueue.enqueue(yahia)
    # pseudoqueue.enqueue(bat)
    print(pseudoqueue.__str__())
    # # print(pseudoqueue.dequeue())
    # # print(pseudoqueue.__str__())
    # print(pseudoqueue.deQueue())
