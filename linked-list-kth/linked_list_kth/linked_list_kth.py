from distutils.command.build_scripts import first_line_re
from locale import currency
from tkinter import N


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


     - When appending or inserting into the linked list, the first entery point that through it I can do
    the functionality of those methods is the head, so I have to start from there, and end right before
    the None that the last node in the linked list points to when I'm appending.
    -methods:
    append
    insert_after
    insert_after

    - a length method to calculate the exact length of the linked list
    - find kth value method that takes a k value and return the kth value from the end of the list

    """

    def __init__(self):
        self.head = None

    def __str__(self):

        output = "Head -> "
        if self.head is None:
            output = "Empty linked list"
        else:
            current = self.head
            while current:
                output += f"{current.value} -> "
                current = current.next

            output += "None"
        return output


    def insert(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

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

    def includes(self, value):
        if value == None:
            raise TypeError("argument is missing")
        else:
            current = self.head
            while current is not None:
                if current.value == value:
                    return True
                current = current.next
        return False


    def length(self):
        current = self.head
        total = 0
        while current is not None:
            total +=1
            current = current.next
        
        return total 
   

    def find_kth(self,k):
        first_pointer = self.head
        second_pointer = self.head


        if k >= 0 and k < self.length():
            for i in range(k):
                second_pointer = second_pointer.next
            while second_pointer.next is not None:
                second_pointer = second_pointer.next
                first_pointer = first_pointer.next
            return first_pointer.value
        
        if k > self.length():
            return ('The kth value is out of range')
        
        if  k < 0 and k < self.length():
            return ('The kth value is of negative value, please provide a positive one!')

        if type(k) != int:
            return ('The kth value is not an integer, please provide an int value!')
        
         

    def to_string(self):
        return self.__str__()
        # return f'{self.head} -> {self.head.next} -> {self.head.next.next} -> {self.head.next.next.next} -> {self.head.next.next.next.next} -> {self.head.next.next.next.next.next}'

   

if __name__ == "__main__":
    # bat = Node("Bat")
    # print(bat)
    # print(LinkedList)

    # ll = LinkedList()
    # ll.head = Node ('one')
    # ll.head.next = Node("Batool")
    # ll.head.next.next = Node('Yahia')
    # print(ll)

    ll = LinkedList()
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    one = Node("number 1")
    two = Node("number 2")
    # ll.append(batool)
    # ll.append(yahia)
    # ll.append(btoush)
    # ll.append(one)
    # ll.append(two)
    # ll.insert(btoush)
    # ll.insert(yahia)
    ll.insert(btoush)
    ll.insert(yahia)
    ll.insert(batool)

    ll.append(two)

    # print(ll.to_string())
    print(ll.__str__())
    # print(ll.includes("Batool"))
    # print(ll.includes("one"))
    # print(ll.length())
    print(ll.find_kth(2))
    # print(one)
    # print(ll.display())
