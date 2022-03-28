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



class PseudoQueue():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()


    def enQueue(self, node):
        self.stack1.push(node)

    def deQueue(self):
        # if self.stack2.is_empty == True:
        #     self.stack2(self.stack1.pop())
        # return self.stack2.pop()
            
        if not self.stack2.is_empty():
            self.stack2.push(self.stack1.pop())

        if not self.stack1.is_empty():
            return self.stack1.pop()

        if self.stack2.is_empty():
            raise Exception("Stack 2 is empty!")







if __name__ == "__main__":

    stack = Stack()

    # creating nodes
    bat = Node("Bat")
    yahia = Node("Yahia")
    btoush = Node("Btoush")

    # pushing nodes to an empty stack
    # stack.push(btoush)
    # stack.push(yahia)
    # stack.push(bat)

    # # poping a node from a stack
    # # print(stack.__str__())
    # # print(stack.pop())
    # print(stack.__str__())

    # # peeking at the top node
    # print(stack.peek())

    # # is the stack empty?
    # print(stack.is_empty())

    ###################################################################################################    

    pseudoqueue = PseudoQueue()

    pseudoqueue.enQueue(btoush)
    pseudoqueue.enQueue(yahia)
    pseudoqueue.enQueue(bat)
    
    print(pseudoqueue.deQueue())

    