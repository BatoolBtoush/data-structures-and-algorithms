# **Trees**

Trees are non-linear data structures in which nodes are linked by edges. The root node acts as the Parent node, while the left and right nodes act as Child nodes.

### ***In binary trees:***
- I could have a singular root node and many leaves.
- I should only have one root.
- I could have at most 2 children, and 1 or zero children are allowed.

<br>


### ***Traversing through the binary tree is important for:***

- searching for nodes.
- printing the tree as a whole. And it can be done in either of two ways:

    - **Depth First:** uses a call stack aka recursion to traverse the height/depth of the tree.

    - **Breadth First:** uses a queue.


### ***Depth First traversal***

is when we prioritize going through the depth (height) of the tree first. And it can be carried out in three different ways:

- **Pre-order:** root >> left >> right
- **In-order:** left >> root >> right
- **Post-order:** left >> right >> root

<br>

### ***Binary Search Trees***
In this type of tree, nodes are organized in a way where the values that are smaller than the root are placed to the left, and all the values that are larger than the root are placed to the right.


Searching through a Binary Search Trees
It's done by comparing the node we're looking for to the tree's or sub-tree. We only scan the left side if the value is smaller or only scan the right side if the value is larger.

 
<br>

<br>


## **Challenge**

1. Create a **Node class** that has properties for the value stored in the node, the left child node, and the right child node.

2. Create a **Binary Tree class**and define a method for each of the depth first traversals:
- pre order
- in order
- post order which returns an array of the values, ordered appropriately.

3. Create a **Binary Search Tree class** and this class should be a sub-class of the Binary Tree Class, with the following additional methods:
- Add

    - Arguments: value
    - Return: nothing
    - Adds a new node with that value in the correct location in the binary search tree.
- Contains
    - Argument: value
    - Returns: boolean indicating whether or not the value is in the tree at least once.


4. Structure and Testing: Utilizing the Single-responsibility principle


<br>

<br>

## **Approach & Efficiency**


### ***Depth First traversal***

- **Big O time complexity:** O(n)

- **Big O space complexity:** O(n)

<br>



### ***Binary Search Trees***


- **Big O time complexity:** O(h), h: height (balanced binary tree)

- **Big O space complexity:** O(1)


<br>

<br>

## **API**

- **Pre-order:** traverses throguht the tree in this way:
    root >> left >> right

    and output a list of the nodes in the tree

<br>

- **In-order:** traverses throguht the tree in this way:

    left >> root >> right

    and output a list of the nodes in the tree

<br>

- **Post-order:** traverses throguht the tree in this way:

    left >> right >> root

    and output a list of the nodes in the tree

<br>

- **add:** adds a new node into the binary tree, depending on whether it's greater or less than the self.root or the current node I'm looking at.

<br>

- **contains:** returns a boolean indicating whether or not the value is in the tree at least once.