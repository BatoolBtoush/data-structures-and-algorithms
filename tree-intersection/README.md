# **Challenge Summary**

You're asked to find common values in 2 binary trees, by writing a function called ```tree_intersection``` that takes two binary trees as parameters.

Using your Hashmap implementation as a part of your algorithm, return a set of values found in both trees.

<br>

## **Whiteboard Process**
<!-- Embedded whiteboard image -->

<br>

## **Approach & Efficiency**

### **Approach:**

    - Create a Hashmap to store the values of the first tree
    - Create a Hashmap to store the values of the second tree
    - Iterate through the first tree and check if the value exists in the second tree
    - If it does, add it to a set
    - Return the set

### **Efficiency:**

    - Time: O(n)
    - Space: O(n)


<br>

## **Solution**
<!-- Show how to run your code, and examples of it in action -->