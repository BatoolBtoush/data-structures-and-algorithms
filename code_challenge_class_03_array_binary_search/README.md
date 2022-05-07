# Binary Search of Sorted Array

You're asked to write a function that takes two inputs or arguments, one is a sorted list, the other is a search key and you have to return the index of the list’s element that is equal to the value of the search key or return -1 if the search key doesn't exist in the list.


**Inputs** = a sorted list and a search key.

**Output** = the index of the element that matches the search key


<br>


## Whiteboard Process
![Array Binary Search for code challenge class 03](/code_challenge_class_03_array_binary_search/array-binary-search.jpg)


<br>


## Approach & Efficiency

The approach I took was to first determine the highest and lowest values in the list to help me determine the mid value, that I will start my search in. And if the search key value matches the element in the mid index then return that index, if not; then ask if the search key is greater or less than the mid index value and based on that cut the list into a smaller list with different values of low and high, and repeat iteration until mid index is returned.

But if the search key doesn't exist in the list, then return -1.


<br>

**Big o complexity**

Time = O(logN).

Space  = O(logN).
