# Stacks and Queues
**Stack**:

A stack is a data structure that consists of Nodes. Each Node only references the next Node in the stack and not the ond before it.

~ What can be doen on a stack is:

Push: To add nodes or items into the stack

Pop: To remove nodes or items from the stack. When attempting to pop an empty stack an exception will be raised.

Top: This is the top of the stack.

Peek: To view the top node of the stack. When attempting to peek an empty stack an exception will be raised.

IsEmpty: A methid that returns true when stack is empty otherwise returns false.

<br>

~ Concepts for handling stacks:

FILO: First In Last Out This means that the first item added in the stack will be the last item popped out of the stack.

LIFO: Last In First Out This means that the last item added to the stack will be the first item popped out of the stack.

<br>
<br>

**Queue**:

~ What can be doen on a queue:

Enqueue: To add nodes or items to the queue.
Dequeue: To remove items or nodes from the queue. And if the queue is empty an exception will be raised.
Front: This is the front/first node of the queue.
Rear: This is the rear/last node of the queue.
Peek: To view the value of the front node in the queue. And if the queue is empty an exception will be raised.
IsEmpty: A method that returns true when queue is empty otherwise returns false.
 
<br>

~ Concepts for handling queues:

FIFO: First In First Out This means that the first item in the queue will be the first item out of the queue.

LILO: Last In Last Out This means that the last item in the queue will be the last item out of the queue.

<br>

<br>

 

 
## Challenge
Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

Create a Stack class that has a top property, and the following methods:
- push
- pop
- peek
- is empty

Create a Queue class that has a front and a rear property, and the following methods:
- enqueue
- dequeue
- peek
- is empty


<br>

<br>



## Approach & Efficiency

The **approach** was to create several methods inside each class, and those methods were to add, delete and ispect nodes from the stack and queue.

While of course considering the difference between the stack and queue in how or where to add the nodes and from where to delete.

<br>

The **big O** in the stack's methods:
1. The push method: O(1)
2. The pop method: O(1)
3. The peek method: O(1)

Because it doesn't matter how many nodes are in the stack (n), as these previous methods always take the same amount of time to perform the operation.

The big O in the queue's methods:
1. The enqueue method: O(1)
2. The dequeue method: O(1)
3. The peek method: O(1)

Because it doesn't matter how many nodes are in the queue (n), as these previous methods always take the same amount of time to perform the operation.


<br>

<br>


## API
~ The push method: O(1)

To add or push a node into the stack, I would assign it as the new top, with its next pointing to the original top.

<br>


~ The pop method: O(1)

To remove or pop a node off the stack we are removing it from the top. So the top node will be re-assigned to the node that lives below and the top node is returned to the user.

<br>

~ The peek method:

This method is for inspecting the top node of the stack.

<br>

~ The isEmpty method:

This method returns a True or False, based on the existance of a top node or not. (empty stack or not).

<br>

~ The enqueue method:

1. Change the next property of the rear node to point to the node we are adding.

2. Re-assign the rear reference or pointer to point to the node we are adding.

 
<br>

~ The dequeue method:

1. Create a temporary reference named temp and have it point to the same node that front is pointing too.

2. Re-assign front to the next value that the node front is pointing to.

3. Re-assign the next property on the temp node to None.

<br>

~ The peek method:

This method is for inspecting the front node of the queue.

<br>

~ The isEmpty method:

This method returns a True or False, based on the existance of a top node or not. (empty queue or not).

 