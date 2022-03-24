
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
    - The to_string method is just another visual repersentaion
    - The includes method is just there to check if a certain value is present in the linked list or not.

    - I also added an additional method (display) that would return a collection or list of the existing
    items in the linked list

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

    def insert(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node


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

    def reverse_linked_list(self):
        previous = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        # exit out of the while loop when the current in None
        # and set the new head node to the previous node
        self.head = previous

    
if __name__ == "__main__":
    ll = LinkedList()
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    loves = Node("loves")
    music = Node("music")

    ll.insert(btoush)
    ll.insert(yahia)       
    ll.insert(batool)
    ll.append(loves)
    ll.append(music)

    # before reversing the linked list
    print("** Before reversing the linked list: **",ll.__str__())
    ll.reverse_linked_list()
    # after reversing the linked list
    print("** After reversing the linked list: **",ll.__str__())