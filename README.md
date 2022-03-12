# data-structures-and-algorithms


# Singly Linked List
Linked lists are just another way to structure or organize our data, and store them in sequence. As it can grow or shrink in size.
They consist of group of nodes, and each node holds 2 things:

1. value
2. a reference to the next node (some sort of an address) because node in linked list are scattered all over the place in the memory, not like arrays where they're given a block of memory where each element follows the previous.


## Challenge
Create a custom linked list, by creating two classes: Node and LinkedList
and in each class I have to use **__init__()** method to set the needed attributes, where in the Node class it's only the value. And in the LinkedList class it's the head node.

In the LinkedList class I have to create additional methods to do some functionalities for me while traversing through the list
```
   class Node:
       def __init__(self, value):
        self.value = value
        self.next = None
```
```
 class LinkedList:
      def __init__(self):
          self.head = None
```


And after creating each class in a file called *linked_list.py* I have to do some testing for each functionality in file called *test_linked_list.py*



## Approach & Efficiency
The approach I took is demonstrated in my code.
Regarding the efficiency and the Big O aspect of things....

When I inserted into the beginning of the linked list using **insert** method the time compliexity was O(1) because it was only required to search for the head node and 
implement the new node there instead.

But when appending using **append** method the time complexity was O(n) because I had to go through all the nodes in the list until I reached the end of it.

When using the **includes** method to check whether a certain value was present in the linked list, the time complexity was O(n) of course because the value I'm looking
for might be at the end.


## API
- [x] created a Node class
- [x] created a LinkedList class
- [x] added every required method in each class
- [x] wrote additional methods
- [x] wrote the required tests
- [x] my tests passed


- [x] created the Insert method to help add nodes to the beginning of the list.
- [x] created the includes method to look for a certain value in the linked list.
- [x] created the to_string method to provide a represtation of the LinkedList class instances.
- [x] did some testing for each method.
- [x] my tests passed.
