# data-structures-and-algorithms

# Challenge Summary

You're asked to create your own linked list by coding a class that takes has these methods:
1. append: has one argument of the value/node to be added to the end of the linked list
2. insert before: has two arguments (value to add before, new value to be added)
3. insert after: has two arguments (value to add after, new value to be added).

the linked list should look something like this:
                  head -> {}-> {}-> {}-> None



## Whiteboard Process
![whiteboard1](/linked-list-insertions/assests/linked-list-insertion1.jpg)
![whiteboard2](/linked-list-insertions/assests/linked-list-insertion2.jpg)
![whiteboard3](/linked-list-insertions/assests/linked-list-insertion3.jpg)


## Approach & Efficiency
The approach taken is also explained in the whiteboard, but mainly to always make sure to enter the linked list from the head node and from there start comparing and seeing if the headnode.next value is equal to the value i want to add before or after, and how to change the pointer if the condition is met.


Time complexity - O(N)
Space complexity - O(1)

overall the complexity would be of O(N) as I would be obligated to traverse through the linked list each time.

## Solution
The procedure to run my code is described in the whiteboard.
and other tests have been made there

