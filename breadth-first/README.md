# **Challenge Summary**

You're asked to write a function called breadth_first that takes an arguments of the binary tree and returns a list of all values in the tree, in the order they were encountered


<br>

## **Whiteboard Process**
<!-- Embedded whiteboard image -->

<br>

## **Approach & Efficiency**
***Approach:***
- Create an empty queue
- Start from root and appeand it into the queue
- Loop while root is not TRUE:
    b) Enqueue root’s children into the queue
      starting from left to right children
    c) Dequeue a node from the queue

***Big O:***

- Time Complexity: O(n) 
- Space Complexity: O(n) 

## **Solution**