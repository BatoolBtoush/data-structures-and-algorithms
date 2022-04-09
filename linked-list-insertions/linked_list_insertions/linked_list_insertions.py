class Node:
    """
    - This class is the first step when creating a custom linked list
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


class LinkedList:
    """
    - This class takes care of building a chain of nodes with the help of the Node class.
    - The __init__ method only determins the head node as it is the first entery point to any linked list,
    and since the linked list hasn't been created yet, then it's set to None.
    - The __str__ method shows a better visual of the linked list.
    - When appending or inserting into the linked list, the first entery point that through it I can do
    the functionality of those methods is the head, so I have to start from there, and end right before
    the None that the last node in the linked list points to when I'm appending.
    -methods:
    append
    insert_after
    insert_after
    """

    def __init__(self):
        self.head = None

    def __str__(self):

        output = ""
        if self.head is None:
            output = "Empty linked list"
        else:
            current = self.head
            while current:
                output += f"{current.value} -> "
                current = current.next

            output += "None"
        return output

    def append(self, node):
        if self.head is None:
            self.head = node

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node



    def insert_before(self, node, newnode):
        if self.head is None:
            self.head = node
            
        current = self.head
        if current.value == node.value:
             newnode.next = current
             self.head = newnode
             return

        while current is not None:
            if current.next.value == node.value:
                newnode.next = current.next
                current.next = newnode
                return 
            current = current.next


    def insert_after(self, node, newnode):
        if self.head is None:
            self.head = node
            
        current = self.head
        while current is not None:
            if current.value == node.value:
                newnode.next = current.next
                current.next = newnode
                return 
            current = current.next
        # if self.head is None:
        #      return
             
        # current = self.head
        # while current:
        #     if current.value == node.value:
        #         current.next = newnode
        #     current = current.next
        # return
            

if __name__ == "__main__":
    
    ll = LinkedList()
    # head = Node("head")
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    one = Node("number 1")
    two = Node("number 2")
    before = Node('added before')
    after = Node('added after')

    
    ll.append(batool)
    ll.append(yahia)
    ll.append(btoush)
    ll.append(one)
    ll.append(two)
    # ll.insert_after(two,four)
    ll.insert_after(two,after)
    # ll.insert_after(btoush,four)    
    print(ll.__str__())
  