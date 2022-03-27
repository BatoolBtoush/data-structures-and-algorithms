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
    - zip_lists methods, that takes two input arguments:
      linked list 1 and linked list 2
      output the zipped or merged linked list of the two combined into one, after adjusting
      the next pointers.

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


def zip_lists(list1, list2):
        # initiate the start of each linked list
        list1_current = list1.head
        list2_current = list2.head

        # swap between the two linked lists
        while list1_current != None and list2_current != None:

            # save next pointers
            list1_next = list1_current.next
            list2_next = list2_current.next

            # change next pointers
            list2_current.next = list1_next
            list1_current.next = list2_current

            # update current pointers for next iteration
            list1_current = list1_next
            list2_current = list2_next

        # exit out of the while loop once current value of any linked list is equal to none
        # which means when one linked list is shorter than the other
        list1.append(list2_current)
        return list1



if __name__ == "__main__":

    llist1 = LinkedList()
    llist2 = LinkedList()

    # nodes for the first linked list
    batool = Node("Batool")
    yahia = Node("Yahia")
    btoush = Node("Btoush")
    one = Node("number 1")
    two = Node("number 2")
    llist1.insert(btoush)
    llist1.insert(yahia)
    llist1.insert(batool)
    llist1.append(one)
    llist1.append(two)

    # nodes for the second linked list
    emily = Node("Daisy")
    adam = Node("Adam")
    jb = Node("JB")
    three = Node("number 3")
    four = Node("number 4")
    llist2.insert(jb)
    llist2.insert(adam)
    llist2.insert(emily)
    llist2.append(three)
    llist2.append(four)

    # nodes from code challenge 08
    # num1 = Node(1)
    # num3 = Node(3)
    # num2 = Node(2)
    # llist1.insert(num2)
    # llist1.insert(num3)
    # llist1.insert(num1)

    # num5 = Node(5)
    # num9 = Node(9)
    # num4 = Node(4)
    # llist2.insert(num4)
    # llist2.insert(num9)
    # llist2.insert(num5)
    print(zip_lists(llist1, llist2))
    # print(llist1.__str__())
    # print(llist2.__str__())
