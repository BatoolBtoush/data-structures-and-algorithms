class Node:
    """
    - The __init__ method I have to consider the value the node contain,
    but since the node isn't added to the linked list yet, then the node
    will point to None.
    - The __str__ I can choose the kind of representation I want to for each node I create.
    """

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"

class Stack:
    def __init__(self):
        self.top = None

    def __str__(self):
        output = ""
        if self.top is None:
            output = "Empty stack"
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
        # save the top in a temp value
        temp = self.top
        # re-assign the next of the previous top value as the new top node
        self.top = self.top.next
        # deleting the node by having it point to None
        temp.next = None
        return temp.value


    def peek(self):
        return self.top.value


    def is_empty(self):
        return self.top == None




if __name__ == "__main__":
    # empty stack
    stack = Stack()
    # print("empty stack",stack)

    # creating nodes
    bat = Node("Bat")
    yahia = Node("Yahia")
    btoush = Node ("Btoush")
    # print(bat)

    # pushing nodes to an empty stack
    stack.push(btoush)
    stack.push(yahia)
    stack.push(bat)
    
    # print("not an empty stack",stack)

    # poping a node from a stack
    print(stack.__str__())
    print(stack.pop())
    print(stack.__str__())



    